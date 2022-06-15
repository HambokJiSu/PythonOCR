2022-06-15
OCR 프로젝트 시작

1. Python Tesseract 활용
 1) Tesseract 설치 파일 다운로드
	https://github.com/UB-Mannheim/tesseract/wiki
 2) Tesseract 설치
 	- Korean 언어파일 추가 체크
 3) Tesseract 환경변수 (Path) 추가
 	- 기본값 : C:\Program Files\Tesseract-OCR
 4) 커맨드 창에서 테스트 가능
 	- tesseract d:\adminlogo.png stdout -l eng
 5) Python용 pytesseract 모듈 설치
 	- pip install pytesseract

 2. OpenCV 모듈 추가 활용
  1) Python용 OpenCV 모듈 설치
 	- pip install opencv-python