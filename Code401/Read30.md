# Hash Tables

## Hash Table

- hash functions should be simple.
- hash values can be stored as an array of arrays for chaining same hash values.
- builtin ord() will return unicode number for a character.
- ensure collisions are handled for duplicate hash values. (append into a list for matching hashes)

Hash tables are used for near constant time access.

### Native Hash Tables

- javasScript: everything, literally everything
- python: dictionary
- java: hash maps and hash sets

### overwrite built ins for bracket notation

Edit the getter and setter dunder methods to use bracket notation on a class.

```python

# set item with brackets 
def __setitem__(self, key, value)
  code to set an item at key

# get item with brackest
def __getitem__(self, key):
  code to get value by key
```

> h = HashTable()

> h['fish'] = 10

#### Hash Table Array

Data is stored in a list of lists.
Duplicate hash keys get added to the initial hash list.

#### Adding a value

- check if the hash has a collision
- check if the value already exists in the array[h]
- handle collision if needed by  appending the key,value tuple onto the array.

Here 'dog' and 'god' hash to the same value and must be appended into the same list, located the initial hash location.

```python
[[('salmon', 1000)], [], [], [], [('dog', 20), ('god', 300)], [], [('fish', 10)], [], [], []]


```

### base Structure

```python
# Base hash map with memory size container and storage array 
class HashMap:
  def __init__(self):
    self.MaxSize=10
    self.array = [ [] for i in range(self.MaxSize)]

  def hash(self, key):
    total = 0
    for i in key:
      total += ord(i)
    return total % self.MAX

```

[Hash Tables:codebasics](https://www.youtube.com/watch?v=ea8BRGxGmlA)