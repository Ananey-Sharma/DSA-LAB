# Class representing a single node in a Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data      # Store actual data (e.g., song name)
        self.next = None      # Pointer to next node (initially None)


# Class representing the Singly Linked List
class SinglyLinkedList:
    def __init__(self):
        self.head = None      # Head pointer (start of the list)
    
    # Insert a node at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)     # Create a new node
        new_node.next = self.head # Point new node to current head
        self.head = new_node      # Update head to new node
        print(f"✓ Inserted {data} at beginning")
    
    # Insert a node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)     # Create a new node
        
        if not self.head:         # If list is empty
            self.head = new_node  # Make new node the head
            print(f"✓ Inserted {data} as first node")
            return
        
        current = self.head       # Start from head
        
        # Traverse until the last node
        while current.next:
            current = current.next
        
        current.next = new_node   # Link last node to new node
        print(f"✓ Inserted {data} at end")
    
    # Insert a node after a specific value
    def insert_after(self, prev_data, data):
        current = self.head       # Start from head
        
        # Search for node with value prev_data
        while current and current.data != prev_data:
            current = current.next
        
        if current:               # If node is found
            new_node = Node(data)     # Create new node
            new_node.next = current.next  # Link new node to next node
            current.next = new_node       # Link previous node to new node
            print(f"✓ Inserted {data} after {prev_data}")
        else:
            print(f"✗ {prev_data} not found!")
    
    # Delete a node with given key
    def delete_node(self, key):
        current = self.head       # Start from head
        
        # If head node needs to be deleted
        if current and current.data == key:
            self.head = current.next   # Move head to next node
            print(f"✓ Deleted {key}")
            return
        
        prev = None               # Previous pointer
        
        # Search for node to delete
        while current and current.data != key:
            prev = current        # Store previous node
            current = current.next
        
        if current:               # If node found
            prev.next = current.next   # Bypass current node
            print(f"✓ Deleted {key}")
        else:
            print(f"✗ {key} not found!")
    
    # Search for a node
    def search(self, key):
        current = self.head       # Start from head
        position = 0              # Position counter
        
        # Traverse the list
        while current:
            if current.data == key:   # If key found
                print(f"🔍 Found {key} at position {position}")
                return position      # Return position
            
            current = current.next   # Move to next node
            position += 1            # Increase position
        
        print(f"🔍 {key} not found!")
        return -1                    # Return -1 if not found
    
    # Display the linked list
    def display(self):
        if not self.head:            # If list is empty
            print("📊 List is empty")
            return
        
        current = self.head          # Start from head
        elements = []                # List to store elements
        
        # Traverse and collect elements
        while current:
            elements.append(str(current.data))
            current = current.next
        
        # Print formatted output
        print(f"\n📊 Linked List: {' → '.join(elements)} → NULL")
    
    # Visual ASCII representation of the list
    def visualize(self):
        print("\n┌─────────────────────────────────────┐")
        print("│  Singly Linked List Structure       │")
        print("└─────────────────────────────────────┘")
        
        if not self.head:            # If empty
            print("  HEAD → NULL")
            return
        
        current = self.head          # Start from head
        print("  HEAD", end="")
        
        # Print each node visually
        while current:
            print(f" → [{current.data}]", end="")
            current = current.next
        
        print(" → NULL\n")
    
    # Reverse the linked list
    def reverse(self):
        prev = None              # Previous pointer
        current = self.head      # Start from head
        
        # Traverse the list
        while current:
            next_node = current.next  # Store next node
            current.next = prev       # Reverse link
            prev = current            # Move prev forward
            current = next_node       # Move current forward
        
        self.head = prev              # Update head after reversal
        print("🔄 List reversed!")


# ================== DEMONSTRATION ==================

print("=" * 50)
print("  MUSIC PLAYLIST - SINGLY LINKED LIST")
print("=" * 50)

playlist = SinglyLinkedList()   # Create empty linked list

print("\n🎵 Building Playlist:")

# Insert songs at end
playlist.insert_at_end("Song A: Bohemian Rhapsody")
playlist.insert_at_end("Song B: Stairway to Heaven")
playlist.insert_at_end("Song C: Hotel California")
playlist.insert_at_end("Song D: Imagine")

playlist.visualize()   # Show structure

print("📌 Adding new song at beginning:")
playlist.insert_at_beginning("Song Z: Sweet Child O' Mine")
playlist.visualize()

print("📌 Adding song after 'Song B':")
playlist.insert_after("Song B: Stairway to Heaven", "Song X: Wish You Were Here")
playlist.visualize()

print("🔎 Searching for a song:")
playlist.search("Song C: Hotel California")
playlist.search("Song Y: Unknown")

print("\n🗑️ Removing a song:")
playlist.delete_node("Song X: Wish You Were Here")
playlist.visualize()

print("🔄 Reversing playlist order:")
playlist.reverse()
playlist.visualize()

print("\n⚡ Performance Characteristics:")
print("  • Access: O(n)")
print("  • Search: O(n)")
print("  • Insert at beginning: O(1)")
print("  • Insert at end: O(n)")
print("  • Delete: O(n)")