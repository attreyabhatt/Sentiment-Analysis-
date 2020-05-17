from collections import Counter
from string import punctuation
import matplotlib.pyplot as plt

# reading text file
text = open("read.txt", encoding="utf-8").read()

# converting to lowercase
lower_case = text.lower()

# Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', punctuation))

# splitting text into words
tokenized_words = cleaned_text.split()

# get all stop words from the file
stop_words = open("stop_words.txt", encoding="utf-8").read().split()

# Removing stop words from the tokenized words list
final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

# NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotion.txt
#  - open the emotion file
#  - Loop through each line and clear it
#  - Extract the word and emotion using split

# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list

emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        for f_word in final_words:
            if f_word == word:
                emotion_list.append(emotion.strip())

print(emotion_list)
emo_counter = Counter(emotion_list)
print(emo_counter)

fig, ax = plt.subplots()
ax.bar(emo_counter.keys(), emo_counter.values())
fig.autofmt_xdate()
plt.savefig("emo.png")
plt.show()
