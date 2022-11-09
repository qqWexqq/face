import requests


data = {'img1': "C:/Users/Centr/Desktop/face/images/snoop1.jpg", "img2":"C:/Users/Centr/Desktop/face/images/durov2.jpg"}

a = requests.get('http://127.0.0.1:5000/analyze', json=data).content


b = requests.get('http://127.0.0.1:5000/find', json=data).content


c = requests.get('http://127.0.0.1:5000/getsimilar', json=data).content
print(a)
print(b)
print(c)
