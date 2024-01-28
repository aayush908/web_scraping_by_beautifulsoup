import requests

def fetch_and_save(url , path):
    r = requests.get(url)
    with open(path , "w", encoding='utf-8') as f:
        f.write(r.text)
        f.close()
        
url = "https://timesofindia.indiatimes.com/"
url2 = "https://quickloom.onrender.com/"
path = "data/times.html"
path2 = "data/quickloom.html"
# fetch_and_save(url2 , path2)
fetch_and_save(url , path)
