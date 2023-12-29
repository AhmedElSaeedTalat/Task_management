class Tree_Node:
    """ tree """
    root = None
    parent = None
    left = None
    right = None

    def __init__(self, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right

    def insert_node(self, node, parent, key):
        """ 
            insert Employee node in tree
            -- if salary in node lt or eq to parent
            -- the node insert to the left, otherwise
            -- to the right
            Args:
                node: node to be Inserted
                parent: parent node
            Return - node inserted at the end of recursion
        """
        if key == 'salary':
            if parent is None:
                return node
                
            if node.salary > parent.salary:
                parent.right =  self.insert_node(node, parent.right, key)
            elif node.salary <= parent.salary:
                parent.left =  self.insert_node(node, parent.left, key)
            return parent
        elif key == 'username':
            if parent is None:
                return node    
            if node.username > parent.username:
                parent.right =  self.insert_node(node, parent.right, key)
            elif node.username <= parent.username:
                parent.left =  self.insert_node(node, parent.left, key)
            return parent


    def create_node(self, obj):
        """ 
            conevrt Object to tree node
            -- Object gets convert to dictionary
            -- dict gets copied to the node
            Args:
                obj: object passed to be converted
            Return - node created
        """
        node = Tree_Node()
        emp_obj = obj.__dict__
        username = obj.user.username
        emp_obj['username'] = username
        for key, value in emp_obj.items():
            setattr(node, key, value)
        node.left = None
        node.right = None
        return node

    def traverse(self, root, sorted_data=[]):
        """ traverse created binary tree """
        if root is None:
            return sorted_data

        self.traverse(root.left, sorted_data)
        sorted_data.append({'salary': root.salary, 'username': root.username})
        self.traverse(root.right, sorted_data)
        return sorted_data

    def search(self, key, parent, value, nodes=[]):
        """ search value in binary tree """
        if key == 'salary':
            if parent is None:
                return nodes
            
            if value <= parent.salary: 
                nodes = self.search(key, parent.left, value, nodes)
            
            if value == parent.salary:
                nodes.append(parent)
                return nodes

            if value > parent.salary:
                nodes = self.search(key, parent.right, value, nodes)
            return nodes

        elif key == 'username':
            if parent is None:
                return nodes
            
            if value <= parent.username: 
                nodes = self.search(key, parent.left, value, nodes)
            
            if value == parent.username:
                nodes.append(parent)
                return nodes

            if value > parent.username:
                nodes = self.search(key, parent.right, value, nodes)
            return nodes