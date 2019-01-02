# siftmatching

## 주요기능

1. 디자인 콘텐츠 질의 이미지가 주어지면, 높은 일치율의 근-복사 디자인 콘텐츠 5개를 검출한다.
2. 기존 이미지에서 다양한 변형을 적용한 질의 이미지를 생성한다.
3. 1000여장의 이미지 특징점들이 하나의 파일로 구성된다.



## 설치방법

### 필요한 패키지

- Augmentor==0.2.3

- opencv-python==3.4.2.16

- opencv-contrib-python==3.4.2.16

- Pillow==5.3.0

- requests==2.18.4



### 실행

#### 이미지 리사이징

feature 추출 및 검색 속도 향상을 위해 모든 이미지를 *200x200*으로 리사이징한다.

```
$ python resizer.py
```

#### 질의 이미지 생성 (Image Augmentation)

##### - 적용되는 변형 종류 (부가 설명 추가 예정)

1. 좌우대칭
2. 노이즈 추가
3. 캡션 추가
4. 로고 추가
5. 테두리 추가

```
$ python img_augmentor.py
```

#### SIFT feature 추출 (feature database 생성)

##### - feature 생성방법

1. 이미지 1장 당 파일 1개 생성
2. 모든 이미지의 feature들을 하나의 파일로 생성 (siftdump.pkl)

```
$ python indexer.py
```

#### 이미지 검출 수행 및 결과확인

수정 예정



### 실행환경

- Ubuntu 18.04

- python 3.6



mlwyberns.sogang.ac.kr(:7022)

docker attach sift_matching

/workspace