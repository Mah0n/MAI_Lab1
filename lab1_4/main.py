import numpy as np
import cv2

# Создаем пустую функцию
def nothing(args):
    pass

# Создаем окно для отображения результата и бегунки
cv2.namedWindow("setup")
cv2.createTrackbar("T", "setup", 0, 255, nothing)
cv2.createTrackbar("C", "setup", 0, 255, nothing)  # Добавлен бегунок для параметра C

fn = "dog.jpeg"  # Путь к файлу с картинкой
img = cv2.imread(fn)  # Загрузка изображения
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

while True:
    T = cv2.getTrackbarPos('T', 'setup')
    C = cv2.getTrackbarPos('C', 'setup') - 128  # Значение C смещается на -128 для использования в cv2.adaptiveThreshold()

    # Применяем адаптивную бинаризацию
    img_new = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 2* T +3, C)

    cv2.imshow('img', img_new)

    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
