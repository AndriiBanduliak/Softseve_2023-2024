import random


def randomWord(inputlist):
    if inputlist:
        while True:
            wordlist = list(inputlist)
            while wordlist:
                yield wordlist.pop(random.randint(0, len(wordlist) - 1))
    else:
        yield None
