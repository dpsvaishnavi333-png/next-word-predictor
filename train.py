# train.py

with open("data.txt", "r") as file:
    text = file.read().lower()

words = text.split()

# Dictionary to store next-word counts
next_word = {}

for i in range(len(words) - 1):
    current = words[i]
    next_w = words[i + 1]

    if current not in next_word:
        next_word[current] = {}

    if next_w not in next_word[current]:
        next_word[current][next_w] = 1
    else:
        next_word[current][next_w] += 1

print("Training complete!")
print("Learned patterns:")
print(next_word)
