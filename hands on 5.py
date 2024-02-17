def parent(i):
    return (i - 1) >> 1

def left(i):
    return (i << 1) + 1

def right(i):
    return (i << 1) + 2

def min_heap(arr):
    n = len(arr)
    for i in range((n >> 1) - 1, -1, -1):
        min_heapify(arr, i, n)

def min_heapify(heap, i, heap_size):
    left_child = left(i)
    right_child = right(i)
    currrent_smallest = i

    if left_child < heap_size and heap[left_child] < heap[currrent_smallest]:
        currrent_smallest = left_child

    if right_child < heap_size and heap[right_child] < heap[currrent_smallest]:
        currrent_smallest = right_child

    if currrent_smallest != i:
        #swap element if necessary
        heap[i], heap[currrent_smallest] = heap[currrent_smallest], heap[i]
        #Recursively min_heapify the affected subtree
        min_heapify(heap, currrent_smallest, heap_size)

def pop_parent(heap):
    if not heap:
        return None
    root = heap[0]
    heap[0] = heap[-1]
    del heap[-1]
    min_heapify(heap, 0, len(heap))
    return root


# Example with integers
int_arr = [6, 12, 5, 8, 2]
min_heap(int_arr)
print("\nMin Heap (int) before popping parent:", int_arr)

popped_integer = pop_parent(int_arr)
print("Popped Parent(int):", popped_integer)
print("Min Heap (int) after popping parent:", int_arr)

# Example with floats
float_arr = [7.5, 12.3, 3.1, 5.8, 1.7]
min_heap(float_arr)
print("\nMin Heap (float) before popping parent:", float_arr)

popped_float = pop_parent(float_arr)
print("Popped Parent (float):", popped_float)
print("Min Heap (float) after popping parent:", float_arr)

# Example with custom data structures (e.g., tuples)
custom_arr = [(7, 'strawberry'), (12, 'apple'), (4, 'blueberry'), (1, 'orange'), (9, 'cherry')]
min_heap(custom_arr)
print("\nMin Heap (custom data) before popping parent:", custom_arr)

popped_custom = pop_parent(custom_arr)
print("Popped Parent (custom data):", popped_custom)
print("Min Heap (custom data) after popping parent:", custom_arr)