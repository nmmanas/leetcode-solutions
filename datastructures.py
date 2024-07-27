class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "List <{}>".format(self.to_list())
    
    def to_list(self):
        if not self:
            return []

        next_value = []
        
        if self.next:
            next_value = self.next.to_list()

        return [self.val] + next_value
    
    def __eq__(self, other):
        return self.to_list()==other.to_list()

    @staticmethod
    def parse_list(data):
        root = None
        previous = None

        for idx, n in enumerate(data):

            list_node = ListNode(n)

            if idx == 0:
                root = list_node
            else:
                previous.next = list_node

            previous = list_node

        return root

    @staticmethod
    def parse_list_of_lists(data):

        results = []

        for d in data:
            results.append(ListNode.parse_list(d))

        return results


class TreeNode():
    def __init__(self, key):
        """
        This Python function initializes a binary tree node with a given key value and sets its left and
        right child nodes to None.
        
        :param key: The `key` parameter in the `__init__` method is used to initialize the key value of
        the node in a binary tree. It represents the value stored in the node
        """
        self.key, self.left, self.right = key, None, None

    def height(self):
        """
        The function calculates the height of a binary tree node by recursively finding the maximum height
        of its left and right subtrees.
        :return: The `height` method is returning the height of a binary tree node. It checks if the node
        is None, and if so, returns 0. Otherwise, it recursively calculates the height of the left and
        right subtrees and returns the maximum height plus 1.
        """
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    def size(self):
        """
        The function calculates the size of a binary tree starting from a given node.
        :return: The `size` method is returning the total number of nodes in the binary tree rooted at
        the current node. It recursively counts the nodes in the left subtree, right subtree, and adds 1
        for the current node.
        """
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        """
        The function `traverse_in_order` recursively traverses a binary tree in-order and returns a list
        of keys.
        :return: The `traverse_in_order` method is recursively traversing a binary tree in in-order
        traversal and returning a list of keys in sorted order. The method first checks if the current
        node is None, in which case it returns an empty list. Otherwise, it recursively calls
        `traverse_in_order` on the left child, then appends the current node's key to the list, and
        finally recursively calls `traverse_in_order` on the right child.
        """
        if self is None:
            return []
        return (TreeNode.traverse_in_order(self.left) +
                [self.key] +
                TreeNode.traverse_in_order(self.right))
    
    def traverse_pre_order(self):
        """
        The function `traverse_pre_order` recursively traverses a binary tree in pre-order and returns a
        list of keys.
        :return: The `traverse_pre_order` method is returning a list of keys in pre-order traversal of a
        binary tree. The keys are being concatenated in the order of root, left subtree, right subtree.
        """
        if self is None:
            return []
        return ([self.key] +  
                TreeNode.traverse_pre_order(self.left) + 
                TreeNode.traverse_pre_order(self.right))
    
    def traverse_post_order(self):
        """
        The function `traverse_post_order` recursively traverses a binary tree in post-order and returns a
        list of keys.
        :return: The `traverse_post_order` method is returning a list of keys in post-order traversal of a
        binary tree. The keys are visited in the order of left subtree, right subtree, and then the current
        node.
        """
        if self is None:
            return []
        return (TreeNode.traverse_post_order(self.left) + 
                TreeNode.traverse_post_order(self.right) + 
                [self.key])

    def display_keys(self, space='\t', level=0):
        """
        This Python function recursively displays the keys of a binary tree in a structured manner.
        
        :param space: The `space` parameter in the `display_keys` method is used to specify the
        indentation space for each level of the binary tree when displaying the keys. It is a string that
        represents the whitespace or tab character used for indentation. By default, the `space` parameter
        is set to the tab character, defaults to \t (optional)
        :param level: The `level` parameter in the `display_keys` method is used to keep track of the
        current level or depth of the node in the binary tree. It is incremented or decremented as the
        method recursively traverses the tree nodes. This parameter helps in formatting the output by
        adding appropriate indentation based on, defaults to 0 (optional)
        :return: The `display_keys` method is a recursive function that prints the keys of a binary tree
        in a specific format. It does not explicitly return any value, as it is a void function. The
        function is designed to print the keys of the binary tree in a specific order and format, rather
        than returning any specific value.
        """
        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return

        # If the node is a leaf
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        # If the node has children
        self.right.display_keys(space, level+1)
        print(space*level + str(self.key))
        self.left.display_keys(space, level+1)

    def to_tuple(self):
        """
        This function converts a binary tree node and its children into a tuple representation.
        :return: The `to_tuple` method is returning a tuple representation of the binary tree nodes. If
        the current node is None, it returns None. If the current node has no left or right children (leaf
        node), it returns the key of the current node. Otherwise, it recursively calls `to_tuple` on the
        left and right children and returns a tuple containing the tuple representation of the left child,
        the current node, and the tuple representation of the right child.
        """
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)

    def __str__(self):
        """
        The `__str__` function in Python returns the representation of the object as a string by calling
        the `__repr__` method.
        :return: The `__str__` method is returning the result of the `__repr__` method. This means that
        the string representation of the object will be the same as the representation returned by the
        `__repr__` method.
        """
        return self.__repr__()

    def __repr__(self):
        """
        The `__repr__` function in Python returns a string representation of a BinaryTree object using its
        `to_tuple` method.
        :return: BinaryTree <(1, (2, None, None), (3, None, None))>
        """
        return "BinaryTree <{}>".format(self.to_tuple())

    @staticmethod
    def parse_tuple(data):
        """
        The `parse_tuple` static method in Python is used to create a binary tree node from a tuple
        representation.
        
        :param data: The `parse_tuple` method is a static method that takes a parameter `data`. This
        method is used to parse a tuple data structure and create a binary tree structure from it. The
        method checks if the `data` is a tuple with a length of 3, and if so, it creates
        :return: The `parse_tuple` method returns a TreeNode object based on the input data. If the input
        data is a tuple with three elements, it creates a TreeNode with the second element as the value
        and recursively creates left and right child nodes based on the first and third elements of the
        tuple. If the input data is not a tuple or does not have three elements, it creates a TreeNode
        with the input data
        """
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node