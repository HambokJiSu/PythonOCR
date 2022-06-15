from PIL import Image
import pytesseract
import cv2

#	1) pytesseract 기본 옵션으로 OCR 확인
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
config = ("-l kor+eng --oem 3 --psm 11")
#imgPath = r'img\adminlogo.png'
imgPath = r'img\sourcecode.png'

#	현재 가능한 언어 목록 List
#print(pytesseract.get_languages(config=''))

#	이미지를 Text로
#print(pytesseract.image_to_string(Image.open(imgPath), config=config))

#	글자별 좌표값
#print(pytesseract.image_to_boxes(Image.open(imgPath), config=config))

#	단어별 Data(넓이, 높이, 좌표 등)
#print(pytesseract.image_to_data(Image.open(imgPath), config=config))

#	글자 검색이 가능한 PDF로 변환
# pdf = pytesseract.image_to_pdf_or_hocr(Image.open(imgPath), config=config, extension="pdf")
# with open("test.pdf", "w+b") as f:
# 	f.write(pdf)

#img_cv = cv2.imread(imgPath)
#img_rgb = cv2.cvtColor(img_cv, cv2.IMREAD_GRAYSCALE)
img_cv = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)	#	회색조로 이미지 저장 후 OCR
cv2.imshow("image1", img_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print(pytesseract.image_to_string(img_rgb, config=config))