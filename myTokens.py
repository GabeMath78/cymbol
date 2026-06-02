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

class number(token):

    def __init__(self,value):
        super().__init__(value) 

class float(token):

    def __init__(self,value):
        super().__init__(value)

class plus(token):

    def __init__(self):
        super().__init__("+") 

class minus(token):

    def __init__(self):
        super().__init__("-") 

class lParen(token):

    def __init__(self):
        super().__init__("(") 

class rParen(token):

    def __init__(self):
        super().__init__(")") 

class star(token):

    def __init__(self):
        super().__init__("*") 

class slash(token):

    def __init__(self):
        super().__init__("/") 

class power(token):

    def __init__(self):
        super().__init__("^") 


class variable(token):

    def __init__(self, value):
        super().__init__(value) 