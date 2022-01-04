#RYAN VALLER COMP340-001

import lexerr
import parserr
def evaluate(rootNode):
    if rootNode.lChild == None and rootNode.rChild == None:
        return int(rootNode.value)
    else:
        result = 0
        leftResult = evaluate(rootNode.lChild)
        rightResult = evaluate(rootNode.rChild)
        if rootNode.type == "PLUS":
            result = leftResult+rightResult
            return result
        elif rootNode.type == "MULTIPLICATION":
            result = leftResult*rightResult
            return result
        elif rootNode.type == "DIVISION":
            result = leftResult / rightResult
            return result
        elif rootNode.type == "MINUS":
            result = leftResult - rightResult
            return result
    
