#type casting 
#it is a proces of converting the data from 1 type to another datattype 

#2 types
#implicit  type casting:
# order ==>> int to float lower ordery o higher  
#explicit 
#float to int reversed to implicit 
#
#list 
# list can be defined in 2 ways 
#list1 = [1,2,3,5,8,9]
#l1 = [1,2,3,5,8,9]
#print(l1[2:4])
#l3 = []
#print(l3 [::2])
#for i in range (1,101):
    #print(l3+[i])
 #   print(l3+[i])

#Creation of SET 
#by using Set constructor And {}
#in set we cant add in it , only we add by using update fxn and only set not a simple int.
#by using Pop Fxn we delete the last elemenet.
#Set doesn't maintain  the order of insertion
#set.pop()
#we can also use set.remove(elemnet) to delete elemenet.

#Dict
#p = {"First Name" : "Prateek" , "Last  Name" :"Chaudhary"}
#p.get('First Name')

# #For loop 
# s = {1,2,3,4,5,6,7,8,9,0}
# for i in s:
#     print (s)

# def cal(a,b):#formal args / variales i.e (a,b)
#     print(a*b)
#     #fun calling 
#     # cal(1,2)   
# def calc(j):
#    return j*j

# l1 = [1,2,3,4,5,6]
# for i in l1:
#  print(i)

# def cal(a,b):
#     return(a,b)

# l1 = [1,2,3]

# s=set()
# for i in l1:
#     res= cal(i,i)
#     s.add(res)
# print(s)
# Global Variable
# x = "70" 

# def myfunc():
#     #global x
#     x = "100"
#     print("L is" + x)

# myfunc()

# print("G is" + x)


# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

#Stack___implimenation___

# list=[]
# list.append(1)
# print("push:",list)
# list.append(2)
# print("push:",list)
# list.append(3) 
# print("push:",list)
# list.pop()
# print("pop:",list)
# print("peek:",list[-1])
# list.pop()
# print("pop:",list)
# print("peek:",list[-1])




class Stack(1,2,5,8):

    def _init_(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def is_full(self):
        return len(self.items) == size

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.items)

print("Peek:", stack.peek())
print("Pop:", stack.pop())

print("Stack after pop:", stack.items)

'''
class Queue:
    def _init_(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from an empty queue")

    def size(self):
        return len(self.items)


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:", queue.items)

print("Peek:", queue.peek())
print("Dequeue:", queue.dequeue())

print("Queue after dequeue:", queue.items)
'''