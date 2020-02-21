#Lab #8
#Due Date: 10/12/2018, 11:59PM
########################################
#                                      
# Name: Jessica Walsh
# Collaboration Statement: I completed this lab alone            
#  
########################################


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        

                          
class OrderedLinkedList:
    '''
        Creates a linked list in ascending order
        >>> x=OrderedLinkedList()
        >>> x.pop()
        'List is empty'
        >>> x.add(8)
        >>> x.add(7)
        >>> x.add(3)
        >>> x.add(-6)
        >>> print(x)
        Head:Node(-6)
        Tail:Node(8)
        List:-6 3 7 8
        >>> len(x)
        4
        >>> x.pop()
        8
        >>> print(x)
        Head:Node(-6)
        Tail:Node(7)
        List:-6 3 7
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
        return ('Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def add(self, value):
        #write your code here
        newNode=Node(value)
        current=self.head
        previous=None
        stop=False

        while current is not None and not stop:
            if current.value>value:
                stop=True
            else:
                previous=current
                current=current.next
                
        if previous==None:
                newNode.next=self.head
                self.head=newNode
        else:
                newNode.next=current
                previous.next=newNode
                
        if newNode.next is None:
            self.tail=newNode
                
    def pop(self):
        #write your code here
        current=self.head
        end=self.tail

        if current==None:
            return 'List is Empty'

        if current==end:
            self.head=self.tail=None
            return end.value
        
        while current.next is not end:
            current=current.next
            
        current.next=None
        self.tail=current
        return end.value
       

    def isEmpty(self):
        #write your code here
        if self.head==None:
            return True
        else:
            return False
        

    def __len__(self):
        #write your code here
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.next
        return count
