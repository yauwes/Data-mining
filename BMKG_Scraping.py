from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import json

def scraper(url):
    print("lagi scraping nih, sabar ya bos")

    try:
        options = Options()
        options.add_argument('-headless')
        driver = webdriver.Firefox(options=options)
        driver.get(url)
        
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")


        cuaca = []
        for cuaca_ in soup.find_all("div", class_="service-block bg-cuaca cerah-berawan-siang"):
            nama_kota = cuaca_.find("h2",class_= "kota").text     
            deskripsi_suhu = cuaca_.find("p",attrs = {'class': None}).text   
            suhu_kota = cuaca_.find('h2',class_='heading-md').text 

            cuaca.append(
                    {
                        "Nama Kota" : nama_kota,
                        "Langit" : deskripsi_suhu,
                        "Suhu" : suhu_kota
                        
                    }
                )    
            
        return cuaca


    except Exception as e :
        print("error", e)

        driver.quit()


if __name__ == '__main__':
    # Define the URL
    url = "https://www.bmkg.go.id/"

    data = scraper(url)
    with open('BMKG_scraping.json','w') as json_file:
        json.dump(data, json_file, indent=4)
    