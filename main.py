import arrr
from pyscript import document, fetch


async def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    response = await fetch(
    "https://examples.pyscriptapps.com/api-proxy-tutorial/api/proxies/status-check",
    method="GET"
).text()
    print(response)
    output_div.innerText = arrr.translate(english) + response
