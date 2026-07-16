import requests
from scanner import Scanner

target_url = 'http://10.0.0.11/'
block_links = []
#block_links = ["http://10.0.0.10/dvwa/"]
#data_dict = {'username' : 'admin' , 'password' : 'password' , }
vulnerability_scanner = Scanner(target_url, block_links)
#vulnerability_scanner.session.post('http://10.0.0.10/dvwa/login.php', data=data_dict)


print("[+] CRAWLING ..........." + "\n ___________________________________")

vulnerability_scanner.crawl()
print("[+] SCANNING ..........." + "\n ____________________________________________")
vulnerability_scanner.run_scanner()









