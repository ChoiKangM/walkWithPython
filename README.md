## 1교시
Pycharm, Python, Git Bash 설치  
Pycharm에 Git bash 연동

## 2교시
[`gitignore`](.gitignore) : 깃으로 파이썬 프로젝트 관리할때 사용하지 않을 파일들


```
git add
```

```
git commit -m "Message"
```

```
git config --global user.email "Your@Email.com"
```

```
git config --global user.name "Github account"
```

git 환경설정 확인
```
git config --global --list
```

```bash
git remote add origin 깃레포URL
```

```
git push origin master
```

[마크다운 작성](https://guides.github.com/features/mastering-markdown/)
>  깃헙이 가이드 제공

[Typora](https://typora.io/) : 마크다운을 편하게 작성하고 볼 수 있게 도와주는 서비스



travis ci

## 3교시
[끝말잇기](https://github.com/nwith/words)
> 깃헙에서 Collaborator를 등록해 친구와 끝말잇기 하자

## 4교시
`stirng_interpolation.py` : 문자열
1. 옛날 방식
2. `pyformat`
3. `f-string`
```python
# String Interpolation
a = '123'
new_q = f'{a}'

# 1. 옛날 방식
f'%s %s' % ('one', 'two') # => 'one two'

# 2. pyformat
'{} {}'.format('one', 'two') #=> 'one two'

# 3. f-string
a, b = 'one', 'two'
f'{a} {b}' # => 'one two'

# example
name = '홍길동'
eng_name = "Hong Gil dong"

print('안녕하세요, {1}입니다. My name is {0}'.format(name, eng_name))
print(f'안녕하세요, {name}입니다.')
```
`lotto.py` : `random` 이용한 로또뽑기

```python
import random

numbers = range(1, 46)

lotto = random.sample(numbers, 6)
print(lotto)
print(f'오늘의 행운의 로또는 {sorted(lotto)} 입나다')
```


`write_txt.py` : 파일 입력
1. `open()`
2. `with open()`  
2-1. `writelines`

`Escape Sequence`
```python
# Write File
# 1. open()
f = open('mulcam.txt', 'w') # 'w' : write, 'r' : read, 'a' : append
for i in range(10):
  f.write(f'Hello, Mulcam {i}\r\n')
f.close()

# 2. with open()
with open('mulcam.txt', 'w') as f:
  f.write('Hello, Mulcam!\n')

# 2-1. writelines
with open('mulcam.txt', 'w') as f:
  f.writelines(['1\n','2\n','3\n'])

# with: Context Manager

# \를 사용하는 문자 -> 이스케이프 시퀀스(문자)
# \n : 개행 문자
# \t : tab 문자
# \\ : 역슬레시 문자
# \' : 따옴표 문자
# \" : 쌍따옴표 문자
```
## 5교시
`read_txt.py` : 파일 출력
1. `open files()`
2. `with open()`
```python
# Read File

# 1. open files()
f = open('mulcam.txt', 'r')
all_text = f.read()
print(all_text)
f.close()

# 2. with open()
with open('mulcam.txt', 'r') as f:
  lines = f.readlines() # List
  for line in lines:
    print(line)
```

`reverse_content.py` : 파일 수정
1. `read file`
2. `reverse`
3. `write files`
```python
# 1. read file
with open('mulcam.txt', 'r') as f:
  lines = f.readlines() # list

# 2. reverse
lines.reverse()

# 3. write files
with open('mulcam.txt', 'w') as f:
  f.writelines(lines)
```
`for` : `range` 종료시 매개변수 값

```python
for i in range(10):
  print(i)

print(i) # => 9
```
## 6교시
`naver_rank.py` : `bs4` 사용한 크롤링 활용
> `requests`, `bs4`, `datetime`, `encoding`, `enumerate`
```python
import requests # pip install requests
import bs4 # pip install bs4
import datetime

html = requests.get('https://www.naver.com/').text
soup = bs4.BeautifulSoup(html, 'html.parser')

ranks = soup.select('.PM_CL_realtimeKeyword_rolling .ah_item .ah_k')
now = datetime.datetime.now()

with open('naver_rank.txt', 'w', encoding='utf-8') as f:
  f.write(f'{now} 기준 네이버 검색어 순위\n')
  for i, rank in enumerate(ranks): # [(0, 'a'), (1, 'b'), ...]
    f.write(f'{i+1}. {rank.text}\n')
```
## 7교시
`write_csv.py` : `csv` 파일 출력
1. `f-string`
2. `join()`
3. `csv`
```python
lunch = {
  '양자강': '02-557-4211',
  '김밥카페': '02-553-3101',
  '순남시래기': '02-506-0557'
}
# 1. f-string
with open('lunch.csv', 'w', encoding='utf-8') as f:
  for item in lunch.items(): # [('양자강','02-...), ...]
    f.write(f'{item[0]},{item[1]}\n')

# 2. join()
with open('lunch.csv', 'w', encoding='utf-8') as f:
  for item in lunch.items(): # [('양자강','02-...), ...]
    f.write(','.join(item)+'\n')
    # ','.join(('양자강','02-...), ('역삼동', '02-...'))
    # => 양자강,02-557-4211,역삼동,...

# 3.csv
import csv
with open('lunch.csv', 'w', encoding='utf-8') as f:
  csv_writer = csv.writer(f)
  for item in lunch.items():
    csv_writer.writerow(item)

```  
`read_csv.py` : `csv` 파일 읽기
1. `string` `split`
2. `csv`


```python
# 1. string split
with open('lunch.csv', 'r', encoding='utf-8') as f:
  lines = f.readlines()
  for line in lines:
    # '양자강,02-557-4211\n'
    # '양자강,02-557-4211'
    # ['양자강', '02-557-4211']
    print(line.strip().split(','))

# 2. csv
import csv
with open('lunch.csv', 'r', encoding='utf-8') as f:
  items = csv.reader(f) # [(..., ...),(...),(...)]
  for item in items:
    print(item)
```
## 8교시
`melon_rank.py` : melon에서 실시간 차트 가져오자
```python
import requests
import bs4
import csv

headers ={
  'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36'
}

response = requests.get('https://www.melon.com/chart/index.htm', headers=headers).text
#mobile_response = requests.get('https://m.app.melon.com/index.htm', headers=headers).text
soup = bs4.BeautifulSoup(response, 'html.parser')
songs = soup.select('#lst50')
with open('melon_rank.csv', 'w', encoding='utf-8') as f:
  for song in songs:
    rank = song.select_one('td:nth-child(2) > div > span.rank').text
    title = song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = song.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    f.write(f'{rank}위,{title},{artist}\n')
```
