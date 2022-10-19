word_to_occurrence = {}
text = input("Text: ")
words = text.split()
for word in words:
    frequency = word_to_occurrence.get(word, 0)
    word_to_occurrence[word] = frequency + 1

words = list(word_to_occurrence.keys())

for word in words:
    print(f"{word}: {word_to_occurrence.get(word)}")
