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
    return self.name == other

  def __enter__(self):
    print('Starting with')

  def __exit__(self, exc_type, exc_val, exc_tb):
    print('Close the with method with error handling arguments')


s = Something('Bob')

print(s.__len__())
print(len(s))
print(s())

print(str(s))
print(repr(s))

print(s == 'Bob')
print(s == 'Frank')

with s:
  print(f'This is happening between enter/exit {s.name}')