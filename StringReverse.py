givenString = "The sky is  blue"
output = "blue is sky The"

'''
constainst: "  " it will be replace with " "
'''

def reverseStr(givenStr):
    print("Input: ",givenStr)
    givenStr = givenStr.replace("  "," ")

    strStorer = ""
    shoeList = givenStr.split(" ")[::-1]

    for i in givenStr.split(" ")[::-1]:
        strStorer+= i+" "

    return strStorer

print("Output: ",reverseStr(givenString))