# Game of Greed 2

## Scope

- LEGB: Local, Enclosing, Global, Built-in scopes

- global: available to all code in a module
- Local: available within a block or function of code

- Python scopes are dictionaries called namespaces \_\_dict\_\_

- built in python objects live in the builtins scope.

```python
import sys

sys.__dict__.keys()  # keys of namespace


```

## Big O Notaion

[Video of Big O - nothing new](https://www.youtube.com/watch?v=5Uqawfl0VHQ)

Logarithmic complexity scales linearly in relation to input.

[Art of Problem Solving ](https://artofproblemsolving.com/wiki/index.php/Basic_Programming_With_Python#Program_Example_1_3)