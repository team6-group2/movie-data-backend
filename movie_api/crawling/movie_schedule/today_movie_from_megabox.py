import pandas as pd
from selenium.webdriver.common.by import By


def crawl_today_movie_from_megabox(driver):
    def theater_crawl(result, theater_name, theater_name_url):
        driver.get(theater_name_url)
        driver.implicitly_wait(2)

        # 상영시간표 누르기
        driver.find_element(By.CSS_SELECTOR,
                            '#contents > div.inner-wrap.pt40 > div.tab-list.fixed.mb40.tab-layer > ul > li:nth-child(2) > a').click()
        driver.implicitly_wait(2)

        # 12시에 들어갔을 때 아직 날짜가 안바뀐 것을 볼 수 있음 -> 다음 날로 눌러주기
        driver.find_element(By.CSS_SELECTOR,
                            '#tab02 > div.time-schedule.mb30 > div > div.date-list > div.date-area > div > button:nth-child(3)').click()

        # 영화 제목별 ex) 슈퍼마리오
        movie_elements = driver.find_elements(By.CSS_SELECTOR,
                                              '#tab02 > div.reserve.theater-list-box > div.theater-list')
        for movie_element in movie_elements:
            movie_title = movie_element.find_element(By.CSS_SELECTOR, 'div.theater-tit > p:nth-child(2) > a').text
            start_time_elements = movie_element.find_elements(By.CSS_SELECTOR,
                                                              'div.theater-type-box > div.theater-time > div.theater-time-box > table > tbody > tr > td > div > div.txt-center > a > p.time')
            for start_time_element in start_time_elements:
                # 상영 시각
                start_time = start_time_element.text
                result.append(['MEGABOX'] + [theater_name] + [''] + [movie_title] + [start_time])
                print(['MEGABOX'] + [theater_name] + [''] + [movie_title] + [start_time])

        driver.quit()

        return result

    def location_crawl(location_element):
        '''지역별 크롤링'''
        result = []
        location_element.click()
        theater_name_elements = driver.find_elements(By.CSS_SELECTOR,
                                                     'div.theater-place > ul > li.on > div > ul > li > a')

        for theater_name_element in theater_name_elements:
            # 테스트

            theater_name_url = theater_name_element.get_attribute('href')
            theater_name = theater_name_element.text

            # 지점별 상영시간 크롤링
            result = theater_crawl(result, theater_name, theater_name_url)
            print(f'{theater_name} 완료')

        print(result)
        movie_tbl = pd.DataFrame(result,
                                 columns=('theater_type', 'theater_name', 'location', 'movie_title', 'start_time'))
        return movie_tbl

    def megabox_crawl():
        print('>>> 크롤링 시작')
        main_url = 'https://www.megabox.co.kr/theater/list'
        driver.get(main_url)

        # 서울, 경기, 인천
        location_elements = driver.find_elements(By.CSS_SELECTOR, 'li > button.sel-city')
        movie_total = pd.DataFrame(
            columns=[('theater_type', str), ('theater_name', str), ('location', str), ('movie_title', str),
                     ('start_time', int)])
        # 앞 3개만 크롤링 (서울, 경기, 인천) / 0, 1, 2
        location = {0: '서울', 1: '경기/인천', 2: '경기/인천'}
        for i in range(3):
            print(f'>>> {location[i]} 시작')
            movie_tbl = location_crawl(location_elements[i])
            movie_tbl['location'] = location[i]
            print(f'>>> {location[i]} 완료')

            try:
                movie_total = pd.concat([movie_total, movie_tbl])
            except:
                movie_total = movie_tbl

        return movie_total

    return megabox_crawl()
