__author__ = 'Naheed'

from GraphReader import Paper


class Author:
    def __init__(self,id,name,papers_published):
        self.id = id
        self.name = name
        assert isinstance(papers_published,list)
        self.papers = papers_published

    def add_paper(self,paper):
        assert isinstance(paper,Paper)
        self.papers.append(paper)

    def __str__(self):
        return str(self.id).encode('utf-8')+":".encode('utf-8')+self.name

class GraphProcessor:
    def __init__(self, paperiterator):
        self.it = paperiterator
        self.author_list = [] # List of Author Objects
        self.paper_to_authorsmap = {}  # key = paperid, value = list of authors_id

    def convert_to_hyperedgelist(self):
        authorids = {}  # authorname to authorid map
        uniqueid = 0
        for paper in self.it:
            assert isinstance(paper, Paper)
            authorid_list = []

            for author in paper.authors:
                author_id = authorids.get(author, None)
                if author_id is None: # New Author
                    author_id = uniqueid
                    authorids[author] = author_id
                    self.author_list.append(Author(id=author_id,name=author,papers_published=[paper]))
                    authorid_list.append(author_id)
                    uniqueid += 1
                else:
                    authorid_list.append(author_id)
                    self.author_list[author_id].add_paper(paper)

            self.paper_to_authorsmap[paper.id] = authorid_list

    def print_hypergraph(self):
        print self.paper_to_authorsmap
