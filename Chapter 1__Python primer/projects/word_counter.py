words = input('Enter words:\n')
words=words.split(' ')
word_list = set(words)
word_count={}
for word in word_list:
    word_count[word]=words.count(word)

print(word_count)