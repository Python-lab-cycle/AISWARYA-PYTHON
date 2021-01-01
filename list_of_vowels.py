word = input("Enter a word: ")
for letter in word:
    if letter in 'aeiou':
        print(letter, end="")

# word = input("Enter a word: ")
# vowels = [i for i in word if i in 'aeiou']
# print(vowels)