from selenium import webdriver
import chromedriver_autoinstaller
import os
from bs4 import BeautifulSoup

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'./{chrome_ver}/chromedriver.exe'
if os.path.exists(driver_path):
   pass
else:
    chromedriver_autoinstaller.install(True)

driver = webdriver.Chrome(driver_path)
def get_tier_champion(tier, position):
    uri = f"https://www.op.gg/champions?region=global&tier={tier}&position={position}"
    champion_list = []
    driver.get(uri)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    for champions in soup.find(class_='css-jgru8w e1oulx2j7').find('tbody').find_all('tr'):
        count = 0
        champion_object={}
        for champion in champions.find_all("td"):
            if count == 0:
                pass
            else:
                if count == 1:
                    champion_object["name"] = champion.text
                if count == 2:
                    if champion.text == '0':
                        champion_object["tier"] = "op"
                    else:
                        champion_object["tier"] = champion.text
                if count == 3:
                    champion_object["winper"] = champion.text
                if count == 4:
                    champion_object["pickper"] = champion.text
                if count == 5:
                    champion_object["banper"] = champion.text
            count += 1
        champion_list.append(champion_object)
    return champion_list

champion_tier = get_tier_champion("platinum_plus", "top")

def get_user_champion_info(champion_name):
    for tiers in champion_tier:
        if tiers['name'] == champion_name:
            print(champion_name + "는 " + tiers["tier"] + "티어 챔피언 입니다.\n\n" + champion_name +"에 대한 세부정보\n\n" + "승률: " + tiers['winper'] + "\n픽률: " + tiers["pickper"] + "\n밴률: " + tiers["banper"])
get_user_champion_info("자야")