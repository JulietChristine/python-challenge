import os

file_path = os.path.join("Resources/paragraph_1.txt")
with open(file_path, "r") as txtfile:
    words = ""
    for word in txtfile:
        words = word
words_list = words.split(" ")
sentence_list = word.split(".")
character_count = 0
for word in words_list:
    for letter in word:
        character_count += 1
avg_letter = character_count/len(words_list)
avg_sentence = len(words_list)/len(sentence_list)

print("Paragragh Analysis")
print("-------------------------")
print(f"Approximate Word Count: {len(words_list)}")
print(f"Approximate Sentence Count: {len(sentence_list)}")
print(f"Average Letter Count: {round(avg_letter, 1)}")
print(f"Average Sentence Length: {round(avg_sentence, 1)}" + "\n")

# I had tough time with the new lines,
# so I wasnt able to make a single code that worked on both

file_path = os.path.join("Resources/paragraph_2.txt")
with open(file_path, "r") as txtfile:
    words = ""
    for line in txtfile:
        for word in line:
            words += word
for line in words:
    wordy = words.rstrip("\n\n")
words_list = wordy.split()
sentence_list = words.split("\n\n")

character_count = 0
for word in words_list:
    for letter in word:
        character_count += 1
avg_letter = character_count/len(words_list)
avg_sentence = len(words_list)/len(sentence_list)

print("Paragragh Analysis")
print("-------------------------")
print(f"Approximate Word Count: {len(words_list)}")
print(f"Approximate Sentence Count: {len(sentence_list)}")
print(f"Average Letter Count: {round(avg_letter, 1)}")
print(f"Average Sentence Length: {round(avg_sentence, 1)}" + "\n")