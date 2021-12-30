# Game of Greed 3

## List Comprehension

[List Comprehension](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python)

- Shorthand syntax for iterating a list.  
- filterable

```python

# perform expression on each item of a list: return new list
new_list = [ expression for i in list ]

# populate a list
numbers = [num for num in range(10)]

# Random Numbers
random_numbers = [ randint(1,6) for i in range(10)]

# Even Numbers
# List comprehension with filter
even_nums = [x for x in range(10) if x % 2 == 0]

# String slicing/manipulation
names = ['Toshi', 'Mike', 'Vanessa']
letters = [ name[:3] for name in names]

# Read lines of a file
file = open("dreams.txt", 'r')
poem = [ line for line in file ]

# modify/join 2 lists
modified = [x+y for x in ['Cat', 'hat', 'bat'] for y in ['!', '?', '.']]
```

## Decorators

[Decorators](https://realpython.com/primer-on-python-decorators/)

[JavaScript Decorators - Good Article](https://www.simplethread.com/understanding-js-decorators/)

A syntax for higher order functions.

- *args **kwargs handle arguments passed to the original function

```python

def my_decorator(func):
  def wrapper(*args, **kwargs):
    # do stuff to args or whatever
    fun(*args, **kwargs)
  return wrapper

@my_decorator
def do_stuff(cats):
  return 'Doing things if the decorator lets me'

```

### Return Values from Decorators

- The decorator 'wrapper' function must return a value

```python
def my_decorator(func):
  def wrapper(*args, **kwargs):
    # do stuff in wrapper then return value
    return func(*args, **kwargs)
  return wrapper

@my_decorator
def make_important(word):
  return word + '!!'

```

### Functools

- functools wrapper maintains original properties for a wrapped function.

### Decorating Classes

- Decorators on a class do not modify methods

```python
# Class Decorators: 
# Modifying a Class constructor
def modify_class(cls):
  def wrapper(*args, **kwargs):
    n = cls(*args, **kwargs)
    n.special_new_prop = 'Fluffykins'
    return n
  return wrapper

@modify_class
class Animal:
  def __init__(self, name, type):
    self.name = name
    self.type = type

kitten = Animal('Noni', 'Tiger')

print(kitten.special_new_prop)
# Fluffykins
```

### Muliple Decorators

- stack order

```python
@dec1
@dec2
def do_stuff()

dec1(dec2(do_stuff()))

```
