# Program to find the most repeated character in a string

from pprint import pprint

from django.urls import reverse

sentence = 'This is a common interview question'

char_sent = {}

for char in sentence:
    if char in char_sent:
        char_sent[char] += 1
    else:
        char_sent[char] = 1

pprint(char_sent, width=1)

pprint(sorted(char_sent.items(), key=lambda x: x[1]))

pprint(sorted(char_sent.items(), key=lambda x: x[1], reverse=True))
