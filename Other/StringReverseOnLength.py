givenString = "THIS IS A INTERVIEW BY ASD ORG"
output = "A BY IS ORG ASD THIS INTERVIEW "

'''
constainst: "  " it will be replace with " "
'''

def reverseStrOnLength(givenStr):
    print("INPUT: ",givenStr)
    givenStr = givenStr.replace("  "," ")
    strStorer = ""
    shoeList = givenStr.split(" ")[::-1]

    NoticeDict = {}
    for i in shoeList:
        if len(i) not in NoticeDict.keys():
            NoticeDict[len(i)] = []
        NoticeDict[len(i)].append(i)

    sorted_list = sorted(NoticeDict.keys())

    strToShow = ""
    for i in sorted_list:
        for i in NoticeDict[i]:
            strToShow += i+" " 
    
    return strToShow

print("OUTPUT: ",reverseStrOnLength(givenString))