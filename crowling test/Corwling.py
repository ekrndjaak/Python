#미국 개인소비지출물가 크롤링하기
from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%AF%B8%EA%B5%AD+%EA%B0%9C%EC%9D%B8%EC%86%8C%EB%B9%84%EC%A7%80%EC%B6%9C%EB%AC%BC%EA%B0%80&oquery=%EB%AF%B8%EA%B5%AD+%EA%B0%9C%EC%9D%B8%EC%86%8C%EB%B9%84%EC%A7%80%EC%B6%9C&tqi=iKyM1lp0Yidss49Jlg4ssssst3G-134083")
soup = BeautifulSoup(response, "html.parser") #html에 대하여 접근할 수 있도록

value = soup.find("strong", {"class":"num"})
print(value)

value2 = value.text.strip()
print(value2[0:4])