class token:

    def __init__(self, value):
        self.value = value 
        self.left=None
        self.right=None

    def __str__(self):
        return self.value 

    def setLeft(self,val):
        self.left=val
    
    def setRight(self,val):
        self.right=val

    def eval(self):
        pass


class number(token):

    def __init__(self,value):
        super().__init__(value) 



class plus(token):

    def __init__(self):
        super().__init__("+") 

    def eval(self):
        a = self.left
        b = self.right

        

        return float(self.left) + float(self.right)

class minus(token):

    def __init__(self):
        super().__init__("-") 

    def eval(self):
        return float(self.left) - float(self.right)

class lParen(token):

    def __init__(self):
        super().__init__("(") 

class rParen(token):

    def __init__(self):
        super().__init__(")") 

class star(token):

    def __init__(self):
        super().__init__("*") 

    def eval(self):
        return float(self.left) * float(self.right)

class slash(token):

    def __init__(self):
        super().__init__("/") 

    def eval(self):
        return float(self.left) / float(self.right)

class power(token):

    def __init__(self):
        super().__init__("^") 

    def eval(self):
        return float(self.left) ** float(self.right)


class variable(token):

    def __init__(self, value,c):
        super().__init__(value) 
        self.c=c
        