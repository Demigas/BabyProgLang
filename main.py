import lexerr
import parserr
import evaluator
import decipher
import time
print("\nHello baby language. \nEnter baby exp and see what you get.")

while True:
    babyExp = input(">>> ")
    if babyExp == "poopoo":
        break
    srcCode = decipher.decipher(babyExp)
    print("interpreted as: ", srcCode)
    tokSeq = lexerr.tokenize(srcCode)
    rootNode = parserr.parse(tokSeq)
    result = evaluator.evaluate(rootNode)
    print("The result is: ", result)

print("Now it is time to go poo poo.")
time.sleep(15)
#print(tokSeq)

 
