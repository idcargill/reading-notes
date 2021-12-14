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



Fluffy = Dragon('Fluffykins', 'Green')

Fluffy.tell_secret()