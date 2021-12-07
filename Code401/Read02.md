# Testing and Modules

[In Tests we Trust](https://code.likeagirl.io/in-tests-we-trust-tdd-with-python-af69f47e6932)

- TDD: test driven development
- start with failing tests

## Books

Growing Object-Oriented Software by Steve Freeman, Nat Pryce\
Test Driven Development by Kent Beck

## \_\_main\_\_

[\_\_main\_\_ - geekforgeek](https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/)

A file that is imported will be set to the file name, files run directly as scripts will be set with name == main.

```
# check if code is the main file or being imported
if __name__ == '__main__':
    # code to run when enacted as a script

```

## Recursion

[Recursion - geeksforgeeks](https://www.geeksforgeeks.org/recursion/)

[Recursion - Computerphile](https://www.youtube.com/watch?v=Mv9NEXX1VHc)

Recursion is a process where function calls itself until a base case condition is reached. Without a base case catch, the function will be called infinitely.

### Direct vs Indirect Recursion

```
# direct recursion
def func(n):
  if n < 1:
    return 1
  else:
    return fun(n-1)


# indirect recursion
def func1(n):
  # stuff
  func2(x)

def func2(x):
  # stuff
  func1()

```

- Tail Recursion is when the function call is the last thing executed by the function.

- Recursive functions have larger space and time requirements than other iterative methods.

- Recursion can be clean and succinct code for some problems.


## Modules

[Python Modules - Real python](https://realpython.com/courses/python-modules-packages/)

```
import mod1 
mod1.func()

import func2 from mod1
func2()

if __name__ == '__main__':
  print('I can not be controlled!')

# Packages require __init__.py file for reference

```

[Python Modules Video - Real python](https://realpython.com/python-modules-packages/)

## Lists

[Google - python lists](https://developers.google.com/edu/python/lists)

- Assignments do not make copies.
- is checks for reference
- list + list appends 2 lists
- in checks for value in list
- not in
- for in creates iteration
- range(number)  |  range(start, end)

### List Methods

- list.append(x)  add to end of list
- list.insert(index, x)  insert at index, shift elements right
- list.extend(list2)  adds list2 to end of list. Same as +
- list.index(x)   looks for x and returns first index.
- list.remove(x)  remove first instance of x
- list.sort()  sorts in place, no return. (sorted() preferred)
- list.reverse()  reverses a list in place, no return
- list.pop(index)  removes and returns element at index. Last element by default

```
x = [a, b ,c]
y = x

x is y  # True

# append 2 lists
x + y  # [a, b, c, a, b, c]

# iteration
for i in list:
  print(i)

# in / not in
my_list = ['cat', 'hat']

'fish' in my_list  # False
'cat' in My_list  # True
'bat' not in my_list # True


# While
i = 0

while i < len(my_list):
  print(my_list[i])
  i += 1

```

### List Slicing

- list[start : end]
- list[0:3] = new value replacing 0-3

## Strings

[Google - python strings](https://developers.google.com/edu/python/strings)

- Strings are immutable
- same slicing as lists
- convert to unicode with u'words'

### String Methods

```
s.lower()
s.upper()
s.strip() # removes whitespace from start and end
s.isalpha()
s.isdigit()
s.isspace()
s.find('other string')  # returns first index or -1
s.replace('old', 'new')
s.split('delim')  # returns a list of substring separated by delimiter. returns list
s.join(list)  # opposite of split.  Joins a list into strings


# convert to unicode
ustring = u'words of stuff'

# convert to utf-8
s = ustring.encode('utf-8')
```

## Testing

[Pytest](https://docs.pytest.org/en/latest/)

- file must begin or end with 'test'
- functions must start with 'test': test_method1()
- py.test runs all tests
- py.test file_name

### Run test by substring

- py.test -k method1 -v
- k 'expression' represents substring
- v increases the verbosity

```
import pytest
@pytest.mark.set1
def func():

# ------
# file 2
import pytest
@pytest.mark.set1
def funcsomething():


py.test -m set1
```

[Pytest tutorial](https://www.guru99.com/pytest-tutorial.html)

### pytest mark

- @pytest.mark.name
- test functions in different files
- py.test -m 'name'

### pytest fixture

- @pytest.fixture
- main function to test in conftest.py file

### pytest perametrized

```
import pytest
@pytest.mark.parametrize('input1, input2, output', [(5,5,10), (3,5,12)])
def test_add(input1, input2, output):
  assert input1 + input2 == output, 'failed'

```
  
### pytest Parallel

- update pytest to ^6.0
- poetry add pytest-xdist
- py.test -n 4   (4 workers)

### pytest Xfail  Skip Test

- @pytest.mark.xfail  will not be registered as pass or fail during test output.
- @pytest.mark.skip will skip a test completely.

### XML output

- py.test file -v -junitxml='result.xml'

### framework testing

[Framework test tutorial](https://www.guru99.com/pytest-tutorial.html#14)