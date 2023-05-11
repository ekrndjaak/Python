#로또 1등 당첨금액 크롤링 프로그램
from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen("https://search.naver.com/search.naver?sm=tab_sug.aslt&where=nexearch&query=%EB%A1%9C%EB%98%90%EB%B2%88%ED%98%B8&oquery=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%B8%EA%B5%AC%EC%88%98&tqi=ia0Talp0YihsseWnQoVssssstLl-396442&acq=%EB%A1%9C%EB%98%90%EB%B2%88%ED%98%B8&acr=1&qdt=0")
soup = BeautifulSoup(response, "html.parser") #html에 대하여 접근할 수 있도록

value = soup.find("p",{"class":"win_text"})
print(value)


value = value.text.strip()

print(value)