from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import datetime


class Driver:
    def __init__(self):
        options = webdriver.ChromeOptions()
#         options.add_argument('headless')
        options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
        self.driver = webdriver.Chrome(
            '/Users/WMHY/Downloads/chromedriver', options=options)

    def __call__(self):
        return self.driver

    def get_url(self, url):  # 새 창으로 url 열기
        self.driver.get(url)

    def get_default(self):  # default 프레임 이동
        while True:
            try:
                self.driver.switch_to_default_content()
                return
            except:
                print('default frame 이동')
                pass

    def get_fra(self, name):  # 특정 프레임 이동
        while True:
            try:
                self.driver.switch_to_frame(name)
                break
            except:
                self.get_default()
                print(name, 'frame 이동')
                continue

    def find_by_xpath(self, xpath):  # Xpath로 단일 요소 찾기
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                            (By.XPATH, xpath)))

    def find_by_class(self, class_name):  # class name으로 단일 요소 찾기
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                            (By.CLASS_NAME, class_name)))

    def find_by_tag(self, tag):  # tag로 단일 요소 찾기
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.TAG_NAME, tag)))

    def find_by_name(self, name):  # name으로 단일 요소 찾기
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, name)))

    def find_all_by_class(self, class_name):  # class name으로 모든 요소 찾기
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.TAG_NAME, class_name)))

    def find_all_by_tag(self, tag):  # tag로 모든 요소 찾기
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.TAG_NAME, tag)))

    def find_all_by_name(self, name):  # name으로 모든 요소 찾기
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.NAME, name)))

    def find_all_by_tag_with_obj(self, obj, name):  # tag으로 모든 요소 찾기
        return WebDriverWait(obj, 20).until(
            EC.presence_of_all_elements_located(
                (By.TAG_NAME, name)))

    def find_by_tag_with_obj(self, obj, name):  # tag으로 요소 찾기
        return WebDriverWait(obj, 20).until(
            EC.presence_of_element_located(
                (By.TAG_NAME, name)))

    def find_by_link(self, text):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, text)))

    def click(self, btn):
        self.driver.execute_script("arguments[0].click();", btn)

    def close(self):
        self.driver.close()


a = Driver()
# 홈페이지 접속
a.get_url('https://www.holidaykorea.kr/main/index.php')

# 로그인
a.find_by_xpath("//*[@id='header']/div[1]/div[1]/div/ul[2]/li[1]/a").click()
# 아이디 입력
a.find_by_xpath("//input[@id='loginId']").send_keys("woomir")
# 비번 입력
a.find_by_xpath("//*[@id='loginPwd']").send_keys("$52Telecast")
a.find_by_xpath("//*[@id='formLogin']/div[1]/div[1]/button").click()

# 숏베
# a.get_url('https://www.holidaykorea.kr/goods/goods_view.php?goodsNo=1000000212')

# Test
a.get_url('https://www.holidaykorea.kr/goods/goods_view.php?goodsNo=1000000216')

# 풀플라이
# a.get_url('https://www.holidaykorea.kr/goods/goods_view.php?goodsNo=1000000156')


count = 0
while count < 1:
    a.get_url('https://www.holidaykorea.kr/goods/goods_view.php?goodsNo=1000000212')
    html = a.driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    soldOutCheck = soup.select_one('button.btn_add_soldout')
    print(soldOutCheck)
    if soldOutCheck == None:
        count += 1

# 옵션 선택
a.find_by_xpath(
    "//*['@id=frmView']/div/div/div[2]/div/dl/dd/div/a").click()
html = a.driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 내용 읽기
contents = soup.select('li.active-result')
for aa in contents:
    if '블랙' in aa.get_text().split():
        index = aa["data-option-array-index"]

# 블랙 선택
indexA = int(index) + 1
xpath = "//*[@id='frmView']/div/div/div[2]/div/dl/dd/div/div/ul/li[{0}]".format(
    indexA)
a.find_by_xpath(xpath).click()

# 구매 버튼 클릭
a.find_by_xpath("//*[@id='frmView']/div/div/div[4]/div/button[1]").click()

# 동의 버튼 체크
a.find_by_xpath(
    "//*[@id='frmOrder']/div/div[2]/div[4]/div[4]/div[3]/div[2]/div/label").click()

# 결제 버튼 클릭
a.find_by_xpath(
    "//*[@id='frmOrder']/div/div[2]/div[4]/div[4]/div[3]/div[3]/button").click()
