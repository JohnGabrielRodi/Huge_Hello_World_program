# Master index of hello world program.

class Hello:
    print('Beginning Hello_world program...')
  
  def __init__(self, hello_string, split_up):
      self.hello_string = hello_string
      self.split_up = split_up

  def method(self):
      # repository for odds & ends
      print(self.split_up)

  def print_hw(self):
      ''' simple print method '''
      print(self.hello_string)

  def shuffles(self):
      '''  splits and returns '''
      import random
      bar = self.hello_string.split()
      return bar

  def with_str(self):
      ''' returns after string '''
      print('result:', self.hello_string)

  def multiples(self):
      '''  returns multiples '''
      return self.hello_string * 4

  def comp(self):
      ''' splits and returns through a list comprehension '''
      bar = [x for x in self.hello_string]
      print(bar)


    

obj = Hello('Hello World!', ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!'])
