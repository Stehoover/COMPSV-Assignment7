class DoctorNode:
    def __init__(self, name: str):
        self.name = name
        self.left = None  
        self.right = None 

    def __str__(self):
        return f"DoctorNode({self.name})"



class DoctorTree:

    def __init__(self):
        self.root = None 

    def _find_node(self, current_node: DoctorNode, name: str) -> DoctorNode | None:
        if current_node is None:
            return None
        if current_node.name == name:
            return current_node
        
        # Search left and right subtrees
        found = self._find_node(current_node.left, name)
        if found:
            return found
        return self._find_node(current_node.right, name)

    def insert(self, parent_name: str, employee_name: str, side: str) -> bool:
        new_node = DoctorNode(employee_name)

        if self.root is None:
            # Tree is empty. The first insertion sets the root.
            if parent_name == employee_name:
                self.root = new_node
                return True
            return False 

        # Find the parent node
        parent_node = self._find_node(self.root, parent_name)

        if parent_node is None:
            # Parent not found
            return False

        # Parent found, attempt insertion
        if side.lower() == 'left':
            if parent_node.left is None:
                parent_node.left = new_node
                return True
            else:
                # Left side is already occupied
                print(f"Error: Left position under {parent_name} is already occupied by {parent_node.left.name}.")
                return False
        elif side.lower() == 'right':
            if parent_node.right is None:
                parent_node.right = new_node
                return True
            else:
                # Right side is already occupied
                print(f"Error: Right position under {parent_name} is already occupied by {parent_node.right.name}.")
                return False
        else:
            # Invalid side
            print("Error: Side must be 'left' or 'right'.")
            return False

    # Tree Traversal

    def preorder(self, node: DoctorNode | None) -> list[str]:
        result = []
        if node:
            result.append(node.name)
            result.extend(self.preorder(node.left))
            result.extend(self.preorder(node.right))
        return result

    def inorder(self, node: DoctorNode | None) -> list[str]:
        result = []
        if node:
            result.extend(self.inorder(node.left))
            result.append(node.name)
            result.extend(self.inorder(node.right))
        return result

    def postorder(self, node: DoctorNode | None) -> list[str]:
        result = []
        if node:
            result.extend(self.postorder(node.left))
            result.extend(self.postorder(node.right))
            result.append(node.name)
        return result




# Test your DoctorTree and DoctorNode classes here
def test_doctor_tree():
    """Tests DoctorNode and DoctorTree functionality, including insertion and traversals."""
    print("--- Testing DoctorTree ---")
    tree = DoctorTree()

    # 1. Test insertion and root setting
    print("1. Inserting Root Doctor 'Dr. Smith'...")
    assert tree.insert("Dr. Smith", "Dr. Smith", "root")
    print(f"Root: {tree.root.name}")

    # 2. Build the structure
    # Level 1
    assert tree.insert("Dr. Smith", "Dr. Jones", "left")
    assert tree.insert("Dr. Smith", "Dr. Chen", "right")

    # Level 2
    assert tree.insert("Dr. Jones", "Dr. Lee", "left")
    assert tree.insert("Dr. Jones", "Dr. Miller", "right")
    assert tree.insert("Dr. Chen", "Dr. Patel", "left")

    # Level 3 (Incomplete structure)
    assert tree.insert("Dr. Lee", "Dr. Kim", "left")

    # Test case: Failure to insert where a spot is taken
    print("Attempting invalid insertion (right of Dr. Jones)...")
    assert not tree.insert("Dr. Jones", "Dr. Adams", "right")
    print("-" * 20)

    # 3. Test Traversal
    print("2. Testing Traversal Orders:")
    root = tree.root

    # Preorder: Root, Left, Right
    preorder_list = tree.preorder(root)
    expected_preorder = ['Dr. Smith', 'Dr. Jones', 'Dr. Lee', 'Dr. Kim', 'Dr. Miller', 'Dr. Chen', 'Dr. Patel']
    print(f"Preorder (Root, Left, Right): {preorder_list}")
    assert preorder_list == expected_preorder

    # Inorder: Left, Root, Right
    inorder_list = tree.inorder(root)
    expected_inorder = ['Dr. Kim', 'Dr. Lee', 'Dr. Jones', 'Dr. Miller', 'Dr. Smith', 'Dr. Patel', 'Dr. Chen']
    print(f"Inorder (Left, Root, Right):   {inorder_list}")
    assert inorder_list == expected_inorder

    # Postorder: Left, Right, Root
    postorder_list = tree.postorder(root)
    expected_postorder = ['Dr. Kim', 'Dr. Lee', 'Dr. Miller', 'Dr. Jones', 'Dr. Patel', 'Dr. Chen', 'Dr. Smith']
    print(f"Postorder (Left, Right, Root): {postorder_list}")
    assert postorder_list == expected_postorder

    print("\n DoctorTree and Traversal tests passed successfully!")
    print("=" * 40)

# Run the test
test_doctor_tree()
