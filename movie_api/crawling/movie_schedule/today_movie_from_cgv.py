import re
from datetime import date

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


def today_movie_from_cgv(driver):
    def crawling_title_starttime(areacode, theaterCode, theaterName, today):
        if areacode == "01":
            city = "서울"
        elif areacode == "02":
            city = "경기도"
        elif areacode == "202":
            city = "인천"

        try:
            driver.get(f"http://www.cgv.co.kr/theaters/?areacode={areacode}&theaterCode={theaterCode}&date={today}")
            driver.implicitly_wait(10)
            district=driver.find_element(By.XPATH, "//*[@id='contents']/div[2]/div[1]/div/div[2]/div[1]/strong").text
            if areacode=="02":
                district=re.search(r"\b\w+시\b", district).group()
            else:
                district=re.search(r"\b\w+구\b", district).group()
            iframe = driver.find_element(By.ID, "ifrm_movie_time_table")
            driver.switch_to.frame(iframe)
            # print(driver.page_source)
            iframe_page_source = BeautifulSoup(driver.page_source, "html.parser")
            movies_data = iframe_page_source.select("body > div > div.sect-showtimes > ul > li")
            temp_data = []
            for movie_data in movies_data:
                movie_title = movie_data.div.find("div", "info-movie").a.text.strip()
                halls = movie_data.div.find_all("div", "type-hall")
                for hall in halls:
                    time_table = hall.select("div.info-timetable > ul > li")
                    for t in time_table:
                        start_time = t.em.text
                        if not start_time:
                            start_time = t.a.em.text

                        temp_data.append({"theater_type": "CGV", "theater_name": theaterName, "city": city, "district":district, "movie_title": movie_title, "start_time": start_time})
            return temp_data
        except Exception as error:
            print(error)
            pass

    def crawling_location_theatername():
        soup = BeautifulSoup(requests.get("http://www.cgv.co.kr/theaters/").text, "html.parser")
        script = soup.find("div", id="contents").script.string
        expression = r'"RegionCode":\s*"([^"]*)"\s*,\s*"TheaterCode":\s*"([^"]*)"\s*,\s*"TheaterName":\s*"([^"]*)'
        matches = re.findall(expression, script, re.DOTALL)
        data = []
        today = date.today().strftime("%Y%m%d")
        for match in matches:
            if match[0] in ["01", "02", "202"]:
                temp_data = crawling_title_starttime(match[0], match[1], match[2], today)
                temp_data and data.extend(temp_data)
                # time.sleep(0.5)
            else:
                break

        df = pd.DataFrame(data)
        df = df[["theater_type", "theater_name", "city", "district", "movie_title", "start_time"]]
        return df

    return crawling_location_theatername()
