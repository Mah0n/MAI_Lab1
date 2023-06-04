import numpy as np
import cv2


# Создаем пустую функцию
def nothing(args):
    pass


# Создаем окно для отображения результата и бегунки
cv2.namedWindow("setup")
cv2.createTrackbar("T", "setup", 0, 100, nothing)  # Диапазон значений T изменен на [0, 100] для лучшей настройки

fn = "dog.jpeg"  # Путь к файлу с картинкой
img = cv2.imread(fn)  # Загрузка изображения
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

while True:
    T = cv2.getTrackbarPos('T', 'setup')

    # Применяем степенное преобразование
    img_new = np.power(imgray, T / 100.0).astype(
        np.uint8)  # Нормализация T к диапазону [0, 1] и приведение типа к uint8

    cv2.imshow('img', img_new)

    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
