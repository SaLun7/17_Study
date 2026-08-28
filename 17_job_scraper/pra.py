import requests
from bs4 import BeautifulSoup

search = "파이썬"
url = f"https://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=recently&searchword={search}"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'
}

r = requests.get(url, headers=headers)


soup = BeautifulSoup(r.text, "html.parser")
lis = soup.find_all("div", class_ = "item_recruit")

jobs = []

for li in lis:
    try:
        company = li.find("div", class_ = "area_corp").find("strong", class_ = "corp_name").find("a").text.strip()
        title = li.find("div", class_ = "area_job").find("h2", "job_tit").find("a").text.strip()
        due_date = li.find("div", class_ = "job_data").find("span", class_ = "date").text.strip()
        print(company)
    except:
        pass

    