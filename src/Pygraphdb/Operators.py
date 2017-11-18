__author__ = 'Naheed'

from HyperGraph import HyperGraph, Vertex, HyperEdge


class Select:
    def __init__(self, hg, attribute=None, val=None, ):
        self.attr = attribute
        self.val = val
        self.hypergraph = hg

    def get_vertex(self):
        """
        Call this function when each attribute,value is associated with only one vertex
        """
        for object in self.hypergraph.repr.container:
            if isinstance(object, Vertex):
                if object.attr_val.get(self.attr, None) == self.val:
                    return object
        return None

    def get_vertexbyid(self, id):
        for object in self.hypergraph.repr.container:
            if isinstance(object, Vertex):
                if object.id == id:
                    return object
        return None


class MultiSelect:
    """
    Select Vertices according to attribute,value pairs
    """

    def __init__(self, attr_val_pair_list, hg):
        self.attr_val_pairs = attr_val_pair_list
        self.hypergraph = hg

    def get_vertices(self):
        """
        Call this when each attribute,value pair in the list corresponds to only one vertex.
        """
        vertices = []
        for key, val in self.attr_val_pairs:
            selected_v = Select(self.hypergraph, key, val).get_vertex()
            if selected_v:
                vertices.append(selected_v)

        return vertices
