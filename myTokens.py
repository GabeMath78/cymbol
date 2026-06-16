class token:

    def __init__(self, value):
        self.value = value 
        

    def __str__(self):
        return str(self.value )

   

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
            return str(str(self.c)+self.value+"^"+str(self.p))
        else:
            return str(str(self.c)+self.value)
    

class symbol(token):

    def __init__(self, value):
        super().__init__(value)
        self.left=None
        self.right=None

    def setLeft(self,val):
        self.left=val
    
    def setRight(self,val):
        self.right=val

    def isBothSameVar(self,a,b):
        if isinstance(a,variable) and isinstance(b,variable):
                if a.value == b.value :
                    return True
        return False




class plus(symbol):

    def __init__(self):
        super().__init__("+") 

    def sum(self):
        a = self.left
        b = self.right

        if (not isinstance(a,number) and a is not None) or (not isinstance(b,number) and b is not None):

            if self.isBothSameVar(a,b) and a.p == b.p:
                return variable(a.value,a.c+b.c,a.p)

            return self
            

        if a is None or a.value==0.0 :
            if b is None:
                return number(0.0)
            return b
        
        if b is None or b.value==0.0:
            return a
    
        return number(a.value + b.value)

    

class minus(symbol):

    def __init__(self):
        super().__init__("-") 

    def sum(self):
        a = self.left
        b = self.right

        if (not isinstance(a,number) and a is not None) or (not isinstance(b,number) and b is not None):
            return self
            

        if a is None or a == 0.0:
            if b is None:
                return number(0.0)
            b.value=-b.value
            return b
        
        if b is None or b ==0.0:
            return a
    
        return number(a.value - b.value)




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
            

        if a is None or a ==0.0 or b is None or b ==0.0: 
            return number(0.0)
        
        if a ==1.0 :
            return b

        if b ==1.0:
            return a
    
        return number(a.value * b.value)



class slash(symbol):

    def __init__(self):
        super().__init__("/") 

    def sum(self):
        a = self.left
        b = self.right

        if (not isinstance(a,number) and a is not None) or (not isinstance(b,number) and b is not None):
            return self
            

        if a is None:
            a = number(0.0)
        
        if b is None:
            print("zero division error")
            return None

        if b == 1.0:
            return a
    
        return number(a.value / b.value)

class power(symbol):

    def __init__(self):
        super().__init__("^") 

   

    def sum(self):
        a = self.left
        b = self.right

        if (not isinstance(a,number) and a is not None) or (not isinstance(b,number) and b is not None):
            return self
            

        if a is None or a ==0.0:
            return number(0.0)
        
        if b is None or b == 0.0:
            return number(1.0)

        if b  == 1.0:
            return a
            
    
        return number(a.value ** b.value)



        