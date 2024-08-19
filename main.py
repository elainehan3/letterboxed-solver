import arrr
import pyscript


async def translate_english(event):
    input_text = pyscript.document.querySelector("#english")
    english = input_text.value
    output_div = pyscript.document.querySelector("#output")
    try:
        response = await pyscript.fetch(
        "https://www.nytimes.com/puzzles/letter-boxed",
        method="GET").json()
    except Exception as e:
        response = e
    print(response)
    output_div.innerText = arrr.translate(english) + response
