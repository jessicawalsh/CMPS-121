#Lab #10
#Due Date: 10/26/2018, 11:59PM
########################################
#                                      
# Name: Jessica Walsh
# Collaboration Statement: I completed this assignment alone         
#  
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class Queue:
    '''
        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        'Queue is empty'
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.dequeue()
        1
        >>> print(x)
        Head:Node(2)
        Tail:Node(3)
        Queue:2 3
    '''
    def __init__(self): 
        self.head=None
        self.tail=None

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nQueue:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def isEmpty(self):
        #write your code here
        return self.head==None

    def __len__(self):
        #write your code here
        current=self.head
        count=0
        while current!= None:
            count+=1
            current=current.next
        return count

    def enqueue(self, value):
        #write your code here
        newNode=Node(value)

        if self.isEmpty():
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            newNode.previous=self.tail
            self.tail=newNode     

    def dequeue(self):
        #write your code here
        if self.isEmpty():
            return "Queue is empty"
        else:
            deq_node=self.head.value
            self.head=self.head.next
            return deq_node


