# Q1. Count contents in a file
# a. Count each letter frequency
# b. Count words
# c. Count occurrences of a specific word
# d. Find longest word

import re

filename = input("Enter file name: ")

with open(filename, "r") as file:
    content = file.read()

# a. Letter frequency
frequency = {}

for char in content.lower():
    if char.isalpha():
        frequency[char] = frequency.get(char, 0) + 1

print("\nLetter Frequency:")
for letter in sorted(frequency):
    print(letter, ":", frequency[letter])

# b. Count words
words = re.findall(r"\b\w+\b", content)
print("\nTotal number of words:", len(words))

# c. Occurrences of specific word
search_word = input("\nEnter word to search: ")
count = sum(1 for word in words if word.lower() == search_word.lower())
print("Occurrences of", search_word, ":", count)

# d. Longest word
if words:
    longest_word = max(words, key=len)
    print("\nLongest word:", longest_word)
    print("Length:", len(longest_word))
else:
    print("\nFile is empty.")
