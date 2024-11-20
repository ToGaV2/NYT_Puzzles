#!/usr/bin/env python3
"""
This is the original Wordle Game Solver Program written in 2021
Run each cell as needed to solve your game...
"""
import urllib.request
import math
#from pprint import pprint

## You'll need a dictionary. Here are two publicly available word lists.
# These free word lists are incomplete. Not all puzzle words are represented.

# download the U Michigan Word List (~65k words)
dictionlist = "https://www-personal.umich.edu/~jlawler/wordlist"
# download the english sowpods referenced list (~145k words)
dictionlist = "https://www.wordgamedictionary.com/english-word-list/download/english.txt"


# If you want to ensure you most of the words from the NYT Games, I suggest the
# RIDYHEW wordlist available here (zip): https://codehappy.net/wordlist/ridyhew.zip
# RIDYHEW homepage and documentation is here: https://codehappy.net/wordlist.htm
# You'll need to download the wordlist, place it somewhere online, and then reference it...


def checker(ff, gg):
    nn = []
    tt = []
    for i in elist:
        p = 0
        for l in i:
            if l not in ff:
                p += 1
        if p == 5:
            nn.append(i)
    # now run the list through the charcount function
    for i in nn:
        if len(gg) > 0:
            pp = 0
            for l in gg:
                if l in i:
                    pp += 1
            if pp < len(gg):
                tt.append(i)
    for i in tt:
        nn.remove(i)
    print(clooker(nn))
    return nn


def clooker(list):
    looks = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
             'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for i in list:
        for l in i:
            looks.setdefault(l, 0)
            looks[l] += 1
    print('These are the letters and corresponding word prevalence left in the alphabet.')
    dl = sorted([(v, k) for k, v in looks.items()], reverse=True)
    return dl


blist = []
list = []

response = urllib.request.urlopen(dictionlist)
print(f'If the document downloaded correctly you get a 200 message: {response.code}')

for bline in response:
    # read each line of the doc into list['word']
    #   line.decode(encoding)
    stripped = (bline.rstrip())
    blist.append(stripped.decode())
total_words = len(blist)
print(f'There are {total_words} loaded into the system.')
print('Working to remove unnecessary words. (>5 characters, hyphens, roman numerals, numbers, etc.)')

elist = []
for i in blist:
    if i.isalpha():
        if len(i) == 5:
            # if i.islower() :
            elist.append(i.lower())
set = len(elist)
eliminated = (1 - (round(set / total_words, 2))) * 100
print(f'Complete. {set} words remain. Elimated {eliminated}% so far')

# trail: use the best word you've got (will improve over time)
print('Please input "trail" into the Wordle.')
print('(this word has very popular letters that check over half of the possibilities...')

yes = input('Ready to Continue? (Yes or No) ')
ff = []
gg = []
if yes.lower() == 'yes' or yes.lower() == 'y':
    print(' ')
    while True:
        print('Please input the BAD letters one at a time')
        print('we already know these are bad:', ff, ')')
        c = str(input('Input a letter (hit enter to stop): '))
        if c == '':
            break
        elif c.isalpha and len(c) == 1:
            ff.append(c)
    print(' ')
    while True:
        print('Please input the GOOD letters one at a time')
        print('we already know these are good:', gg, ')')
        g = str(input('Input a letter (hit enter to stop):'))
        if g == '':
            break
        elif g.isalpha and len(g) == 1:
            gg.append(g)

    print(' ')
    print('-------------- checks completed successfully --------------')
    ylist = checker(ff, gg)
    print(f'We\'re down to {len(ylist)} words out of {total_words}.')
    print('Try one of these words next. ')
    pset = math.ceil(len(ylist) / 10)
    for i in range(pset):
        st = i * 10
        stop = i * 10 + 10
        print(ylist[st:stop])
    print("Tip: Try to pick one with the most popular letters above...")

"""# Enter the word you've chosen into Wordle, then come back
##(and run the next cell)
"""

yes = input('Ready to Continue? (Yes or No) ')
if yes.lower() == 'yes' or yes.lower() == 'y':
    print("Round 2:")
    print(' ')
    while True:
        print('Please input the BAD found letters one at a time')
        print('(we already know these are bad:', ff, ')')
        c = str(input('Input a letter (hit enter to stop): '))
        if c == '':
            break
        elif c.isalpha and len(c) == 1:
            ff.append(c)
    print(' ')
    while True:
        print('Please input the GOOD letters one at a time')
        print('(we already know these are good:', gg, ')')
        g = str(input('Input a letter (hit enter to stop): '))
        if g == '':
            break
        elif g.isalpha and len(g) == 1:
            gg.append(g)

    print(' ')
    print('-------------- checks completed successfully --------------')
    ylist = checker(ff, gg)
    print(f'We\'re down to {len(ylist)} words out of {total_words}.')
    print('Try one of these words next. ')
    pset = math.ceil(len(ylist) / 10)
    for i in range(pset):
        st = i * 10
        stop = i * 10 + 10
        print(ylist[st:stop])
    print("Tip: Try to pick one with the most popular letters above...")
else:
    print("Have a nice day :)")

"""#Round 3: Input the word you've chosen from above into Wordle.
##(Then come back and run the next cell)
"""

