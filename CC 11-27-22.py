##It's time to create a method to transform the data stored in our NewList objects. We'll be recreating the functionality of the list.append() from the built-in Python list class.

class NewList():
    
    def __init__(self, initial_state):
        self.data = initial_state
        
    def append(self,new_item):
        self.data = self.data + [new_item]
        
my_list = NewList([1,2,3,4,5])

print(my_list.data)

my_list.append(6)

print(my_list.data)