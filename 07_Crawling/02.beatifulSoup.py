from bs4 import BeautifulSoup

# test0.html 파일 읽기

html = ''
with open('./test0.html', encoding='utf-8') as f:
    html = f.read()

# html 구조 분석

soup = BeautifulSoup(html, 'html.parser')

print(soup)