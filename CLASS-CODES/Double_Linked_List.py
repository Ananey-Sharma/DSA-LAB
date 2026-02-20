# Class representing a single node in a Doubly Linked List
class DNode:
    def __init__(self, data):
        self.data = data        # Store the actual data (e.g., website name)
        self.next = None        # Pointer to next node
        self.prev = None        # Pointer to previous node


# Class representing the Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None        # Head pointer (start of list)
    
    # Method to insert a node at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = DNode(data)      # Create new node
        
        if self.head:               # If list is not empty
            new_node.next = self.head   # New node points to current head
            self.head.prev = new_node   # Current head's previous points to new node
        
        self.head = new_node        # Update head to new node
        print(f"✓ Inserted {data} at beginning")  # Confirmation message
    
    # Method to insert a node at the end of the list
    def insert_at_end(self, data):
        new_node = DNode(data)      # Create new node
        
        if not self.head:           # If list is empty
            self.head = new_node    # Make new node the head
            print(f"✓ Inserted {data} as first node")
            return                  # Exit function
        
        current = self.head         # Start from head
        
        # Traverse until the last node
        while current.next:
            current = current.next
        
        current.next = new_node     # Last node points to new node
        new_node.prev = current     # New node's previous points to last node
        print(f"✓ Inserted {data} at end")
    
    # Method to delete a node with given value
    def delete_node(self, key):
        current = self.head         # Start from head
        
        # Traverse to find the node with matching data
        while current and current.data != key:
            current = current.next
        
        if not current:             # If key not found
            print(f"✗ {key} not found!")
            return
        
        # If node to delete is head
        if current == self.head:
            self.head = current.next    # Move head to next node
            if self.head:               # If list is not empty after deletion
                self.head.prev = None   # Remove previous reference
        else:
            if current.next:            # If not last node
                current.next.prev = current.prev   # Link next node to previous
            if current.prev:            # If not first node
                current.prev.next = current.next   # Link previous node to next
        
        print(f"✓ Deleted {key}")      # Confirmation message
    
    # Display list from head to tail
    def display_forward(self):
        if not self.head:              # If list is empty
            print("📊 List is empty")
            return
        
        current = self.head            # Start from head
        elements = []                  # List to store elements
        
        # Traverse forward
        while current:
            elements.append(str(current.data))   # Add data to list
            current = current.next              # Move to next node
        
        # Print formatted output
        print(f"\n📊 Forward: NULL ⇄ {' ⇄ '.join(elements)} ⇄ NULL")
    
    # Display list from tail to head
    def display_backward(self):
        if not self.head:              # If list is empty
            print("📊 List is empty")
            return
        
        current = self.head            # Start from head
        
        # Move to last node (tail)
        while current.next:
            current = current.next
        
        elements = []                  # List to store elements
        
        # Traverse backward using prev pointer
        while current:
            elements.append(str(current.data))
            current = current.prev     # Move to previous node
        
        # Print formatted output
        print(f"📊 Backward: NULL ⇄ {' ⇄ '.join(elements)} ⇄ NULL")
    
    # Visual representation of list structure
    def visualize(self):
        print("\n┌─────────────────────────────────────┐")
        print("│  Doubly Linked List Structure       │")
        print("└─────────────────────────────────────┘")
        
        if not self.head:              # If empty
            print("  NULL")
            return
        
        current = self.head            # Start from head
        print("  NULL", end="")        # Print starting NULL
        
        # Traverse and print nodes visually
        while current:
            print(f" ⇄ [{current.data}]", end="")
            current = current.next
        
        print(" ⇄ NULL\n")            # Print ending NULL


# ================== DEMONSTRATION ==================

print("=" * 50)    # Print separator line
print("  WEB BROWSER HISTORY - DOUBLY LINKED LIST")
print("=" * 50)

browser_history = DoublyLinkedList()   # Create empty doubly linked list

print("\n🌐 Building Browser History:")

# Insert websites at end
browser_history.insert_at_end("google.com")
browser_history.insert_at_end("github.com")
browser_history.insert_at_end("stackoverflow.com")
browser_history.insert_at_end("wikipedia.org")

browser_history.visualize()   # Show structure

print("▶️ Forward Navigation:")
browser_history.display_forward()   # Display forward

print("\n◀️ Backward Navigation:")
browser_history.display_backward()  # Display backward

print("\n📌 Opening new tab:")
browser_history.insert_at_beginning("youtube.com")  # Insert at beginning
browser_history.visualize()

print("❌ Closing a page (github.com):")
browser_history.delete_node("github.com")   # Delete specific node
browser_history.visualize()

print("📌 Visiting new page:")
browser_history.insert_at_end("linkedin.com")  # Insert at end
browser_history.visualize()

# Print time complexity information
print("\n⚡ Performance Characteristics:")
print("  • Access: O(n)")
print("  • Search: O(n)")
print("  • Insert at beginning: O(1)")
print("  • Insert at end: O(n) [O(1) with tail pointer]")
print("  • Delete: O(1) [if node reference available]")
print("  • Bidirectional traversal: Yes")
