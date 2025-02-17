from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# pip list -> 설치 항목들
# pip show beautifulsoup4 -> 간단한 정보들
# pip install --upgrade beautifulsoup4 -> 버전 업그레이드
# pip uninstall beautifulsoup4 -> 삭제