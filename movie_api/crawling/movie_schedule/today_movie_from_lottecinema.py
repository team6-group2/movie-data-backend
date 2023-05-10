import time
import requests
from datetime import date
import pandas as pd
from selenium.webdriver.common.by import By


def today_movie_from_lottecinema(driver):
    def getCinemaId():
        cinema_id_dict = {}

        driver.get("https://www.lottecinema.co.kr/NLCHS/Ticketing/Schedule")
        driver.implicitly_wait(10)

        cinema_id = []
        for i in range(1, 25):  # (1~24) 서울 영화관 고유 아이디 추출
            element = driver.find_element(By.XPATH,
                                          '//*[@id="nav"]/ul/li[3]/div/ul/li[2]/div/ul/li[{}]/a'.format(i))

            href = element.get_attribute("href")  # href 속성 값을 가져옵니다.
            cinema_id.append(href[-4:])  # href 값을 출력합니다.

        cinema_id_dict["서울"] = cinema_id

        cinema_id = []
        for i in range(1, 48):  # (1~48) 경기/인천 영화관 고유 아이디 추출
            element = driver.find_element(By.XPATH,
                                          '//*[@id="nav"]/ul/li[3]/div/ul/li[3]/div/ul/li[{}]/a'.format(i))

            href = element.get_attribute("href")
            cinema_id.append(href[-4:])

            cinema_id_dict["경기/인천"] = cinema_id

        return cinema_id_dict

    def getMovieInfo():
        today = date.today()
        today_date = today.strftime("%Y-%m-%d")

        url = "https://www.lottecinema.co.kr/LCWS/Ticketing/TicketingData.aspx"
        citys = {"서울": "0001", "경기/인천": "0002"}
        cinema_id_dict = getCinemaId()
        all_movie = []

        for city in citys:
            cinema_id_list = cinema_id_dict[city]  # ['1013', '9094', '9010', '1004', ...
            city_id = citys[city]  # 0001
            for cinema_id in cinema_id_list:
                time.sleep(1)  # 요청 전에 딜레이를 줌
                dic = {"MethodName": "GetPlaySequence",
                       "channelType": "HO",
                       "osType": "",
                       "osVersion": "",
                       "playDate": today_date,
                       "cinemaID": "1|{}|{}".format(city_id, cinema_id),
                       "representationMovieCode": ""
                       }
                parameters = {"paramList": str(dic)}
                response = requests.post(url, data=parameters).json()
                movies_response = response['PlaySeqs']['Items']

                for move_res in movies_response:
                    move_data = {"theater_type": "LOTTE CINEMA", "theater_name": move_res['CinemaNameKR'],
                                 "city": city, "movie_title": move_res['MovieNameKR'],
                                 "start_time": move_res['StartTime']}

                    all_movie.append(move_data)

        df = pd.DataFrame(all_movie, columns=["theater_type", "theater_name", "city", "movie_title", "start_time"])
        return df

    return getMovieInfo()
