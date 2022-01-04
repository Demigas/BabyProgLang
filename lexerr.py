class token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

def fixUnary():
    unarySeq = []
    unarySeq.append(token("LPAREN", '('))
    unarySeq.append(token("NUMBER", '0'))
    unarySeq.append(token("MINUS", '-'))
    unarySeq.append(token("NUMBER", '1'))
    unarySeq.append(token("RPAREN", ')'))
    unarySeq.append(token("MULTIPLICATION", '*'))
    return unarySeq
    
def tokenize(srcCode):
    tokSeq = []
    while srcCode != "":
        char = srcCode[0]
        if char == "+":
            newToken = token("PLUS", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]
        elif char == "/":
            newToken = token("DIVISION", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]
        elif char == "*":
            newToken = token("MULTIPLICATION", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]
        elif char == "-":
            newToken = token("MINUS", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]
        elif char == "(":
            newToken = token("LPAREN",char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]
        elif char == ")":
            newToken = token("RPAREN",char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]    
        elif char == " ":
            srcCode = srcCode[1:]        
        elif char.isdigit():
            numbStr = ""
            while char.isdigit():
                numbStr += char
                srcCode = srcCode[1:]
                if srcCode == "":
                    char = ""
                else:
                    char = srcCode[0]
            newToken = token("NUMBER", numbStr)
            tokSeq.append(newToken)

    newTokSeq =[]
    for index in range(len(tokSeq)):
        print(tokSeq[index])
        if tokSeq[index].type == "MINUS" and ((tokSeq[index-1].type != "RPAREN" and tokSeq[index-1].type != "NUMBER") or index == 0):
            newTokSeq += fixUnary()
        else:
            newTokSeq.append(tokSeq[index])
    return newTokSeq

   
    
