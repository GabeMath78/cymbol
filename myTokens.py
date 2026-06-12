class token:

    def __init__(self, value):
        self.value = value 
        

    def __str__(self):
        return self.value 

   

    def sum(self):
        return self


class number(token):

    def __init__(self,value):
        super().__init__(value) 

class variable(token):

    def __init__(self, value,c =1,p=1):
        super().__init__(value) 
        self.c=c
        self.p=p

    def __str__(self):
        if self.p!=1:
            return (self.value+"^"+str(self.p))
        else:
            return self.value
    

class symbol(token):

    def __init__(self, value):
        super().__init__(value)
        self.left=None
        self.right=None

    def setLeft(self,val):
        self.left=val
    
    def setRight(self,val):
        self.right=val



class plus(symbol):

    def __init__(self):
        super().__init__("+") 

    def sum(self):
        a = self.left
        b = self.right

        if (not isinstance(a,number) and a is not None) or (not isinstance(b,number) and b is not None):
            return self
            

        if a is None:
            a = number(0)
        
        if b is None:
            b = number(0)
    
        return number(float(a.value) + float(b.value))

    

class minus(symbol):

    def __init__(self):
        super().__init__("-") 

    def sum(self):
        a = self.left
        b = self.right

        if (not isinstance(a,number) and a is not None) or (not isinstance(b,number) and b is not None):
            return self
            

        if a is None:
            a = number(0)
        
        if b is None:
            b = number(0)
    
        return number(float(a.value) - float(b.value))




class lParen(token):

    def __init__(self):
        super().__init__("(") 

class rParen(token):

    def __init__(self):
        super().__init__(")") 



class star(symbol):

    def __init__(self):
        super().__init__("*") 

    def sum(self):
        a = self.left
        b = self.right

        if (not isinstance(a,number) and a is not None) or (not isinstance(b,number) and b is not None):
            return self
            

        if a is None:
            a = number(0)
        
        if b is None:
            b = number(0)
    
        return number(float(a.value) * float(b.value))



class slash(symbol):

    def __init__(self):
        super().__init__("/") 

    def sum(self):
        a = self.left
        b = self.right

        if (not isinstance(a,number) and a is not None) or (not isinstance(b,number) and b is not None):
            return self
            

        if a is None:
            a = number(0)
        
        if b is None:
            print("zero division error")
            return None
    
        return number(float(a.value) / float(b.value))

class power(symbol):

    def __init__(self):
        super().__init__("^") 

   

    def sum(self):
        a = self.left
        b = self.right

        if (not isinstance(a,number) and a is not None) or (not isinstance(b,number) and b is not None):
            return self
            

        if a is None:
            a = number(0)
        
        if b is None:
            b = number(0)
    
        return number(float(a.value) ** float(b.value))



        