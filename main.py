class Node:
    def __init__(self, leaf_value=None):
        self.children = dict()
        self.leaf_value = leaf_value

    def add_child(self, edge_string):
        self.children[edge_string] = Node()

if __name__ == '__main__':
    #TGGAATTCTCGGGTGCCAAGGAACTCCAGTCACACAGTGATCTCGTATGCCGTCTTCTGCTTG
