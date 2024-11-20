#!/usr/bin/env python3
"""
This is the refactored Wordle Game Solver Program written in 2021
Run each cell as needed to solve your game...
"""
import urllib.request
import math

### You'll need a dictionary. Here are two publicly available word lists. ###
# These free word lists are incomplete. Not all puzzle words are represented. #
# download the U Michigan Word List (~65k words)
dictionlist = "https://www-personal.umich.edu/~jlawler/wordlist"
# download the english sowpods referenced list (~145k words)
dictionlist = "https://www.wordgamedictionary.com/english-word-list/download/english.txt"

# If you want to ensure you most of the words from the NYT Games, I suggest the
# RIDYHEW wordlist available here (zip): https://codehappy.net/wordlist/ridyhew.zip
# RIDYHEW homepage and documentation is here: https://codehappy.net/wordlist.htm
# You'll need to download the wordlist, place it somewhere online, and then reference it...

# function to eliminate words > or < 5 letters
def checker(ff: list, gg: list) -> list:  # bad letter and good letter lists
    nn, tt = [], []  #empty variables
    # loop through dictionary and kick out the words with a letter on the bad list
    for i in elist:
        p = 0  # incrementer set to zero for each word
        for l in i:  # loop through letters in the word
            if l not in ff:  # is the letter on the bad list?
                p += 1  # if not increment
        if p == 5: # no letters are on the bad list?
            nn.append(i) # add it to the remaining word list
    # loop through the remaining words and doublecheck the good list letters
    for i in nn: # loop through the remaining words
        if len(gg) > 0: # do we have a good letter list?
            pp = 0 # set incrementer to 0 for each iteration
            for l in gg: # loop through the good list letters
                if l in i: # is the letter in the word?
                    pp += 1 # if so increment
            if pp < len(gg): # pp should equal length of gg
                tt.append(i) # if not add to error list

    for i in tt:  # remove the error list words
        nn.remove(i)

    clooker(nn)  # run the letter counter
    return nn  # return the good word list

# function to count occurences of each letter within remaining dictionary
def clooker(list):
    # start with zero'd dictionary of english letters
    looks = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
             'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    # loop through the words
    for i in list:
        # loop though the letters in each word
        for l in i:
            # error catch weird letters
            looks.setdefault(l, 0)
            # increment the letter
            looks[l] += 1
    print('These are the letters and corresponding word prevalence left in the alphabet.')
    dl = sorted([(v, k) for k, v in looks.items()], reverse=True) # sort by prevalence
    print(dl) # print the results to stdout

if __name__ == '__main__':
    # load the dictionary
    blist, list = [], []  # empty variables
    response = urllib.request.urlopen(dictionlist)  # download the list and result
    print(f'If the document downloaded correctly you get a 200 message: {response.code}')

    # process the dictionary into full byte decoded dictionary list
    for bline in response:
        # read each line of the dictionary doc into list['word']
        #   line.decode(encoding)
        stripped = (bline.rstrip())
        blist.append(stripped.decode())
    total_words = len(blist)
    print(f'There are {total_words} loaded into the system.')
    print('Working to remove unnecessary words. (>5 characters, hyphens, roman numerals, numbers, etc.)')

    # process into wordle compliant list (alpha, 5 letters, no spaces)
    elist = []  #variable to catch list
    for i in blist:  # loop through full dictionary
        if i.isalpha():  # check for all alpha characters
            if len(i) == 5:  # check the length
                # if i.islower() :
                elist.append(i.lower())  #add it to the list

    # measure the result and report to stdout
    set = len(elist)
    eliminated = (1 - (round(set / total_words, 2))) * 100
    print(f'Complete. {set} words remain. Elimated {eliminated}% so far')

    # trail: use the best word you've got (will improve over time)
    print('\n\nPlease input "trail" into the Wordle.\n')
    print('(this word has very popular letters that check over half of the possibilities...\n\n')

    ff, gg, rounds, thisround = [], [], 6, 1  # bad list, good list, max rounds, current round
    while rounds > thisround:
        yes = input('Ready to Continue? (Yes or No) ')
        if yes.lower() == 'yes' or yes.lower() == 'y':
            print(f'Great, let`s enter the results from Round {thisround}.')
            print('Please input the Non-Matching letters, one at a time...')
            while True:
                if len(ff) > 0:
                    print('Letters we already know are bad:', ff, ')')
                c = str(input('Input a letter (or hit enter to move on): '))
                if c == '':
                    break
                elif c.isalpha and len(c) == 1:
                    ff.append(c)
            print(' ')
            print('Please input the Matching letters, one at a time...')
            while True:
                if len(gg)>0:
                    print('Letters we already know are good:', gg, ')')
                g = str(input('Input a letter (or hit enter to move on):'))
                if g == '':
                    break
                elif g.isalpha and len(g) == 1:
                    gg.append(g)

            print(' ')
            print('-------------- checks completed successfully --------------')
            ylist = checker(ff, gg)
            if len(ylist) == 0:
                print('Uh Oh. There are no words left. Please start the program over.')
                break

            print(f'We\'re down to {len(ylist)} words out of {total_words}.')
            print('Try one of these words next. ')
            pset = math.ceil(len(ylist) / 10)
            for i in range(pset):
                st = i * 10
                stop = i * 10 + 10
                print(ylist[st:stop])

            thisround += 1
        else:
            print("Have a wonderful rest of your day!")
            break

    print("Thanks for using this Wordle Solver.")