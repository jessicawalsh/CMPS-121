#Lab #6
#Due Date: 09/30/2018, 11:59PM
########################################
#                                      
# Name: Jessica Walsh   
# Collaboration Statement: I completed this lab alone             
#  
########################################

class Vector:
    '''
        Takes a list and creates a Vector object to perform vector operations
        >>> Vector([1,2])+Vector([5])
        'Error - Invalid dimensions'
        >>> Vector([1,2])+Vector([5,2])
        Vector([6, 4])
        >>> Vector([1,2])-Vector([5,2])
        Vector([-4, 0])
        >>> Vector([1,2])*Vector([5,2])
        9
        >>> x=Vector([2,4,6])
        >>> y=Vector([7,8,9])
        >>> x+y
        Vector([9, 12, 15])
        >>> x-y
        Vector([-5, -4, -3])
        >>> x-Vector([1,2])
        'Error - Invalid dimensions'
        >>> x+5
        'Error - Invalid operation'
        >>> x*y
        100
        >>> x*5
        Vector([10, 20, 30])
        >>> 5*x
        Vector([10, 20, 30])
    '''
    def __init__(self, vector):
        self.vector = vector

    #To compare and determine if both Vector objects are equal
    #Include this in your final submission
    def __eq__(self, other):
        return self.vector==other.vector

    # --- Your code starts here
    def __add__(self,other):
        if type(self)!=type(other):
            return 'Error-Invalid Operation'
        elif len(self.vector)!=len(other.vector):
            return 'Error- Invalid Dimensions'
        else:
            added=list(x+y for x,y in zip(self,other))
            return Vector(added)
        
    def __sub__(self,other):
        if type(self)!=type(other):
            return 'Error-Invalid Operation'
        elif len(self.vector)!=len(other.vector):
            return 'Error-Invalid Dimensions'
        else:
            subtracted=list(x-y for x,y in zip(self,other))            
            return Vector(subtracted)

    def __mul__(self,other):
        if type(self)==type(other):
            if len(self.vector)!=len(other.vector):
                return 'Error-Invalid Dimensions'
            else:
                multiplied=list(x*y for x,y in zip(self,other))
                scalar=sum(multiplied)
                return(scalar)
        elif type(other)==int or type(other)==float:
            mul_vec=list(x*other for x in self.vector)
            return Vector(mul_vec)
        
        
    def __rmul__(self,other):
        return self.__mul__(other)               
                        
    def __str__(self):
       return "Vector({})".format(self.vector)

    def __repr__(self):
        return "Vector({})".format(self.vector)

    def __iter__(self):
        return self.vector.__iter__()
    
    def __len__(self):
        return len(self.vector)
    
    def __getitem__(self,key):
        return self.vector[key]   

    #---Your code ends here
