# FileIO & Exceptions

## File Handling 

[Files in Python - Real python](https://realpython.com/read-write-files-python/)

[Read & Write Files - video Real python](https://realpython.com/python-exceptions/)

[Files Quiz - Real python](https://realpython.com/quizzes/read-write-files-python/)

### Line Endings

- Unix / Mac: use LF  \n
- Windows: use CR+LF  \r\n

### Encoding

ASCII - 128 characters
Unicode (UTF-8) => most common, many characters

### Python & Files

file modes
r - read
a - append
w - write (overwrite)
rb - read binary
wb - write binary

```python

# Open and close file
reader = open('./file')

try: 
  # code file stuff here
finally:
  reader.close()

## with

with open('./file_name') as reader:
  # do stuff.  
  # File will close after code executes


```

### file objects

- Text  open with an <'_io.TextIOWrapper'> class
- Buffered binary open returns and <'_io.BufferedReader'> or '_io.BufferedWRiter'
- Raw binary: open returns a '_io.FileIO'

```python
# opening a raw binary file
open('./file_name', 'rb', buffering=0)
```

### Reading Files

- .read(size=-1)  - Read a file based on number of bytes. Whole file by default or -1
- .readline(size=1) - Reads at most size # of characters. If no argument or -1, entire line is read. Works as 'yield'
- .readlines() - Reads the remaining lines in the file object.

#### File iteration

```python
with open('./file_name.txt', 'r') as reader:
  line = reader.readline()
  while line != '': # EOF char
    print(line, end='')
    line = reader.readline()

## OR

with open('./file_name.txt', 'r') as reader:
  for line in reader:
    print(line, end='')

```

### Writing Files

- .write('string') - Write string to file
- writelines(seq) - Write a sequence to a file. No line endings are appended, you must add line endings. 

```python
with open('file.txt', 'r') as reader:
  file_guts = reader.readlines()

with open('file.txt', 'w') as writer:
  for line in file_guts:
    writer.write(line)
```

### File Bytes

```python
with open('file_name.txt', 'rb') as reader:
  print(reader.readline())

```

### Changing Line Endings

dos_text.str.replace('\r\n','\n')

### Append File

```python
with open('file_name.txt', 'a') as a_writer:
  a_writer.write('\nA new line of text')

```

### Context Manager

- \_\_enter\_\_() -> invoked when calling a with statement
- \_\_exit\_\_() -> is called when exiting from a with statement block

```python
class my_file_reader():
  def __init__(self, file_path):
    self.__path = file_path
    self.__file_obj = None

  def __enter__(self):
    self.__file_obj = open(self.path)
    return self
  
  def __exit__(self, type, val, tb):
    self.__file_obj.close()

```

## Exceptions & Try/Except/Else

[Exceptions - Real python](https://realpython.com/python-exceptions/)

- Syntax errors are parsing errors.
- Catch Errors by type
- try/except can be nested

```python
# Raising an Exception
raise  Exception('This is my error message')

# Assertion Error
assert (this statement is false), 'This is my assertion message.'

x = 5
try:
  assert (x > 20), 'Cats!'
except AssertionError as error:
  print('Error Message: ', error)
# 'Error Message: Cats!'


try:
  # something
except:
  # Catch errors
else:
  # run if there are no errors
finally:
  # run this code always 
```
