import re
def TextScanner(words, letter):
    result = []
    let_ = letter.lower()[0]
    for word in re.split('[\s,.!-?;:\n\t]+',words):
    #words.split(r'\,\.\!'):
        if word is not None and len(word) > 0:
            if word.lower()[0] == let_:
                result.append(word)
    return result

with open("ОжеговСИ.txt", "r", encoding="utf-16" ) as file:
    inp_w = file.read()

letter = input()
res = TextScanner(inp_w, letter)

for line in res:
    print(line)

print(len(res))

