# Class representing a Linear List using Python list
class LinearList:
    def __init__(self):
        self.items = []   # Initialize empty list to store elements
    
    # Insert element at given position (or at end if position not given)
    def insert(self, element, position=None):
        if position is None:   # If no position specified
            self.items.append(element)   # Add element at end
            print(f"✓ Inserted {element} at end")
        else:
            self.items.insert(position, element)  # Insert at specific index
            print(f"✓ Inserted {element} at position {position}")
    
    # Delete element from given position
    def delete(self, position):
        # Check if position is valid
        if 0 <= position < len(self.items):
            removed = self.items.pop(position)   # Remove element at position
            print(f"✓ Deleted {removed} from position {position}")
            return removed   # Return deleted element
        
        print("✗ Invalid position!")  # If invalid index
        return None
    
    # Search for an element in the list
    def search(self, element):
        try:
            pos = self.items.index(element)  # Find index of element
            print(f"🔍 Found {element} at position {pos}")
            return pos   # Return index if found
        
        except ValueError:   # If element not found
            print(f"🔍 {element} not found!")
            return -1
    
    # Display all elements in the list
    def display(self):
        print(f"\n📊 Current List: {self.items}")   # Print list
        print(f"📏 Length: {len(self.items)}")      # Print size of list
        return self.items
    
    # Visual ASCII representation of list
    def visualize(self):
        print("\n┌─────────────────────────────────────┐")
        print("│  Visual Representation of List     │")
        print("└─────────────────────────────────────┘")
        
        if not self.items:   # If list is empty
            print("  [Empty List]")
        else:
            # Print each element with index
            for i, item in enumerate(self.items):
                print(f"  Index {i}: [{item}]")
        print()


# ================== DEMONSTRATION ==================

print("=" * 50)
print("  STUDENT GRADE MANAGEMENT SYSTEM")
print("=" * 50)

grades = LinearList()   # Create empty LinearList object

# Adding student grades
print("\n📝 Adding Student Grades:")
grades.insert(85)  # Add first student grade
grades.insert(92)  # Add second student grade
grades.insert(78)  # Add third student grade
grades.insert(95)  # Add fourth student grade
grades.insert(88)  # Add fifth student grade

grades.visualize()   # Display list visually

# Insert new student grade at middle position
print("📌 Inserting new student at position 2:")
grades.insert(90, 2)   # Insert at index 2
grades.visualize()

# Searching operations
print("🔎 Searching Operations:")
grades.search(95)   # Search existing grade
grades.search(100)  # Search non-existing grade

# Delete student record
print("\n🗑️ Deleting student at position 3:")
grades.delete(3)   # Delete element at index 3
grades.visualize()

# Display final list
print("📈 Final Grade List:")
grades.display()

# Performance characteristics
print("\n⚡ Performance Characteristics:")
print("  • Access by index: O(1)")   # Direct indexing
print("  • Search: O(n)")            # Linear search
print("  • Insert at end: O(1)")     # Append operation
print("  • Insert at middle: O(n)")  # Shifting required
print("  • Delete: O(n)")            # Shifting required