yes = input('Ready to Continue? (Yes or No) ')
if yes.lower() == 'yes' or yes.lower() == 'y':
    print("Round 3:")
    print(' ')
    while True:
        print('Please input the BAD found letters one at a time')
        print('(we already know these are bad:', ff, ')')
        c = str(input('Input a letter (hit enter to stop): '))
        if c == '':
            break
        elif c.isalpha and len(c) == 1:
            ff.append(c)
    print(' ')
    while True:
        print('Please input the GOOD letters one at a time')
        print('(we already know these are good:', gg, ')')
        g = str(input('Input a letter (hit enter to stop): '))
        if g == '':
            break
        elif g.isalpha and len(g) == 1:
            gg.append(g)

    print(' ')
    print('-------------- checks completed successfully --------------')
    ylist = checker(ff, gg)
    print(f'We\'re down to {len(ylist)} words out of {total_words}.')
    print('Try another word, with the most popular letters above...')
    pset = math.ceil(len(ylist) / 10)
    for i in range(pset):
        st = i * 10
        stop = i * 10 + 10
        print(ylist[st:stop])
    print("Pick a word. OR have me line up your green letters.")
else:
    print("Have a nice day :)")

"""#Round 4: You're running out of chances to win this wordle...
This round will use the same format. Good Luck!!!

"""

print("Round 4:")
yes = input('Continue? (Yes or No) ')
if yes.lower() == 'yes' or yes.lower() == 'y':
    while True:
        print('Please input the BAD found letters one at a time')
        print('(we already know these are bad:', ff, ')')
        c = str(input('Input a letter (hit enter to stop): '))
        if c == '':
            break
        elif c.isalpha and len(c) == 1:
            ff.append(c)
    print(' ')
    while True:
        print('Please input the GOOD letters one at a time')
        print('(we already know these are good:', gg, ')')
        g = str(input('Input a letter (hit enter to stop): '))
        if g == '':
            break
        elif g.isalpha and len(g) == 1:
            gg.append(g)

    print(' ')
    print('-------------- checks completed successfully --------------')
    ylist = checker(ff, gg)
    print(f'We\'re down to {len(ylist)} words out of {total_words}.')
    print('Try another word, with the most popular letters above...')
    pset = math.ceil(len(ylist) / 10)
    for i in range(pset):
        st = i * 10
        stop = i * 10 + 10
        print(ylist[st:stop])
    print("We have to pick a word from these.")
else:
    print("Have a nice day :)")

print("Round 4:")
yes = input('Continue? (Yes or No) ')
if yes.lower() == 'yes' or yes.lower() == 'y':
    while True:
        print('Please input the BAD found letters one at a time')
        print('(we already know these are bad:', ff, ')')
        c = str(input('Input a letter (hit enter to stop): '))
        if c == '':
            break
        elif c.isalpha and len(c) == 1:
            ff.append(c)
    print(' ')
    while True:
        print('Please input the GOOD letters one at a time')
        print('(we already know these are good:', gg, ')')
        g = str(input('Input a letter (hit enter to stop): '))
        if g == '':
            break
        elif g.isalpha and len(g) == 1:
            gg.append(g)

    print(' ')
    print('-------------- checks completed successfully --------------')
    ylist = checker(ff, gg)
    print(f'We\'re down to {len(ylist)} words out of {total_words}.')
    print('Try another word, with the most popular letters above...')
    pset = math.ceil(len(ylist) / 10)
    for i in range(pset):
        st = i * 10
        stop = i * 10 + 10
        print(ylist[st:stop])
    print("We have to pick a word from these.")
else:
    print("Have a nice day :)")


print("Round 5:")
yes = input('Continue? (Yes or No) ')
if yes.lower() == 'yes' or yes.lower() == 'y':
    while True:
        print('Please input the BAD found letters one at a time')
        print('(we already know these are bad:', ff, ')')
        c = str(input('Input a letter (hit enter to stop): '))
        if c == '':
            break
        elif c.isalpha and len(c) == 1:
            ff.append(c)
    print(' ')
    while True:
        print('Please input the GOOD letters one at a time')
        print('(we already know these are good:', gg, ')')
        g = str(input('Input a letter (hit enter to stop): '))
        if g == '':
            break
        elif g.isalpha and len(g) == 1:
            gg.append(g)

    print(' ')
    print('-------------- checks completed successfully --------------')
    ylist = checker(ff, gg)
    print(f'We\'re down to {len(ylist)} words out of {total_words}.')
    print('Try another word, with the most popular letters above...')
    pset = math.ceil(len(ylist) / 10)
    for i in range(pset):
        st = i * 10
        stop = i * 10 + 10
        print(ylist[st:stop])
    print("We have to pick a word from these.")
else:
    print("Have a nice day :)")


print("Bonus Round:")
yes = input('Continue? (Yes or No) ')
if yes.lower() == 'yes' or yes.lower() == 'y':
    while True:
        print('Please input the BAD found letters one at a time')
        print('(we already know these are bad:', ff, ')')
        c = str(input('Input a letter (hit enter to stop): '))
        if c == '':
            break
        elif c.isalpha and len(c) == 1:
            ff.append(c)
    print(' ')
    while True:
        print('Please input the GOOD letters one at a time')
        print('(we already know these are good:', gg, ')')
        g = str(input('Input a letter (hit enter to stop): '))
        if g == '':
            break
        elif g.isalpha and len(g) == 1:
            gg.append(g)

    print(' ')
    print('-------------- checks completed successfully --------------')
    ylist = checker(ff, gg)
    print(f'We\'re down to {len(ylist)} words out of {total_words}.')
    print('Try another word, with the most popular letters above...')
    pset = math.ceil(len(ylist) / 10)
    for i in range(pset):
        st = i * 10
        stop = i * 10 + 10
        print(ylist[st:stop])
    print("We have to pick a word from these.")
else:
    print("Have a nice day :)")