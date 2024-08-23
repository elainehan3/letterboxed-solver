import json
from typing import Dict, List

# Below is unused code that is not needed for the function of the program
# used once to remove unusable words from the word list

def check_dupes(word):
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            return True
    return False


def remove_bad():
    with open("./words1.txt", "r+") as file:
        d = file.readlines()
        file.seek(0)
        for word in d:
            if (len(set(word)) <= 13 and not check_dupes(word)):
                file.write(word)
        file.truncate()

remove_bad()


def make_dict() -> Dict[str, any]:
    def make_empty_dict():
        d = {}
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        d["Z"] = {"Z": []}
        for i in range(25,-1,-1):
            print(alphabet[i])
            d[alphabet[i]] = {}
            for key in d.keys():
                if (key is not alphabet[i]):
                    d[alphabet[i]][key] = d[key]
            d[alphabet[i]][alphabet[i]] = []
        return d
    with open("./dict1.json", "w") as outfile:
        d = make_empty_dict()
        print("done")
        p = json.dumps(d)
        print("done2")
        outfile.write(p)

    with open("./words1.txt", "r") as file:
        # remove all words with more than 12 unique characters
        # remove all words with same character twice in a row
        valid = [[word, sorted(set(word))] for word in file if len(set(word)) <= 12 and not check_dupes(word)]
        d = make_empty_dict()
        for word_group in valid:
            word = word_group[0]
            set_word = word_group[1]
            travel = d
            i = 1
            while i < len(set_word):
                new = travel[set_word[i]]
                travel = new
                i += 1
            travel[set_word[-1]].append(word)
            print(set_word)
        print("done")
        valid_dict = json.dumps(d)

    with open("./dict1.json", "rw") as outfile:
        outfile.write(valid_dict)
        outfile.close()



  