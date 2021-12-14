# Classes & Objects

## Classes

[Classes & Objects - learn python](https://www.learnpython.org/en/Classes_and_Objects)

```python

class Dragon:
  def __init__(self, name, color):
    self.name = name
    self.color = color
    self.__secret = 'I am a dragon secret'

  def breathe_fire(self):
    print(f'My name is {self.name} and I breath fire!')
  
  def tell_secret(self):
    print(self.__secret)

  @staticmethod
  def staticMethod():
    print("I have no concept of myself.") 

```

## Recursion

[Thinking Recusively - Real python](https://realpython.com/python-thinking-recursively/)

- A recursive function will call itself until a base case is reached.
- State must be either handled in each recursive call or maintained globally.

### Memoization

[LRU Cache](https://realpython.com/lru-cache-python/)
[Memoization](https://towardsdatascience.com/memoization-in-python-57c0a738179a)

- @lru_cache uses a dictionary
- a double linked list with hash table.

```python
from functools import lru_cache

# Store each function call value in a hash table
@lru_cache
def my_function(x):
  pass

# maxsize attribute controls memory limits (16 entries)
@lru_cache(maxsize=16)
def my_function(x):
  pass

print(my_function.cache_info())
# CacheInfo(hits=#, misses=#, maxsize=16, currsize=16)
```

### lru_cache

- hits = number of calls@lru_cache returned from memory
- misses = number of calls not in memory and were computed

## Pytest

[Python test - Linux Journal - Poor article](https://www.linuxjournal.com/content/python-testing-pytest-fixtures-and-coverage)

[fixtures - pytest Documentation](https://docs.pytest.org/en/latest/explanation/fixtures.html)

### Fixtures

- Fixtures are global testing variables that provide information for the testing environment.
- Fixture scope set to 'module' will run only once.

```python
def my_func():
  pass

@pytest.fixture
def fixture_function():
  return my_func(X)

def test_my_func(my_func, fixture_function):
  assert my_func in fixture_function # assert 
```
