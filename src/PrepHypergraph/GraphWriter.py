__author__ = 'Naheed'

class GraphWriter:
    def __init__(self, filename):
        self.filename = filename

    def write_authors(self,authors):
        with open(self.filename,'a') as f:
            for auth_obj in authors:
                print type(str(auth_obj))
                f.write(str(auth_obj))
                f.write('\n')

    def write_papers(self,paper_iterator,paperid_to_authormap):
        with open(self.filename,'a') as f:
            for paper in paper_iterator:
                # print str(paper)
                # f.write(str(paper).encode('utf-8')+':'+','.join([str(id) for id in paperid_to_authormap[paper.id]]))
                # f.write('\n')
                f.write(str(paper)+"\n")

    def write_papers(self, paper_iterator, limit = 30):
        print limit," papers - "
        with open(self.filename, 'a') as f:
            for count,paper in enumerate(paper_iterator):
                # print str(paper)
                # f.write(str(paper).encode('utf-8')+':'+','.join([str(id) for id in paperid_to_authormap[paper.id]]))
                # f.write('\n')
                if(str(paper).strip() == ""):
                    limit+=1
                    continue
                f.write(str(paper) + "\n")
                if(count>limit-2):
                    break
