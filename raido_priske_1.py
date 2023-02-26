#https://leetcode.com/problems/reverse-string/description/

#Võtan kasutajalt sisendi
word = input("Sisesta sõna, mida ümber põõrata\n")

#Teen sisendist array
i = 0
wordArray = []
while i < len(word):
    wordArray.append(word[i])
    i += 1

#Pööran array
i = 0
finalArray = []
while i < len(wordArray):
    finalArray.append(wordArray[len(wordArray) - (i + 1)])
    i += 1

print(finalArray)