from __future__ import print_function
import nltk
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize
# import random
from random import choice, randint
from nltk.tokenize import WhitespaceTokenizer, sent_tokenize, word_tokenize
from itertools import permutations
import time, os, sys, sched
import repeating, string
from textblob import TextBlob
from textblob import Word
from nltk.stem import WordNetLemmatizer
import helper
from nltk.corpus import wordnet as wn # allows us to access pos types
#help(nltk.corpus.reader)
z = nltk.corpus.gutenberg.fileids()
f = open('artistStatements.txt')
# use the decode method to convert to ascii (textblob prefers ascii)
# raw = sys.stdin.read().decode('ascii', errors="replace")
raw = f.read()
rawShort = raw[:400]
f.close()
artBlob = TextBlob(raw)
shrtBlob = TextBlob(rawShort)
aBLength = len(artBlob)
wList = artBlob.words
posShort = shrtBlob.tags
tags = artBlob.tags
noun_phrases = artBlob.noun_phrases
ccS = shrtBlob.sentences

for i, items in enumerate(posShort):
    print(i, items, items[0], items[1])

adjNounCombo, verbAdverb, aVerb, aPlNoun, adj, gerund, noun, determiner, lngCmbo, my_they_VB_combo = [], [],[], [],[], [], [], [], [], []

def removePunctuation(text):
    text = text.lower()
    exclude = set(string.punctuation)
    keep_these_punct = ['/', '%', '-']
    for punct in keep_these_punct:
        exclude.remove(punct)
    converted_text = ''.join(ch for ch in text if ch not in exclude)
    return converted_text

for i, items in enumerate(tags):
    if items[1] == 'JJ' and tags[i+1][1] == 'NN':
        theCombo = (items[0], tags[i+1][0])
        thisCombo = " ".join(theCombo)
        adjNounCombo.append(thisCombo)
        # print(items[0], tags[i+1][0])
        # print(items, tags[i+1])
# print(adjNounCombo)

for i, items in enumerate(tags):
    if items[1] == 'VBD' and tags[i+1][1] == 'RB':
        theCombo2 = (items[0], tags[i+1][0])
        thisCombo2 = " ".join(theCombo2)
        verbAdverb.append(thisCombo2)
        # print(items[0], tags[i+1][0])
        # print(items, tags[i+1])
# print(verbAdverb)

for i, items in enumerate(tags):
    if items[1] == 'JJ' and tags[i+1] == 'JJ' and tags[i+2] == 'JJ' and tags[i+3] =='CC' and tags[i+4] =='JJ' and tags[i+5]=='NNS':
        myLongCombo = (items[0], tags[i+1][0], tags[i+2][0], tags[i+3][0], tags[i+4][0], tags[i+5][0])
        myLongCombo = " ".join(myLongCombo)
        lngCmbo.append((myLongCombo))

th = ('they' or 'They')
for i, items in enumerate(tags):
    # print("my enumerate is ", items)
    if items[0] == th:
        temp_combo = (items[0], tags[i+1][0], tags[i+1][1])
        my_they_VB_combo.append(temp_combo)
print('my_they_VB ', my_they_VB_combo)

this_string = ' '
new_list, my_i = [], []
for i, items in enumerate(my_they_VB_combo):
    # print(items[2])
    if items[2] == 'VBP':
        this_string = (items[0], items[1])
        new_list.append(this_string)
        # new_list = my_they_VB_combo.append(items)
print(new_list)

for i, items in enumerate(new_list):
    if items[1] == 'are':
        new_list.remove(items)
# print(new_list)

my_list_no_are = [new_list.remove(items) for i, items in enumerate(new_list) if items[1] =='are']
print(new_list)

i_is = 'I'
for i, items in enumerate(tags):
    # print("my enumerate is ", items)
    if items[0] == i_is:
        new_group = (items[0], tags[i+1][0], tags[i+1][1])
        my_i.append(new_group)
# print('my_i ', my_i)
new_i, new_i_no_repeat = [], []
my_i_string = ''

for i, items in enumerate(my_i):
    if items[2] == 'VBP' and items[1] not in ['am', 'use', 'have', 'want', 'turn', 'take', 'see', 'believe', 'make', 'bring', 'try', 'find']:
        my_i_string = items[0] + " "+ items[1]
        new_i.append(my_i_string)

print(new_i)

#don't add an item to the list if it already exists in the list
for i in range(len(new_i)):
    if new_i[i] not in new_i_no_repeat:
        new_i_no_repeat.append(new_i[i])

print("no rep", new_i_no_repeat)

print(lngCmbo)
for i, items in enumerate(tags):
    if items[1] == 'VB':
        aVerb.append(items[0])

for i, items in enumerate(tags):
    if items[1] == 'NNS':
        aPlNoun.append(items[0])

for i, items in enumerate(tags):
    if items[1] == 'JJ':
        adj.append(items[0])

for i, items in enumerate(tags):
    if items[1] == 'NN':
        noun.append(items[0])

for i, items in enumerate(tags):
    if items[1] == 'VBG':
        gerund.append(items[0])

for i, items in enumerate(tags):
    if items[1] == 'DT':
        determiner.append(items[0])



#outputRange
oR = 1
for i in range(oR):
    print(choice(adjNounCombo) +','+ " " +choice(verbAdverb), choice(noun_phrases))
print('\n')
for i in range(oR):
    print(choice(noun_phrases), choice(aVerb), choice(noun_phrases))
print('\n')
for i in range(oR):
    print(choice(aPlNoun), choice(aVerb), choice(noun_phrases))
print('\n')
for i in range(oR):
    print(choice(aPlNoun), choice(aVerb), choice(adj))
print('\n')
for i in range(oR):
    print(choice(aPlNoun), choice(aVerb), choice(adjNounCombo))
#this is a pattern from videogrep
print('\n')
for i in range(oR):
    print(choice(gerund), choice(determiner), choice(adjNounCombo))
print('\n')



count = 0
def rptGerundPat():
    global count
    print(choice(gerund), choice(determiner), choice(adjNounCombo))
    count = count + 1
    # print(count)
    if count > 10:
        r.stop()
    return count

r = repeating.Repeat(2, rptGerundPat)

def rPunct(text):
    return [word.lower() for word in text if word.isalpha()]

w = string
myNewList = []

#the key difference between these is that isalpha will remove the string
def myConversionPunct(text):
    word = text.lower()
    word = word.split()
    for w in word:
        if w.isalpha():
            myNewList.append(w)
            # print(w)
    convert = " ".join(myNewList)
    return(convert)

u = Word("rocks")
w = Word("better")
lemTest = Word("sentences")
myString = "These sentences don't have much of a point, it is mostly an example. 'The thing is', he said, 'We are all doomed.'"
myS = Word(myString)
# myString = myString.lower()
print(rPunct(myString))
print(myConversionPunct(myString))
print(removePunctuation(myString))
print("rocks :", u.lemmatize())
print("better : ", w.lemmatize("a"))
print(myS.lemmatize())
print(lemTest.lemmatize())

mySplitString = myString.split()
tempList = []

for i in mySplitString:
    newLem = Word(i)
    z = newLem.lemmatize()
    print(z)
    tempList.append(z)

print(" ".join(tempList))


