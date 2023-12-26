import requests
from bs4 import BeautifulSoup

DEFAULT_TIME_OUT = 5
DETECT_HEADER = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"}

def GetPageTitle(url):
    print("Now detect: {}".format(url))
    try:
        resp = requests.get(url, headers=DETECT_HEADER, verify=False, timeout=DEFAULT_TIME_OUT)
        code = resp.status_code
        html = resp.content
        tree = BeautifulSoup(html, "html.parser")
        title = tree.title.contents[0]
        return code, title
    except Exception as e:
        return 600, "TimeOut"


if __name__ == "__main__":
    GetPageTitle("https://www.huolala.cn")
