from myTokens import *

class node:
    def __init__(self,value, right=None, left = None):
        self. value = value
        self.right = right 
        self.left = left 



class parser:
    def __init__(self):
        self.tokens=[]
        self.current=0
        self.__symbols={"+":plus,"-":minus,"/":slash,"*":star,"^":power,"(":lParen,")":rParen}

   
    def scanToken(self):
        try:
            # print(self.tokens[self.current])
            return self.tokens[self.current]
        except IndexError:
            return None


    def advance(self):

        self.current +=1

    def printTokens(self):

        for i in self.tokens:
            print(i," ",i.left," ",i.right)
            

    #method to turn string into tokens
    def tokenize(self,expr):
        current=""
        
        index=0

        #loop through expression
        while index < len(expr):

            current= expr[index]

            #if current is number
            if current.isdigit() or current ==".":
                
                #check if there are previous tokens
                if len(self.tokens) >0:

                    ##check if previous token is number
                    if  isinstance(self.tokens[-1], number):
                        prev = self.tokens[-1].value 
                        self.tokens.pop()
                        current = prev + current
                
               
                self.tokens.append(number(current))



            elif current.isalpha():
                self.tokens.append(variable(current))

            elif current in self.__symbols:
                self.tokens.append(self.__symbols[current]())

            
            
            index+=1



    # handles + and -
    # E = T { +|- T}
    def parseExpression(self):
        left = self.parseTerm()

        mid = self.scanToken()
        

    
        while mid is not None and ( mid.value == "+" or mid.value =="-"):

            

            #advance to point at terminal value hopefully
            self.advance()
            right = self.parseTerm()

            mid.setLeft(left)
            mid.setRight(right)


            left = mid

            # self.advance()
            mid = self.scanToken()


            
        
        return left




    
    # handles * and /
    # T = F {*|/ F}
    def parseTerm(self):

        left = self.pasrseFactor()

        mid = self.scanToken()

        
        while mid is not None and mid.value in {"*","/"}:


            #adcanve to point to termincal value hopfully
            self.advance()
            right = self.pasrseFactor()

            mid.setRight(right)
            mid.setLeft(left)

            left = mid

            # self.advance()
            mid = self.scanToken()

        return left
                
        
        
    #handles numbers
    def pasrseFactor(self):
        
        current = self.scanToken()

        if isinstance(current, number):
            self.advance()
            return current

        if isinstance(current,variable):
            self.advance()
            return current

        elif isinstance(current,lParen):

            self.advance()

            a = self.parseExpression()
            # self.current-=1

            if not isinstance(self.scanToken(),rParen):
                return None

            else:
                self.advance()
                return a

                

a = parser()

a.tokenize("5 + 1- 2*(2 + 1) +5 *8")

# a.printTokens()

print(a.parseExpression())

a.printTokens()


