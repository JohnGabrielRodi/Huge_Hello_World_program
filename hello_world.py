 # Master index of hello world program.

 class Hello:
 print('Beginning Hello_world program...')
 
 def __init__(self, hello_string):
     self.hello_string = hello_string
  
 def method(self):
      # repository for odds & ends
      pass

 def print_hw(self):
     ''' simple print method '''
     print(self.hello_string)

    
    
obj = Hello('Hello World!')
obj.print_hw()
