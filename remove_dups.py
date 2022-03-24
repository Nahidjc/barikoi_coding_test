
sentence = input()
word_list = sentence.split()
unique_list = []
for word in word_list:
    if word not in unique_list:
        unique_list.append(word)


new_sentence=' '.join(unique_list)
print(new_sentence)