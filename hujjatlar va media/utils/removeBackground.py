import requests
import logging
url = "https://background-removal.p.rapidapi.com/remove"

payload = "image_url=https%3A%2F%2Fobjectcut.com%2Fassets%2Fimg%2Fraven.jpg"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-host': "background-removal.p.rapidapi.com",
    'x-rapidapi-key': "801a7550dcmsh0cd07bd9b136744p1984d9jsn22d3897ebcec"
    }

async def remove_background(img_url):
    payload=f"image_url={img_url}"
    response = requests.request("POST", url, data=payload, headers=headers)
    link=response.json()['response']['image_url']
    return link