# Linked Lists

## Linked Lists

- nodes connected "linked" together.
- Single linked or doubly linked.
- Each node points "links" to the next node in the list.
- Singly linked lists only point to the next node
- Doubly linked point to the previous node and next node.
- Each node contains a property called Next that references the next node.
- Head == first node in a list
- Current == Currently referenced node

- dynamic data structure that does not need continuous memory.

### Traversing a Linked List

- must use the next value for linked list traversal
- NullReferenceException is thrown if a node is null.
- While loop while next node is not null.

### Adding a Node at Head

- Add() method : (O(1)).  To add at the front, replace the current Head with a new node.
- set newNode.Next to the same location as the original Head.
- shift the head to the newly added node.

### Linked List Insertion

Fast for single Head access - Slow for other Node access.

- Inserting to the Head O(1)
- Inserting at Tail O(n)


[Linked Lists - CF](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-05/resources/singly_linked_list.html)

[Linked LIst part1 - medium](https://medium.com/basecs/whats-a-linked-list-anyway-part-1-d8b7e6508b9d)

[LInked List part2 - medium](https://medium.com/basecs/whats-a-linked-list-anyway-part-2-131d96f71996)

#### Units of Measurement

- time in milliseconds (dependant on machine)
- number of operations executed
- number of basic operations executed (operations that contribute the most to total running time).

##### Memory Space

- amount of space needed to hold the algorithm code
- amount of space needed to hold the input data
- the amount of space needed for the output data
- the amount of working space needed.

#### Orders of Growth

- O(1) Constant Time
- O(log n) Logarithmic Growth, grows by log n
- O(n) Linear Growth
- O(n log n) Linearithmic Growth n x log n slightly greater than linear growth
- O(n<sup>2</sup> ) Quadratic Growth ( common in nested growth)
- O(n<sup>3</sup> ) Cubic Growth
- O(2 <sup>n</sup> ) Exponential Growth

#### Best Case, Worst Case, Average Case

- Big O's most common concern is worst case.
- Big Omega notates the best case for an algorithm.
- Big Theta average case.

### Arrays VS Linked Lists

|Array   | Linked List|
|--------|------------|
|indexed access is fast | constant fast insertion/deletions |
|Known data size  | Unknown data size |
|Faster iteration through all elements     | you do not need random access to elements    |
|Memory is a concern, Arrays are smaller    | Allow insertion in the middle of list   |
