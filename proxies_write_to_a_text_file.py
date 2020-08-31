import requests , random
from bs4 import BeautifulSoup
         ################################ th3h04x #################################

def write_to_file(proxies):

    with open('proxies.txt','w') as file:
        for a in proxies:
            file.write("".join(a) + '\n')

    print("[+]finished writing to the file[+]")

def get_proxies():

    url = "https://free-proxy-list.net/"
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    proxies = []

    for row in soup.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    #print(proxies)
    return proxies



def get_session(proxies):
    
    session = requests.Session()

    proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session


if __name__ == "__main__":

    proxies = get_proxies()

    write_to_file(proxies)

    for i in range(5):
        s = get_session(proxies)
        try:
            print("Request page with IP:", s.get("http://icanhazip.com", timeout=2).text.strip())
        except Exception as e:
            continue
