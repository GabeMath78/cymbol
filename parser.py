from myTokens import *

class parser:
    def __init__(self):
        self.tokens=[]
        self.__symbols={"+":plus,"-":minus,"/":slash,"*":star,"^":power,"(":lParen,")":rParen}

    #method to turn string into tokens
    def tokenize(self,expr):
        current=""
        
        index=0
        while index < len(expr):

            # if expr[index].isdigit():
            #     current += expr[index]
        
            # else:

            current= expr[index]

            if current.isdigit():

                if len(self.tokens) >0:
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

                

a = parser()

a.tokenize("34 *x + 6 / 8 ^ 2")

for i in a.tokens:
    print(i)

