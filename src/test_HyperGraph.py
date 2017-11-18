__author__ = 'Naheed'

from Pygraphdb.HyperGraph import HyperGraph
from Pygraphdb.Operators import MultiSelect

vertexadd_str = '''
0:Hoon Hong
1:Dongming Wang
2:Charles J. Brooks
3:Ahmed E. Hassan
4:Parminder Flora
5:Darrel Creacy
6:Carlito Vicencio
7:Neil Daswani
8:Anita Kesavan
9:Shinto Eguchi
10:John Copas
'''
edge_add_str = '''
11:2006:0,1
12:2003:2
13:2007:3,4
14:2005:5,6
15:2006:7,8
16:2006:9,10
'''

v = '''
0:name:Hoon Hong
1:name:Dongming Wang
'''
e = '''
11:year:2006
11:is:0,1
12:year:2003
12:is:2
13:is:3,4
13:year:2007
'''

hdb = HyperGraph()


def get_vertex_avaluetuple(values):
    return ('id', values[0]), ('name', values[1])


def get_edge_avaluetuple(values):
    return ('id', values[0]), ('year', values[1])


def get_list_attributed_vertices(list_of_vertices):
    '''
    Assuming List_of_vertices is comma separated string
    '''
    list_avalue_vertices = []
    for i in list_of_vertices.split(','):
        list_avalue_vertices.append( ('id',int(i)) )
    return list_avalue_vertices


def test_hypergraph_create():
    for query in vertexadd_str.splitlines():
        if query:
            values = query.split(':')
            values[0] = int(values[0])
            hdb.create_new_attribute_valuedvertex(get_vertex_avaluetuple(values))

    # Add hyperedges
    for query in edge_add_str.splitlines():
        if query:
            values = query.split(':')
            values[0] = int(values[0])
            values[1] = int(values[1])
            selected_vertices = MultiSelect(get_list_attributed_vertices(values[2]),hdb).get_vertices()
            hdb.create_new_attribute_valuededge(selected_vertices, get_edge_avaluetuple(values)[:2])
    hdb.traverse()


if __name__ == '__main__':
    test_hypergraph_create()