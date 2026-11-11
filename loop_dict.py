#loop with dict
#we have word banana and we want to count the number of each letter in the word
word = "banana"
count = {}
for letter in word:
    count[letter]=count.get(letter,0)+1
print(count)