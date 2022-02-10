# Automation

## Regular Expressions

[Python REGEX](https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial)

> r'raw string'

### Re Methods

- re.match(pattern, string)   finds at beginning of string
- re.search(r'pattern', 'string').group()  collects group of pattern matching, searches entire string
- re.findall(pattern, string, flags=0)  finds all matching
- re.finditer(string, [postion, end_postion]) returns regex match objects as an iterator
- re.compile(pattern, flags=0) re.I re.M   creates an RE object
- re.sub(patter, repl, string, count=0, flags=0)  substitute
- re.subn(pattern, repl, string, count=0)  returns number of replacements performed
- re.split(string, [maxsplit = 0]) splits string where pattern matches and returns a list.
- match.start()
- match.end()
- mathc.span()

### Flags  (re.X | re.I)

- I: ignore case
- S: dotall, mach any character
- M: multiline
- X: Verbose

- ^ start of string
- $ end of string
- \w lower case
- \W upper case
- \s singe whitespace, newline, tab, return
- \S not a whitespace
- \d 0-9
- \D not a decimal digit
- \t tab
- \n newline
- \r return
- \A Start of new string
- \Z end of string
- \b beginning or end of word
- \\* preceding 0 or more times
- \\+ preceding one or more times
- ? preceding zero or one times
- {x} x times
- {x,} at least x times
- {x,y} at least x but no more than y

-(?P<name>)  named group

- *? matches as little as possible. non-greedy

```python
import re

re.match(r'[A-Z-!]', Text).group()

matched = re.search(r'(?P<email>)(?P<username>[w\.-]+)@(?P<host>[\w\.-]+)))', text)

matched.group('email')
matched.group('username')
matched.group[2]
```

### shutil module

[python shutil](https://pymotw.com/3/shutil/)

file operations

- shutil.copyfile()
- shutil.copyfileobj(input, output)
- shutil_copymode()   copy permissions
- shutil_copystat() copy
- shutil.copytree('..path', '/new_dir)
- shutil.rmtree(path)
- shutil.move('path', 'new location')
- shutli.which('filename')  # finding files
- shutil.disk_usage('.')

### Automation 

[Browser/desktop automation](https://www.youtube.com/watch?v=dZLyfbSQPXI)

- Selenium: a python browser. Allows easy python browser manipulation.

- PyAutoGUI: GUI Automation

[Automation ideas videa](https://www.youtube.com/watch?v=qbW6FRbaSl0&t=69s)

[watchdog](https://pythonhosted.org/watchdog/)

- Directory monitoring of file system events.
