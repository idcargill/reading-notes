# Game of Greed 4

## Dunder Methods

Special "magic" methods

- enable iteration
- operation overloading
- method invocation
- context management

```python
__str__ = official string representation
__repr__ = Informal string representation
__eq__ = equality check
__lt__ = less than
__add__  == add
__call__ == call the object like a function
__enter__ / __exit__ == context manager. allows use of with

```

```python
# Dunder Methods

class Something:
  def __init__(self, name):
    self.name = name

  def __len__(self):
    return 5

  def __call__(self):
    return 'Called the object like a function'

  def __str__(self):
    return 'Official string representation of object'

  def __repr__(self):
    return f'An informal string of whatever I want, oh hi {self.name}.'

  def __eq__(self, other):
    return self.name == other.name

```

### context manager

Resource management, such as releasing a file by closing.

- with operates between enter and exit dunder methods.

```python
# Context managers

__enter__ / __exit__ 

with open('file.txt', 'w') as file:
  file.write('stuff')
# file closed and released back OS

def __enter__(self):
  print('Starting with')

def __exit__(self, exc_type, exc_val, exc_tb):
  print('Close the with method with error handling arguments')

with s:
  print(f'This is happening between enter/exit {s.name}')
```

## Statistics and Probability

- Trial: a sample set of data
- descriptive statistics: mean, standard deviation.
- inferential statistics: a brief rational behind the statistical outcome.
- Probability is the theory of outcome, statistics are the tools to test the theory.
- Normal Distribution: A bell shaped curve centered on the mean. 

### Central Limit Theorem & Three Sigma Rule

- Given a normal distribution, 68% of observations are within 1 standard deviation of the mean, 95% within 2 SD and 99.7% within the 3rd SD.

- Z score determines how many SD a data point is from the mean.

[intro to Statistics](https://www.youtube.com/watch?v=MdHtK7CWpCQ)

[Al Guru](https://www.youtube.com/watch?v=7jmBE4yPrOs)

[Statistics module](https://docs.python.org/3/library/statistics.html)