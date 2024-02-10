import sys

file_name = input("enter file name: ")

try:
    n = sys.argv[1]
except(Exception):
    print("error")
    sys.exit()

words = {}

def clean_and_split(s):
    s = s.replace(',', ' ')
    return s.lower().split()

with open(file_name, 'r') as f:
    for line in f:
        for word in clean_and_split(line):
            words[word] = words.get(word, 0) + 1
    

for i in range(1, int(n)+1):
    max_key = max(words, key=words.get)
    print("number {} most common word is \"{}\" and it appeared {} times.".format(i, max_key, words[max_key]))
    del words[max_key]