import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_cookies():
    # 设定无头浏览器选项（可选）
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.baidu.com")

    # 获取 cookies
    selenium_cookies = driver.get_cookies()
    driver.quit()

    cookies = {cookie['name']: cookie['value'] for cookie in selenium_cookies}
    return cookies

def get_search_results(keyword = "deepseek", max_pages = 2):
    # 自动获取 Edge 浏览器的 cookie
    cookies = get_cookies()
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
    # 获得每页搜索结果
    cnt = 0
    for page in range(max_pages):
        print('开始爬取第{}页'.format(page + 1))
        url = 'https://www.baidu.com/s?wd=' + keyword +'&pn=' + str(page*10)
        r = requests.get(url, headers=headers, cookies=cookies)
        html = r.text
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(html, 'html.parser')
        divs = soup.find_all('div', class_=re.compile('c-container'))
        for div in divs:
            try:
                title = div.h3.a.text
                link = div.h3.a['href']
            except:
                continue

            # 通用方式提取摘要
            desc = None

            # 方法1：找 p 标签（最常见情况）
            if desc is None:
                p_tag = div.find('p')
                if p_tag:
                    desc = p_tag.get_text(strip=True)

            # 方法2：如果没有 p，再找可能的 span，带 text 类的（百度百科常有）
            if desc is None:
                span_tags = div.find_all('span', class_=re.compile(".*text.*"))
                desc_texts = [span.get_text(strip=True) for span in span_tags if span.get_text(strip=True)]
                if desc_texts:
                    desc = "\n".join(desc_texts)

            # 方法3：最后兜底：找所有可见文本拼接（防止错过结构怪异的条目）
            if desc is None:
                desc = div.get_text(separator="\n", strip=True)

            cnt += 1
            yield {'title': title, 'link': link, 'summary': desc}
        print('正在爬取:{},共查询到{}个结果'.format(url, cnt))

if __name__ == "__main__":
    for k in get_search_results(keyword="深度学习", max_pages=2):
        print(k)