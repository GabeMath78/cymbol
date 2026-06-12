from myTokens import *



class parser:
    def __init__(self):
        self.tokens=[]
        self.current=0
        self.__symbols={"+":plus,"-":minus,"/":slash,"*":star,"^":power,"(":lParen,")":rParen}
        self.head=None

   
    def scanToken(self):
        try:
            # print(self.tokens[self.current])
            return self.tokens[self.current]
        except IndexError:
            return None


    def parse(self,expr):
        self.tokens=[]
        self.current=0

        self.tokenize(expr)

        self.head = self.parseExpression()

        self.printTreeHelper()


    def sum(self):
        self.head = self.sum_help(self.head)
        self.printTreeHelper()


    def sum_help(self,node):

        if node is None:
            return None


            
        if isinstance(node,symbol):
            node.left = self.sum_help(node.left)

            node.right = self.sum_help(node.right)
        
        
        return node.sum()


        

        

    def printTreeHelper(self):
        print()
        self.printTree(self.head)
        print()

    
    def printTree(self, node, prefix="", isLeft=True, isRoot=True):
        if node is None:
            return None

        if isinstance(node,symbol) and node.right is not None:
            self.printTree(node.right,prefix+ ("|   " if isLeft else "   "),False,False)

        if not isRoot:
            print(prefix + ("└── " if isLeft else "┌── ") + str(node.value))
        else:
            print("    "+str(node.value))


        if isinstance(node,symbol) and node.left is not None:
            self.printTree(node.left, prefix + ("    " if isLeft else "|   "), True,False)


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


            #if its a variable
            elif current.isalpha():
                c=1
                #if there is coefficient
                if index != 0 and isinstance(self.tokens[-1],number):
                    c = self.tokens.pop()
                    self.tokens.append(variable(c.value+current,c.value))
                else:
                    self.tokens.append(variable(current))



            elif current in self.__symbols:

                if index !=0 and current == "-" and isinstance(self.tokens[-1],minus):
                    self.tokens.pop()
                    current="+"

                


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

        left = self.parsePower()

        mid = self.scanToken()

        
        while mid is not None and mid.value in {"*","/"}:


            #adcanve to point to termincal value hopfully
            self.advance()
            right = self.parsePower()


            mid.setRight(right)
            mid.setLeft(left)

            

            left = mid

            # self.advance()
            mid = self.scanToken()

        return left

    
    #handles ^
    # P = F {^ F}
    def parsePower(self):
        
        left = self.parseFactor()
        
        mid = self.scanToken()

        while mid is not None and mid.value =="^":
            self.advance()
            right = self.parseFactor()

            if isinstance(left,variable):
                print("in 1")

                if isinstance(right,number):

                    
                    left.p = right.value


                else:
                    print("in 2")
                    left.p = right
                    print(left)
                    
                    

            else:
                mid.setLeft(left)
                mid.setRight(right)

                left = mid 

            mid = self.scanToken()
        return left
        
        
    #handles numbers
    def parseFactor(self):
        
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

# a.tokenize("5 *2^3")

# # a.printTokens()

# print(a.parseExpression())

# a.printTokens()

a.parse("4+5x^(5+2)")
########3x*(5x+5^2)



a.sum()


