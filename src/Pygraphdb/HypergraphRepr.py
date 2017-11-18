__author__ = 'Naheed'

MAIN_MEM_SIZE = 1000


class RDFTripple:
    def __init__(self, triple=(None, None, None)):
        self.data = triple


class HypergraphRepresentation:
    def __init__(self, structure):
        self.repr = structure
        self.storage = 'storage.hgdb'
        self.storagehandle = open(self.storage, 'a+')

    def get_repr(self):
        if self.repr == 'adj-list':  # Flat List
            return ListRepr('adj-List')

    def add_newvertex(self, v):
        # assert isinstance(v,Vertex)
        pass

    def add_newedge(self, e):
        # assert isinstance(e,HyperEdge)
        pass


class ListRepr(HypergraphRepresentation):
    def __init__(self, structure):
        HypergraphRepresentation.__init__(self, structure)
        self.container = [] * MAIN_MEM_SIZE

    def add_newvertex(self, v):
        self.container.append(v)
        store = (str(v.id) + ":is:" + str(v.id) + "\n")
        for attr, val in v.attr_val.items():
            store += (str(v.id) + ":" + str(attr) + ":" + str(val) + '\n')
        self.storagehandle.writelines(store)

    def add_newedge(self, e):
        self.container.append(e)
        store = ""
        store = str(e.id) + ":is:" + ",".join([str(x.id) for x in e.vertices]) + "\n"
        for attr, val in e.attr_val.items():
            store += (str(e.id) + ":" + str(attr) + ":" + str(val) + '\n')
        self.storagehandle.writelines(store)
