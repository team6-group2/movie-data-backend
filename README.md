# 영화 상영 정보 웹 서비스

<br></br>
## 프로젝트 개요
### 1. 내용  
영화관 3사(CGV, MEGABOC, LOTTECINEMA) 상영 시간표 데이터를 매일 자정에 스크래핑해서, 상영 정보를 일일히 찾아보지 않아도 특정 지역의 모든 영화 상영 정보를 한눈에 볼 수 있습니다.

![screen-recording](https://github.com/team6-group2/movie-data-backend/assets/65884076/65c9acbb-d341-4a83-9d1b-b7f5475e2436)


### 2. 프로젝트 기간 : 2023.05.01 ~ 2023.05.05
​
### 3. 참여자 정보 및 각 역할
|이름|역할|
|:---:|:---:|
|김동욱|롯데시네마 크롤링, 장고|
|김영준|다음 영화 정보 크롤링, 장고 스케줄러|
|박다혜|메가박스 크롤링, 장고|
|조민동|CGV 크롤링, Docker환경에 DB 구축|  
​
### 4. 활용 기술 및 프레임워크
|데이터 크롤링|selenium, BeautifulSoup|
|프론트엔드|Django, Bootstrap4|
|백엔드|Django, postgresql|
|데브옵스|Docker, git, Django Scheduler|   
<br></br>

## 프로젝트 설치 및 실행방법
​
​
1. 프로젝트 깃 레포지토리 클론
   ```sh
   $ git clone https://github.com/team6-group2/movie-data-backend.git 
   ```
2. docker containter 실행
   ```sh
   $ docker-compose up -d --build
   ```
3. djangojob 테이블에 데이터 추가
   ```sh
   $ docker-compose exec db psql -U postgres postgres
   
   psql (13.10 (Debian 13.10-1.pgdg110+1))
   Type "help" for help.
   
   postgres=# INSERT INTO django_apscheduler_djangojob(id, job_state) VALUES('111', '');
   ```
4. http://localhost:8000/movie/ 접속
