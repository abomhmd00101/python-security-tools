#!/user/bin/env python3


import requests


def request(url):
    try:
        return requests.get("https://" + url)  # 200
    except requests.exceptions.ConnectionError:
        pass


target_url = "example.com"

with open("/home/kali/Desktop/raft-small-files_fuzzing.txt") as wordlist_file:
     	
    for line in wordlist_file:
        word = line.strip()
        test_page = target_url + "/" + word      
        response_page = request(test_page)
   
       	if response_page:
            print("Discovered Page   ------>", "https://" + test_page)
            	

            	
print("--------------------------------------------------------------------------")           	
            	
#with open("/home/kali/Desktop/subdomains.txt") as wordlist_file:


request(target_url)
