
from pathlib import Path

text = Path('data.txt').read_text()
text = text.replace('\n','')
len_text = len(text)

letters = []
only_letters = []
for letter in text:
    if letter not in letters:
        freq = text.count(letter)
        letters.append(freq)
        letters.append(letter)
        only_letters.append(letter)

nodes = []
while len(letters) > 0:
    nodes.append(letters[0:2])
    letters = letters[2:]

nodes.sort()
huffman_tree = []
huffman_tree.append(nodes)


def combine(nodes):
    pos = 0
    newnode = []
    if len(nodes) > 1:
        nodes.sort()
        nodes[pos].append("0")
        nodes[pos + 1].append("1")
        combined_node1 = (nodes[pos][0] + nodes[pos + 1][0])
        combined_node2 = (nodes[pos][1] + nodes[pos + 1][1])
        newnode.append(combined_node1)
        newnode.append(combined_node2)
        newnodes = []
        newnodes.append(newnode)
        newnodes = newnodes + nodes[2:]
        nodes = newnodes
        huffman_tree.append(nodes)
        combine(nodes)
    return huffman_tree


newnodes = combine(nodes)
huffman_tree.sort(reverse=True)

checklist = []
for level in huffman_tree:
    for node in level:
        if node not in checklist:
            checklist.append(node)
        else:
            level.remove(node)


letter_binary = []
if len(only_letters) == 1:
    letter_code = [only_letters[0], "0"]
    letter_binary.append(letter_code * len(text))
else:
    for letter in only_letters:
        lettercode = ""
        for node in checklist:
            if len(node) > 2 and letter in node[1]:
                lettercode = lettercode + node[2]
        letter_code = [letter,lettercode]
        letter_binary.append(letter_code)

print("Kody liter to : ")
for letter in letter_binary:
    print(letter[0], letter[1])


bitstring = ""
for character in text:
    for item in letter_binary:
        if character in item:
            bitstring = bitstring + item[1]

binary = bin(int(bitstring,base = 2))

uncompressedFileSize = len(text)*7
compressedFileSize = len(binary)-2

print()
print("Twoj orginalny plik mial ", uncompressedFileSize," bitow")
print("Twoj skompresowany plik ma ", compressedFileSize," bitow")
print()
print("Skompresowany tekst to : ")
print(binary)

with open("writeFile.txt","w") as writeFile:
    writeFile.write(binary)

compressedFile = Path('writeFile.txt').read_text()
compressedFile= compressedFile.replace('\n','')

bitsttring = str(compressedFile[2:])
uncompressedString = ""
code = ""
for digit in bitsttring:
    code = code+digit
    pos = 0
    for letter in letter_binary:
        if code == letter[1]:
            uncompressedString = uncompressedString + letter_binary[pos][0]
            code=""
        pos +=1

print()
print("Twoj odkompresowany tekst to :")
print(uncompressedString)