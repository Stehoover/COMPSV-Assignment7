class Patient:
    def __init__(self, name: str, urgency: int):
        self.name = name
        self.urgency = urgency # 1 is most urgent, 10 is least urgent

    def __lt__(self, other):
        """Allows comparison based on urgency for heap operations."""
        return self.urgency < other.urgency

    def __str__(self):
        return f"{self.name} (Urgency: {self.urgency})"



class MinHeap:
    def __init__(self):
        # Index 0 is the most urgent patient
        self.data: list[Patient] = [] 

    def _get_parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def _get_left_child_index(self, index: int) -> int:
        return 2 * index + 1

    def _get_right_child_index(self, index: int) -> int:
        return 2 * index + 2

    def _swap(self, i: int, j: int) -> None:
        """Helper to swap two patients in the heap."""
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _heapify_up(self, index: int) -> None:
        if index == 0:
            return

        parent_index = self._get_parent_index(index)
        # If current element is more urgent (lower urgency score) than its parent
        if self.data[index].urgency < self.data[parent_index].urgency:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index: int) -> None:
        size = len(self.data)
        min_index = index
        left_index = self._get_left_child_index(index)
        right_index = self._get_right_child_index(index)

        # Find the smallest (most urgent) among parent, left, and right
        if left_index < size and self.data[left_index].urgency < self.data[min_index].urgency:
            min_index = left_index
        
        if right_index < size and self.data[right_index].urgency < self.data[min_index].urgency:
            min_index = right_index

        # If the most urgent patient is not the current node, swap and continue heapifying down
        if min_index != index:
            self._swap(index, min_index)
            self._heapify_down(min_index)


    ## Public Methods

    def insert(self, patient: Patient) -> None:
        self.data.append(patient)
        self._heapify_up(len(self.data) - 1)

    def remove_min(self) -> Patient | None:
        if not self.data:
            return None
        
        if len(self.data) == 1:
            return self.data.pop()

        # The root is the min element. Swap it with the last element.
        self._swap(0, len(self.data) - 1)
        min_patient = self.data.pop()
        
        # Restore the heap property
        self._heapify_down(0)
        
        return min_patient

    def peek(self) -> Patient | None:
        if not self.data:
            return None
        return self.data[0]

    def print_heap(self) -> None:
        if not self.data:
            print("The emergency queue is empty.")
            return

        print("\n--- Emergency Queue (Min-Heap Priority) ---")
        for i, patient in enumerate(self.data):
            print(f"Position {i}: {patient}")
        print("------------------------------------------")




# Test your MinHeap class here including edge cases
def test_min_heap():
    """Tests MinHeap functionality, including insertion, remove_min, and peek."""
    print("--- Testing MinHeap Emergency Queue ---")
    heap = MinHeap()

    # Create patients with varying urgency (1 is most urgent)
    p1 = Patient("Alice (High)", 1)
    p2 = Patient("Bob (Medium)", 5)
    p3 = Patient("Charlie (Critical)", 1) # Same urgency as Alice, but inserted later
    p4 = Patient("David (Low)", 8)
    p5 = Patient("Eve (Medium-High)", 3)

    # 1. Test insertion
    print("1. Inserting patients...")
    heap.insert(p2) # Bob (5)
    heap.insert(p4) # David (8)
    heap.insert(p5) # Eve (3)
    heap.insert(p1) # Alice (1) - Should bubble to top
    heap.insert(p3) # Charlie (1) - Should settle near Alice

    # Print the heap to see the internal structure (not necessarily sorted, but min-heap property holds)
    heap.print_heap()
    print("-" * 20)

    # 2. Test peek (should be the most urgent patient)
    print("2. Peeking at the most urgent patient...")
    min_patient = heap.peek()
    assert min_patient.urgency == 1
    print(f"Peeked: {min_patient.name} (Urgency: {min_patient.urgency})")
    print(f"Heap Size: {len(heap.data)}")
    print("-" * 20)

    # 3. Test remove_min (should remove Alice, then Charlie)
    print("3. Removing the most urgent patient (should be Alice or Charlie)...")
    treated_patient = heap.remove_min()
    assert treated_patient.urgency == 1
    
    # Check the next patient
    next_patient = heap.peek() 
    print(f"Next Up: {next_patient}")
    assert next_patient.urgency == 1
    print(f"Heap Size: {len(heap.data)}")
    
    treated_patient = heap.remove_min()
    print(f"Treated (2nd): {treated_patient}")
    assert treated_patient.urgency == 1
    
    # Check the next patient (should now be the urgency 3 patient, Eve)
    next_patient = heap.peek()
    print(f"Next Up: {next_patient}")
    assert next_patient.urgency == 3 # Eve
    print(f"Heap Size: {len(heap.data)}")
    
    # Remove all remaining patients
    heap.remove_min() # Eve (3)
    heap.remove_min() # Bob (5)
    heap.remove_min() # David (8)

    # 4. Test empty heap
    print("-" * 20)
    print("4. Testing empty heap...")
    assert heap.peek() is None
    assert heap.remove_min() is None
    assert len(heap.data) == 0
    print("Queue is empty.")
    
    print("\n✅ MinHeap and Patient tests passed successfully!")
    print("=" * 40)

test_min_heap()