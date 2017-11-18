__author__ = 'Naheed'

import pandas as pd
import re

# Regexes for record parsing from papers file
title_pattern = re.compile("#\*([^\r\n]*)")
author_pattern = re.compile("#@([^\r\n]*)")
affiliations_pattern = re.compile("#o([^\r\n]*)")
year_pattern = re.compile("#t([0-9]*)")
venue_pattern = re.compile("#c([^\r\n]*)")
id_pattern = re.compile("#index([^\r\n]*)")
refs_pattern = re.compile("#%([^\r\n]*)")
abstract_pattern = re.compile("#!([^\r\n]*)")


class Paper(object):
    __slots__ = ['id', 'title', 'authors', 'venue', 'refs', 'year', 'abstract']
    csv_header = ('id', 'title', 'venue', 'year', 'abstract')

    def __init__(self, id, title, authors, venue, refs, abstract, year):
        self.id = int(id)  # important
        self.title = title
        self.venue = venue  # important
        self.refs = [int(ref) for ref in refs]  # less important
        self.year = int(year) if year else None  # important
        self.authors = [a.encode('utf-8') for a in authors.split(',') if a]  # important
        self.abstract = abstract if abstract else None

    @property
    def csv_attrs(self):
        attrs = [getattr(self, attr) for attr in self.csv_header]
        return [unicode(attr) if attr else u'' for attr in attrs]

    def __str__(self):
        # return str(self.id)+':'+str(self.year)
        return ",".join(self.authors)

class GraphReader:
    def __init__(self, source):
        self.sourcefile = source
        self.container = None

    def read_citationnetwork(self):
        print self.sourcefile
        self.container = self.iterpapers()
        return self.container

    def match(self, line, pattern):
        """Return first group of match on line for pattern."""
        m = pattern.match(line)
        return m.groups()[0].decode('utf-8').strip() if m else None

    def fmatch(self, f, pattern):
        """Call `match` on the next line of the file."""
        return self.match(f.readline(), pattern)

    def nextrecord(self, f):
        """Assume file pos is at beginning of record and read to end. Returns all
        components as a Paper instance.
        """
        fmatch = self.fmatch
        match = self.match

        title = fmatch(f, title_pattern)
        if title is None:
            return None

        authors = fmatch(f, author_pattern)

        # f.readline()  # discard affiliation info
        year = fmatch(f, year_pattern)
        venue = fmatch(f, venue_pattern)
        paperid = fmatch(f, id_pattern)

        # read out reference list
        refs = []
        line = f.readline()
        m = match(line, refs_pattern)
        while m is not None:
            if m:
                refs.append(m)
            line = f.readline()
            m = match(line, refs_pattern)

        abstract = match(line, abstract_pattern)
        if line.strip(): f.readline()  # consume blank line

        return Paper(
            id=paperid,
            title=title,
            authors=authors,
            year=year,
            venue=venue,
            refs=refs,
            abstract=abstract
        )

    def iterpapers(self):
        """Return iterator over all paper records."""
        with open(self.sourcefile, 'r') as f:
            record = self.nextrecord(f)
            while record is not None:
                yield record
                record = self.nextrecord(f)
