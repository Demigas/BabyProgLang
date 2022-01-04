#RVALLER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Comp 340 - HW6                         #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class treeNode:
    def __init__(self,type,value,precedence):
        self.type = type
        self.value = value
        self.precedence = precedence
    parent = None
    lChild = None
    rChild = None

def getPrecedence(type):
    precedence = 0
    if type == "PLUS" or type == "MINUS":
        precedence = 1
    elif type == "MULTIPLICATION" or type == "DIVISION":
        precedence = 2
    return precedence

def createTreeNodeList(tokSeq):
    x=0
    treeNodeList = []
    newTokSeq = []
    for token in tokSeq:
        if token.type == "LPAREN":
            x+=4
        elif token.type == "RPAREN":
            x-=4
        else:
            newNode = treeNode(token.type,token.value, getPrecedence(token.type)+x)
            treeNodeList.append(newNode)
    return treeNodeList

def parse (tokSeq):
    rootNode = None
    treeNodeList = createTreeNodeList(tokSeq)
    parsing(treeNodeList) #Build edges.
    rootNode = findRoot(treeNodeList)
    return rootNode

def parsing(treeNodeList):
    if len(treeNodeList) <= 1:
        return(treeNodeList)
    dummyNode = treeNode("DUMMY", "",0)
    treeNodeList.insert(0, dummyNode)
    treeNodeList.append(dummyNode)
    x=0
    for index in range(len(treeNodeList)):
        node = treeNodeList[index]
    #print(node.value)
        if node.type == "NUMBER":
            lOp = treeNodeList[index - 1]
            rOp = treeNodeList[index + 1]
            if rOp.precedence > lOp.precedence:
                #Right
                rOp.lChild = node
                node.parent = rOp
                if lOp.type != "DUMMY":
                    lOp.rChild = rOp
                    rOp.parent = lOp
                #print(node.precedence)
            else:
               #left
                lOp.rChild = node
                node.parent = lOp
                #Find
                if rOp.type != "DUMMY":
                    #print(node.type, node.value)
                    while lOp.parent != None:
                        if lOp.parent.precedence < rOp.precedence:
                            break
                        lOp = lOp.parent
                    if lOp.parent != None:
                        lOp.parent.rChild = rOp
                        rOp.parent = lOp.parent
                    rOp.lChild = lOp
                    lOp.parent = rOp
        
def findRoot(treeNodeList):
    rootNode = None
    for node in treeNodeList:
        if node.parent == None and node.type != "DUMMY":
            rootNode = node
            break
    return rootNode

def printTree(rootNode):
    if rootNode.lChild == None and rootNode.rChild == None:
        print(rootNode.value, end = "")
    else:
        print("(", end="")
        printTree(rootNode.lChild)
        print(rootNode.value, end="")
        printTree(rootNode.rChild)
        print(")", end = "")
