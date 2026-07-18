import requests
from bs4 import BeautifulSoup
import urllib.request

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError :
        pass




target_url = 'https://example.com'
response = request(target_url)

parsed_html = BeautifulSoup(response.content.decode(), "html.parser")
forms_lists = parsed_html.find_all('form')


for form in forms_lists:
    action = form.get('action')
    post_url = urllib.parse.urljoin(target_url, action)
    method = form.get('method')


    input_lists = parsed_html.find_all('input')
    post_data = {}

    for input in input_lists:
        input_name = input.get('name')
        input_type = input.get('type')
        input_value = input.get('value')

        if input_type == 'text':
            input_value = value



        post_data[input_name] = input_value

    result = requests.post(post_url, data=post_data)
    print(result.content.decode())
