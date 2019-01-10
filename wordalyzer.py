import random

#input
inp = input("").lower()
mode = "default"

stringEnd = len(inp)

if inp[-1] != ".":
    inp += "."

#wordStarts defines the start positions of words within the inp variable
wordStarts = [0]

#wordEnds marks the end positions of words
wordEnds = []
words = []

greetings = ["hello","hey","hi","\'sup"]

for i in range(len(inp)):
    
    if inp[i] == " " or inp[i] == ".":
        
        wordEnd = i - 1
        wordEnds.append(i)
        wordStarts.append(i + 1)

for i in range(len(wordStarts)):
    
    words.append(inp[wordStarts[i-1]:wordEnds[i-1]])

words.remove("")

if(words[0] in greetings):
    mode = "greet"
while True:
    if(mode == "greet"):
        print(random.choice(greetings).title())
        mode = "aftergreet"
