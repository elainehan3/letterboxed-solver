from pyscript import document
import os

'''
async def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    try:
        response = await pyfetch(
        "https://www.nytimes.com/puzzles/letter-boxed",
        method="GET")
    except Exception as e:
        response = e
        print(e)
    print(response)
    output_div.innerText = english
'''


def get_input() -> (str, str, str, str, str):
    top = document.querySelector("#top")
    t = top.value.upper()
    right = document.querySelector("#right")
    r = right.value.upper()
    bottom = document.querySelector("#bottom")
    b = bottom.value.upper()
    left = document.querySelector("#left")
    l = left.value.upper()
    already = document.querySelector("#alreadyWords")
    a = already.value.upper()
    return t,r,b,l,a

def get_dict(t: str, r: str, b: str, l: str):
    sides = {}
    for c in t:
        sides[c] = "t"
    for c in r:
        sides[c] = "r"
    for c in b:
        sides[c] = "b"
    for c in l:
        sides[c] = "l"
    return sides

def get_words(sides, t: str, r: str, b: str, l: str):
    with open("./words.txt") as file:
        allowed = set(t+r+b+l)
        valid = [word for word in file if set(word) <= allowed]
        remove = []
        for word in valid:
            c_last = word[0]
            i = 1
            while i < len(word):
                if (sides[word[i]] == sides[word[i-1]]):
                    remove.append(word)
                    break
                i += 1
        return set(valid) - set(remove)

def one_word_solution(word_list, chars):
    return [w for w in word_list if set(w) == chars]

# find two word solutions
def two_word_solution(word_list, chars):
    output = []
    for word in word_list:
        last = word[len(word)-1]
        matches = [w for w in word_list if w[0] == last and w!= word]
        for m in matches:
            pair = word + m
            if set(pair) == chars:
                output.append([word,m])
    return output

# find three word solutions
def three_word_solution(word_list, chars):
    ab = [a+b for a in word_list for b in word_list if a[-1]==b[0]]
    candidates = list(set([to_base(a)+a[-1] for a in ab]))
    solutions = {a:b for a in candidates for b in word_list if set(a+b)==chars and a[-1]==b[0]}
    ext = [[a+'-'+b,to_base(a+b)+b[-1]] for a in word_list for b in word_list if a!=b and a[-1]==b[0]]
    vals = ['-'.join([e[0],solutions[e[1]]]) for e in ext if e[1] in solutions.keys()]
    return [v.split('-') for v in vals]

def get_solutions(t: str, r: str, b: str, l: str, already:str):
    sides = get_dict(t,r,b,l)
    valid_words = get_words(sides, t, r, b, l)
    return valid_words

def display_solutions():
    output_div = document.querySelector("#output")
    output_div.innerText = english

def submit_handler(event = None):
    if event:
        event.preventDefault()
        output_div = document.querySelector("#output")
        output_div.innerText = os.listdir('/') 
        t,r,b,l,a = get_input()
        #solutions = get_solutions(t,r,b,l,a)
        output_div = document.querySelector("#output")
        output_div.innerText = os.listdir('/') 


def change_input(t, r, b, l, a): # unused
    top = document.querySelector("#top")
    top.value = t
    right = document.querySelector("#right")
    right.value = r
    bottom = document.querySelector("#bottom")
    bottom.value = b
    left = document.querySelector("#left")
    left.value = l
    already = document.querySelector("#alreadyWords")
    already.value = a
def reset_handler(event = None):
    if event:
        change_input("","","","","")

