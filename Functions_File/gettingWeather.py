import requests
from bs4 import BeautifulSoup

def get_weather(city):
    search = f"weather in {city}"
    url = f"https://www.google.com/search?q={search}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      " AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/141.0.0.0 Safari/537.36"
    }

    # Make the request
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, "html.parser")

    # Try to find temperature
    temp_element = soup.find("span", attrs={"id": "wob_tm"})
    desc_element = soup.find("div", attrs={"id": "wob_dcp"})

    if temp_element and desc_element:
        temp = temp_element.text
        desc = desc_element.text
        result = f"The weather in {city} is {temp}°C with {desc.lower()}."
    else:
        result = "Sorry, I couldn't fetch the weather right now. Please try again later."

    print(result)
    return result
