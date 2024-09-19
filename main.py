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
    with open("./words1.txt") as file:
        allowed = set(t+r+b+l+"\n")
        valid = [word.strip() for word in file if set(word) <= allowed]
        remove = []
        for word in valid:
            i = 1
            while i < len(word):
                if (sides[word[i]] == sides[word[i-1]]):
                    remove.append(word)
                    break
                i += 1
        return set(valid) - set(remove)
        # valid = [word for word in file]
        # return set(valid)

def one_word_sols(words, allowed):
    output = ["<p>" + word + "</p>" for word in words if set(word) == allowed]
    if len(output) == 0:
        output = ["<p>NO ONE WORD SOLUTIONS FOUND</p>"]
    return "".join(output)

# find two word solutions
def two_word_sols(words, allowed):
    output = []
    for word in words:
        last = word[len(word)-1]
        matches = [w for w in words if w[0] == last and w!= word]
        for match in matches:
            pair = word + match
            if set(pair) == allowed:
                output.append("<p>" + word + "→" + match + "</p>")
    return "".join(output)

# find three word solutions
def three_word_solutions(words, chars):
    ab = [a+b for a in words for b in words if a[-1]==b[0]]
    candidates = list(set([to_base(a)+a[-1] for a in ab]))
    solutions = {a:b for a in candidates for b in words if set(a+b)==chars and a[-1]==b[0]}
    ext = [[a+'-'+b,to_base(a+b)+b[-1]] for a in words for b in words if a!=b and a[-1]==b[0]]
    vals = ['-'.join([e[0],solutions[e[1]]]) for e in ext if e[1] in solutions.keys()]
    return [v.split('-') for v in vals]

def get_solutions(t: str, r: str, b: str, l: str, already:str):
    sides = get_dict(t,r,b,l)
    valid_words = get_words(sides, t, r, b, l)
    allowed = set(t+r+b+l)
    one_word_solution = one_word_sols(valid_words, allowed)
    two_word_solution = two_word_sols(valid_words, allowed)
    return one_word_solution, two_word_solution

def display_solutions(one_word, two_word):
    head_one = document.querySelector("#one_word_head")
    head_two = document.querySelector("#two_word_head")
    div_one = document.querySelector("#one_word_sols")
    div_two = document.querySelector("#two_word_sols")
    head_one.innerHTML = "<h2>One Word Solutions</h2>"
    head_two.innerHTML = "<h2>Two Word Solutions</h2>"
    div_one.innerHTML = one_word
    div_two.innerHTML = two_word

def submit_handler(event = None):
    if event:
        event.preventDefault()
        t,r,b,l,a = get_input()
        one_word_solution, two_word_solution = get_solutions(t,r,b,l,a)
        display_solutions(one_word_solution, two_word_solution)


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

