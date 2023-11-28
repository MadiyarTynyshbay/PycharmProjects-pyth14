import requests

url = 'https://httpbin.org/image/jpeg'

response = requests.get(url)

binary_img = response.content

with open('test_img.jpeg', 'wb') as file:
    file.write(binary_img)


