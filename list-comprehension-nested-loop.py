import itertools
import random

#A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
#list comprehension example
squares = [x**2 for x in range(10)]
print(squares)

# joined_words = [' '.join(e) for w in range(len(two_word_combos) )]

s1 = 'abc'
s2 = 'def'

for j in s1:
    for k in s2:
        print(j, k)

new_strings = [j + k for j in s1 for k in s2]
print(new_strings)

l1 = ["zero","one","two","three"]
l2 = ["four", "five","six", "seven"]

jj_nn = ['social engagement', 'institutional critique', 'activist art', 'urban life', 'everyday life', 'rigorous absurdity', 'traditional design', 'public space', 'artificial intelligence', 'biometric sensing', 'personal narrative',\
         'radical personhood', 'digital technology', 'digital art', 'systematic violence', 'feminist discourse', 'prosumer technology', 'contemporary life', 'further dialog', 'sublte manipulation', 'theoretical research', 'whole imagery', \
         'multi-channel video', 'multi-channel audio', 'hand-drawn rotoscoping', 'sound installation', 'cultural hybridity', 'popular culture', 'lush visuality', 'visual music', 'emotional expression', 'archival material', 'capitalist production','non-repesentational drawing', 'feminist art']

conjunctions = ['and this artists work focuses on', 'and of course their famous work in', 'an interdisciplinary practice grounded in']

they_verb =[('they', 'strive'), ('they', 'conjure'), ('they', 'choose'), ('they', 'arise'), ('they', 'occupy'), ('they', 'reside'), ('they', 'speak'), ('they', 'start'), ('they', 'work'), ('they', 'produce'), ('they', 'bridge'), ('they', 'are'), ('they', 'have'), ('they', 'morph'), ('they', 'perceive')]
they_verb_combo = []
I_verb = ['I create', 'I imagine', 'I build', 'I ask', 'I hope', 'I explore', 'I employ', 'I construct', 'I animate', 'I leverage', 'I excavate', 'I immerse', 'I seek', 'I collaborate', 'I write', 'I integrate', 'I manipulate', 'I foreground', 'I choose', 'I examine', 'I aim', 'I present', 'I utilize', 'I re-articulate', 'I layer', 'I address', 'I question', 'I combine', 'I work', 'I attempt', 'I like', 'I collect', 'I bundle', 'I mimic', 'I prioritize', 'I reflect', 'I borrow', 'I interrogate', 'I refuse', 'I consider', 'I draw', 'I intend', 'I look', 'I document', 'I investigate', 'I strive', 'I search', 'I alter', 'I author', 'I incorporate', 'I photograph', 'I remain', 'I treat', 'I populate', 'I accomplish']


seperator = ''
def converttostr(input_seq, seperator):
   # Join all the strings in list
   final_str = seperator.join(input_seq)
   return final_str


for i in range(len(they_verb)):
    new_str = they_verb[i][0] + " " +they_verb[i][1]
    print(new_str)
    they_verb_combo.append(new_str)
print(they_verb_combo)

for i in range(len(l1)):
    for j in range(len(l2)):
        print(l1[i] + ' '+l2[j])
print('\n')

for i in range(len(l1)):
    for j in range (len(l1)):
        if l1[i] is not l1[j]:
            print(l1[i] +" "+l1[j])

#a version that would remove any combo that included the same items in a different order
# new_combos = []
# for i in range(len(l1)):
#     for j in range (len(l1)):
#         if l1[i] is not l1[j]:
#             new_combos.append(l1[i]+" "+ l1[j])

# print(new_combos)

#updated version of code above
new_combos = []
for i in range(len(jj_nn)):
    # print("i is ", i)
    for j in jj_nn[i:]:
        # print("j is ", j)
        # print("jj_nn[i] is ", jj_nn[i])
        if jj_nn[i] != j:
            new_combos.append(jj_nn[i].split(' ')[random.randint(0,1)]+" "+ j.split(' ')[random.randint(0,1)])
            #this is taking a random choice for the first slot

print(new_combos)

new_combos2 = []
for i in range(len(l1)-1):
    print("i is ", i)
    for j in l1[i:]:
        print("j is ", j)
        print("l1[i] is ", l1[i])
        if l1[i] != j:
            new_combos.append(jj_nn[i].split(' ')[random.randint(0,1)]+" "+ j.split(' ')[random.randint(0,1)])
            # new_combos.append(l1[i].split(' ')[0] + " " + j.split(' ')[1])
            # new_combos.append(l1[i])
            #how would you make a nonrandom version?

x = random.randint(0,1)
y = random.randint(0,1)
z = random.randint(0,1)
print("random number prints ", x, y, z)


#tried to get the removal of inverse duplicates, but couldn't figure it out
new = []
for i in range(len(new_combos)):
    new = new_combos[i].split()
    for j in new:
        if new[1] ==new[0] and new[0]==new[1]:
            print('match')
            # print(new[1])
        # print(new[0] +" "+ new[1])

            # new.remove(new[1][0])

print(new)









#see updated program



#
#
# def combine(num, words):
#     final = [] #a list called final is created within the function, this variable is returned when the funciton is completed
#     if num > 0 and len(words) >= num:
#         print ('num: ', num)
#         if num == 1:
#             final = final + [[words[0]]]
#             print ('final in if statement', final)
#         else:
#             final = final + [[words[0]] +
#                     c for c in combine(num - 1, words[1:])]
#             print('final in else statement', final)
#         final = final + combine(num, words[1:])
#     return final
#

#
# print('\n', 'the recursive one starts here')
# s=' '
#
# def combinations(s, l):
#     if l == 0:
#         print(s)
#     else:
#         combinations(s+s1[len(s1)-l], l-1)
#         combinations(s+s2[len(s2)-l], l-1)
#
# combinations(s, len(s1))