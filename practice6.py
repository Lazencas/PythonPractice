
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

#pip list   //설치된 모듈 리스트
#pip show 패키지명   //해당 모듈에대한 상세정보표시
#pip install --upgrade 패키지명  //해당 모듈 최신버전으로 업그레이드
#pup uninstall 패키지명  //모듈삭제