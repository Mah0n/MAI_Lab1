import cv2
import numpy as np

def static_color_correction(image, red_gain, green_gain, blue_gain):
    """
    Применяет метод статической цветокоррекции к изображению.

    Аргументы:
    image -- исходное изображение (в формате BGR)
    red_gain -- коэффициент коррекции для канала Red
    green_gain -- коэффициент коррекции для канала Green
    blue_gain -- коэффициент коррекции для канала Blue

    Возвращает:
    Корректированное изображение.
    """
    # Создание пустого массива той же формы, что и исходное изображение
    corrected_image = np.zeros_like(image)

    # Применение коррекции к каждому каналу изображения
    corrected_image[:, :, 0] = np.clip(image[:, :, 0] * blue_gain, 0, 255)
    corrected_image[:, :, 1] = np.clip(image[:, :, 1] * green_gain, 0, 255)
    corrected_image[:, :, 2] = np.clip(image[:, :, 2] * red_gain, 0, 255)

    return corrected_image


# Загрузка изображения
image = cv2.imread('dog.jpeg')

# Коэффициенты коррекции для каждого канала (можно настроить по желанию)
red_gain = 1.2
green_gain = 0.8
blue_gain = 0.9

# Применение статической цветокоррекции
corrected_image = static_color_correction(image, red_gain, green_gain, blue_gain)

# Отображение исходного и скорректированного изображений
cv2.imshow('Input Image', image)
cv2.imshow('Corrected Image', corrected_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
