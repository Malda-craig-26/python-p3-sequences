#!/usr/bin/env python3
def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return

    sequence = [0, 1]
    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2])
    
    print(sequence)

















#name = "Stella"
#print(name[1])

#class Dog:
   # def __init__(self, name, breed):
       # self.name = name
       # self.breed = breed

    #def bark(self):
       # return "Woof!"

#my_dog = Dog("Buddy", "Golden Retriever")
#print(my_dog.name)  
#print(my_dog.bark())  

# def __init__(self,name,color,age):
       # self.name = name
        #self.color = color
        #self.age = age

   # def announceOwner(self,owner) :
        #print(owner)
        #print(self.name)
        #print(self.color)

        #Daisy = Pet("Daisy","white",1)
        #Daisy.announceOwner("Ike")
        