paragraph = input("Enter a paragraph: ")

words = paragraph.split()

# Count number of words
print("Total number of words:", len(words))

# Word occurrence
count_dict = {}

for word in words:
    word = word.lower()
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1

print("\nWord Occurrences:")
for key in count_dict:
    print(key, ":", count_dict[key])

# Largest word
largest = words[0]

for word in words:
    if len(word) > len(largest):
        largest = word

print("\nLargest word:", largest)

# Reverse of largest word
reverse_word = largest[::-1]
print("Reverse of largest word:", reverse_word)
