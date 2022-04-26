# Pythonisms

[Dunder Methods](https://dbader.org/blog/python-dunder-methods)

### Dunder Methods

- str: informal string representation
- repr: official string representation
- len: length
- getitem: returns an item position as you define
- reversed: iterate in reverse order
- eq / lt: allows for comparison
- add: (self, other) allows access to self and other object to concat
- call: call a custom object output with ()
- enter / exit: protocol methods for using with statements

### Iterators & Generators

[Iterators](https://dbader.org/blog/python-iterators)

- iter and next: dunder methods for looping through an object.



[Generators](https://dbader.org/blog/python-generators)

Utilize the yield statement to return values in order.

```python
def repeat(value):
    while True:
      yield value

```

Yield statements suspend functions and maintain local state.


[Decorators](https://realpython.com/primer-on-python-decorators/)