import collections

def get_code(txt_file, asciiDict):
    for line in txt_file:
        for char in line:
            asciiDict[char] += 1
    asciiDict = {x:y for x,y in asciiDict.items() if y!=0}
    sorted_ascii = sorted(asciiDict.items(), key=lambda kv: kv[1])
    asciiDict = collections.OrderedDict(sorted_ascii)
    return asciiDict

asciiDict = {chr(i): 0 for i in range(32, 127)}
asciiDict['\n'] = 0
txt_file = open("words1ASCII.txt", "r")
code = get_code(txt_file, asciiDict)
print(code)