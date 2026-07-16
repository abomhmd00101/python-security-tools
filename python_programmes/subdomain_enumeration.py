import requests                                        #هاي المكتبة متخصصه في المواقع بحيث انها بتجيب الريكويستات من المواقع

#url = input('Enter URL(without http://): ')
url = "google.com"


def request(url):
    try:
        request = requests.get("https://" + url)       # request.get يعني هات الريسبونس تبع الموقع اللي بدي اعطيه اياه (200و404و300) الخخ
        if request.status_code == 200:
            print(request,"https://"+url )   
            
        else:
        	pass
        
        
        
    except requests.exceptions.ConnectionError :
        print("[-] Connection Error " ,"https://" + url)



with open("/home/kali/Desktop/subdomains.txt") as words_file:
    for line in words_file:
        line = line.strip()
        request(line + "." + url)      #earth
