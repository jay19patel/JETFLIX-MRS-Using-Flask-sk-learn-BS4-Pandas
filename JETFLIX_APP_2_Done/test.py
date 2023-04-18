from collections import Counter




strings =[]
data = db.find({'email':'jay'})
for i in data:
    strings.extend(i['save_genres'])


words = []

for string in strings:
    words.extend(string.split('·'))

word_counts = Counter(words)

sorted_words = []
frequent_words = []
for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
    sorted_words.append((word, count))
    if count >= 5:
        frequent_words.append(word)

print('Frequent words:', frequent_words)
