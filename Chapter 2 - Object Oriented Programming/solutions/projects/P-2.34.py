#Write a Python program that inputs a document and then outputs a barchart plot of the frequencies of each alphabet 
# character that appears in that document.

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def count_char(c, doc):
    count = 0
    for letter in doc:
        if letter == c:
            count +=1
    return count

alphabets = [chr(97+a) for a in range(26)]
y_pos = np.arange(len(alphabets))
file = open('text.txt', encoding='utf-8')
document = file.read()
frequency = []
for alphabet in alphabets:
    frequency.append(count_char(alphabet,document))

plt.bar(y_pos, frequency, align='center', alpha=0.5)
plt.xticks(y_pos, alphabets)
plt.ylabel('Usage')
plt.title('Programming language usage')

plt.show()