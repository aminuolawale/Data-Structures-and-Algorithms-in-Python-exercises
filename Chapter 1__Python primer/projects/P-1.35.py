#Write a Python program that inputs a list of words, separated by whitespace, and outputs how many times 
# each word appears in the list. You need not worry about efﬁciency at this point, however, as this topic 
# is something that will be addressed later in this book.

words = input('Enter words:\n')
words=words.split(' ')
word_list = set(words)
word_count={}
for word in word_list:
    word_count[word]=words.count(word)

print(word_count)