__author__ = 'Naheed'

from PrepHypergraph import GraphReader
from PrepHypergraph import GraphProcessor
from PrepHypergraph import GraphWriter

if __name__ == "__main__":
    gr = GraphReader.GraphReader('/Users/naheed/PycharmProjects/PythonDB/data/citation-network1.txt')
    paperiterator = gr.read_citationnetwork()

    #Preprocessing: Creating Authorlist and  each-author-paperslist + paperid => each-paper-author-list map
    gr_pro = GraphProcessor.GraphProcessor(paperiterator)
    gr_pro.convert_to_hyperedgelist()
    for i in range(64000,630000,100):
        writefilename = "/Users/naheed/PycharmProjects/PythonDB/data/Hypergraph_citation-net2_limit"+str(i)+".txt"
        gw = GraphWriter.GraphWriter(writefilename)
        gw.write_papers(gr.read_citationnetwork(), limit=i)

    #Write
    #gw.write_authors(gr_pro.author_list)
    #gw.write_papers(gr.read_citationnetwork(), gr_pro.paper_to_authorsmap)
