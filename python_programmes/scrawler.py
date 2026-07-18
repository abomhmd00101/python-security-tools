import requests

target = "https://192.168.9.114/"
wordlist_path = "subdomains.txt"


def request(url):
    try:
        req = requests.get(url)
        if req.status_code == 200:
            print(target+"/"+word)
        else:
            pass
    except requests.ConnectionError as e:
        print("[-]Connection error")


with open(wordlist_path) as words_file:
    for word in words_file:
        word = word.strip()
        request(target + "/" + word)
