#Ryan Valler COMP340-001

def decipher(babyExp):
    srcCode = []
    i = 0
    while i < len(babyExp):
        char = babyExp[i]
        if i <= len(babyExp) - 3 and babyExp[i:i+3] == "pee":
            srcCode.append("+")
            i += 1
        elif i <= len(babyExp) - 3 and babyExp[i:i+3] == "gah":
            srcCode.append("-")
            i += 1
        elif i <= len(babyExp) - 3 and babyExp[i:i+3] == "heh":
            srcCode.append("/")
            i += 1
        elif i <= len(babyExp) - 4 and babyExp[i:i+4] == "mama":
            srcCode.append("(")
            i += 1
        elif i <= len(babyExp) - 4 and babyExp[i:i+4] == "dada":
            srcCode.append(")")
            i += 1
        elif i <= len(babyExp) - 4 and babyExp[i:i+4] == "milk":
            srcCode.append("*")
            i += 1
        elif char == "b":
            count = 0
            i += 1
            while i < len(babyExp) and babyExp[i] == 'a':
                count += 1
                i += 1
            if count == 1:
                if len(srcCode) != 0 and srcCode[len(srcCode)-1].isdigit():
                    srcCode[-1] += "1"
                else:
                    srcCode.append("1")
            elif count == 2:
                if len(srcCode) != 0 and srcCode[len(srcCode)-1].isdigit():
                    srcCode[-1] += "2"
                else:
                    srcCode.append("2")
            elif count == 3:
                if len(srcCode) != 0 and srcCode[len(srcCode)-1].isdigit():
                    srcCode[-1] += "3"
                else:
                    srcCode.append("3")
            elif count == 4:
                if len(srcCode) != 0 and srcCode[len(srcCode)-1].isdigit():
                    srcCode[-1] += "4"
                else:
                    srcCode.append("4")
            elif count == 5:
                if len(srcCode) != 0 and srcCode[len(srcCode)-1].isdigit():
                    srcCode[-1] += "5"
                else:
                    srcCode.append("5")
            elif count == 6:
                if len(srcCode) != 0 and srcCode[len(srcCode)-1].isdigit():
                    srcCode[-1] += "6"
                else:
                    srcCode.append("6")
            elif count == 7:
                if len(srcCode) != 0 and srcCode[len(srcCode)-1].isdigit():
                    srcCode[-1] += "7"
                else:
                    srcCode.append("7")
            elif count == 8:
                if len(srcCode) != 0 and srcCode[len(srcCode)-1].isdigit():
                    srcCode[-1] += "8"
                else:
                    srcCode.append("8")
            elif count == 9:
                if len(srcCode) != 0 and srcCode[len(srcCode)-1].isdigit():
                    srcCode[-1] += "9"
                else:
                    srcCode.append("9")
                srcCode.append("0")
        else:
            i += 1

    return "".join(srcCode)

babyExp = "baaaaagahbabaaahehbaabapeebaabamilkbaaaaaa"
srcCode = ""
print(decipher(babyExp))
