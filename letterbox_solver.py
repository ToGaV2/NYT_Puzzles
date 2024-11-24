#! /usr/bin/python3
# Copyright 2022, Todd Gardiner, all rights reserved.
# This software is provided as-is, with no warranty expressed or implied.
# By using this software the user agrees to hold harmless the copyright holder.
# Further, the user agrees that use implies warrant of merchantability, function, and value.
# Further, the user agrees to release the copyright holder from all disputes between them and third parties.
# The copyright holder, and by extension the software, disclaims any and all third party liabilities; as they are disputes between unaffiliated users and third parties.
# All users explicity agree to these terms by using the software.

import urllib.request
from multiprocessing.process import signum

### NEEDED TO DO needs a severability section, to choose venue, and explicit agreement in download
### (digital signature and redundant agreements)...
### However, not commercially viable. So, instead being released as Apache License...

#URL for the U Michigan Word List (Omage to Barbara Quade...)
dictionlist = "https://www-personal.umich.edu/~jlawler/wordlist"

# URL for the english sowpods referenced list (~145k words)
dictionlist = "https://www.wordgamedictionary.com/english-word-list/download/english.txt"
# After a week of testing, the first two word lists are more than acceptable for this use case.
# However, these word lists wer replaced because necessary words for solutions were missed eventually missed.

# # BIGGER BETTER WORDLISTs This is an open source word list...
# 1 Collins Scrabble Dictionary - works really well from a code perspective. But it's copywritten...
# So I won't be distributing it...

# 2 Merriam-Webster, Collins, Oxford, and other respected dictionary offerings do not offer a licensing arrangement
# that will allow this software to economically be competitive in the marketplace (read see the light of day).
# Therefore, they are not an option.

# as a response to the inability to use the Intellectualy Property Protected Dictionaries, legally,
# another dictionary was sought... RIDYHEW (Ridiculously Huge English Word List) is the best answer I've found.
# The appropriate release is posted here -->  https://codehappy.net/wordlist/ridyhew.zip
# Download the zip, post your version somewhere, and then replace the URL here...
# dictionlist = "https://yoursite.com/hosting/yourRIDYHEW.txt"

# These comments are left in the source code to show the evolution of the system and the efforts taken to both develop
# a working system, AND respect the intellectual property of those in the eco-system which this code will be entering.

def worddict():
    # download the defined dictionary url
    response = urllib.request.urlopen(dictionlist)
    print(f'If the document downloaded correctly you\'ll get a 200 message there --> {response.code}')

    # create variables to hold the downloaded dictionary words
    blist =  []

    # loop through the lines in the dictionary
    for bline in response:
        # read each line of the doc into list['word']
        stripped = (bline.rstrip())
        blist.append(stripped.decode())
    total_words = len(blist)
    print(f'There are {total_words} loaded into the system.')
    return blist


#get variables validation of data function
def entervar(checks,length,phrase):
    while True:
        var = str(input(phrase))
        if len(var) == length and var.isalpha() and var not in checks:
            set= [var[0].lower(),var[1].lower(),var[2].lower()]
            break
        else:
            print("That's not 3 letters. Please try again.")
    return set

# run the program
if __name__ == '__main__':
    #load the dictionary
    blist = worddict()
    total_words = len(blist)

    #now get those letters from the NYT LetterBoxed Puzzle
    checks = []
    a = entervar(checks, 3, "What are the top 3 letters?  ")
    checks.append(a[0])
    checks.append(a[1])
    checks.append(a[2])
    b = entervar(checks, 3,"What are the right 3 letters?  ")
    checks.append(b[0])
    checks.append(b[1])
    checks.append(b[2])
    c = entervar(checks, 3,"What are the bottom 3 letters? ")
    checks.append(c[0])
    checks.append(c[1])
    checks.append(c[2])
    d = entervar(checks, 3,"What are the left 3 letters? ")
    checks.append(d[0])
    checks.append(d[1])
    checks.append(d[2])

    checkers = checks
    print('\n\n')
    print('Searching for Words with only these letters:' , checkers)

    # We can filter words that start with only those 12 letters as a first pass
    # We'll also remove anything with a number in it
    # Next, we'll limit our list to only those words with only good letters...

    clist = []
    # first pass loop through the words
    for i in range(len(blist)):
        word = blist[i].lower()
        #print(word[0])
        try:
            if word.isalpha() and word[0] in checkers:
                clist.append(word)
        except:
            pass
    print(clist[-5:])
    # how many words remain after first pass?
    after_clean = len(clist)
    perf =  (after_clean / total_words) *100
    print(f'There are {after_clean} words after first pass. {round(perf,2)}% of the original {total_words}\n')
    print(clist[:20])

    #second pass: check each letter in the remaining words against our inputs
    candidates = []
    for j in  range(len(clist)):
        word = clist[j]
        t = []
        # loop through the letters in the word
        for u in range(len(word)):
            # T/F to list for each letter in the word
            t.append(word[u] not in checkers)
        # Sum booleans, any True in the list, it's no good...
        if sum(t) == 0:
            candidates.append(word)
    after_clean2 = len(candidates)
    perf = (after_clean2 / total_words) * 100
    print(f'There are {after_clean2} words after second pass. {round(perf, 2)}% of the original {total_words}\n\n')

    #first pass on cleaning the list
    print('Words we can craft into our LetterBox: ', len(candidates))
    paginate = len(candidates) // 10 if len(candidates) % 10 == 0 else len(candidates)// 10 + 1
    for page in range(paginate):
        start = page * 10
        stop = start + 10
        print(candidates[start:stop])
    #print(candidates)

    #now we do the letter box test on each word
    cplus = []
    for j in range(len(candidates)):
        #reset vars for the word
        flipper = []
        ll = 0
        word = candidates[j]

        for u in range(len(word)):

            #check to ensure letter is from a different side
            if word[u] in flipper:
                break
            else:

                #set the flipper for the next iteration and add to ll each iteration
                if word[u] in a:
                    flipper = a
                    ll += 1
                elif word[u] in b:
                    flipper = b
                    ll += 1
                elif word[u] in c:
                    flipper = c
                    ll += 1
                elif word[u] in d:
                    flipper = d
                    ll += 1

        #if ll matches word length (aka no breaks) add to the cplus list

        if ll > 0  and ll == len(word):
            cplus.append(word)

    print('Words Boxed Successfully:' , len(cplus), '\n')

    # now we find out if any pangram the puzzle -->
    pgs = []
    for ip in cplus:
        lp = []
        for i in checkers:
            if i in ip:
                lp.append(True)
            else:
                lp.append(False)

        if sum(lp) == 12:
            pgs.append(ip)
        #    print(ip, ' ' , sum(lp))

    # now make two word combos of all boxable words and check for pangramming the puzzle
    doubles = []
    for ip in cplus:
        for i2p in cplus:
            if ip[-1] == i2p[0]:
                lp = []
                poss = ip + ' ' + i2p
                for i in checkers:
                    if i in poss:
                        lp.append(True)
                    else:
                        lp.append(False)

                if sum(lp) == 12:
                    pgs.append(poss)


    print("Found ", len(pgs), " one or two word combinations within the ", total_words, ' word dictionary.')
    print(pgs)