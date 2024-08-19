import arrr
from pyscript import document
from pyscript import fetch


async def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    try:
        response = await fetch(
        "https://www.nytimes.com/puzzles/letter-boxed",
        method="GET").json()
    except Exception as e:
        response = e
    print(response)
    output_div.innerText = arrr.translate(english) + response
