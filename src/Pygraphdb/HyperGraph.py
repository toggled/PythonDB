__author__ = 'Naheed'

from HypergraphRepr import HypergraphRepresentation as repr


class Vertex:
    def __init__(self, id, attribute=[], attr_val_pair=[]):
        assert isinstance(attribute, list)
        assert isinstance(id, int)
        self.attr_val = {}

        if attr_val_pair:
            self.attr_val = dict((key, val) for key, val in attr_val_pair)

        if attribute:
            self.attr_val = dict((key, None) for key in attribute)

        self.id = id

    def add_attribute(self, attribute):
        self.attr_val[attribute] = None

    def set_attributevalues(self, attr_val_pair):
        self.attr_val = dict((key, val) for key, val in attr_val_pair)

    def add_value(self,attribute,val):
        # Assuming that the attribute didn't exist
        self.attr_val[attribute] = val

class HyperEdge:
    def __init__(self, id, vertices, attribute=[], attr_val_pair=[]):
        self.vertices = vertices
        self.attributes = attribute
        self.id = id
        self.attr_val = {}

        if attr_val_pair:
            self.attr_val = dict((key, val) for key, val in attr_val_pair)

        if attribute:
            self.attr_val = dict((key, None) for key in attribute)

    def add_vertex(self, v):
        assert isinstance(v, Vertex)
        self.vertices.append(v)

    def add_vertices(self, vertices):
        assert isinstance(vertices, list)
        self.vertices.extend(vertices)

    def add_attribute(self, attribute):
        self.attr_val[attribute] = None

    def set_attributevalues(self, attr_val_pair):
        self.attr_val = dict((key, val) for key, val in attr_val_pair)


def id_generator():
    new_id = 1
    while True:
        yield new_id
        new_id += 1


class HyperGraph:
    def __init__(self):
        self.repr = repr(structure='adj-list').get_repr()
        self.id_gen = id_generator()

    def create_newvertex(self):
        '''
        Create New Vertex with no attribute or value
        '''
        self.repr.add_newvertex(Vertex(self.id_gen.next(), []))

    def create_newedge(self, list_of_vertices):
        self.repr.add_newedge(HyperEdge(self.id_gen.next(), list_of_vertices, [], []))

    def create_new_attributedvertex(self, attrs):
        '''
        Create New Vertex with only attributes, but no values
        '''
        v = Vertex(self.id_gen.next(), attribute=attrs, attr_val_pair=[])
        self.repr.add_newvertex(v)

    def create_new_attribute_valuedvertex(self, attr_value_tuple):
        '''
        Create New Vertex with both attributes and values
        '''
        v = Vertex(self.id_gen.next(), attribute=[], attr_val_pair=attr_value_tuple)
        self.repr.add_newvertex(v)

    def create_new_attributededge(self, list_of_vertices, attrs):
        e = HyperEdge(self.id_gen.next(), list_of_vertices, attribute=attrs, attr_val_pair=[])
        self.repr.add_newedge(e)

    def create_new_attribute_valuededge(self, list_of_vertices, attr_value_tuple):
        '''
        Create New Vertex with both attributes and values
        '''
        e = HyperEdge(self.id_gen.next(), list_of_vertices, attribute=[], attr_val_pair=attr_value_tuple)
        self.repr.add_newedge(e)

    def traverse(self):
        for obj in self.repr.container:
            if isinstance(obj, Vertex):
                print obj.id, '->', obj.attr_val
            if isinstance(obj, HyperEdge):
                print obj.id, '->', obj.attr_val, ' ==> ', [v.id for v in obj.vertices]
