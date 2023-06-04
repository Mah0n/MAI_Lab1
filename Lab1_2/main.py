import cv2
import numpy as np


def linear_color_correction(image, red_slope, red_intercept, green_slope, green_intercept, blue_slope, blue_intercept):
    """
    Применяет метод линейной цветокоррекции к изображению.

    Аргументы:
    image -- исходное изображение (в формате BGR)
    red_slope -- наклон прямой коррекции для канала Red
    red_intercept -- смещение прямой коррекции для канала Red
    green_slope -- наклон прямой коррекции для канала Green
    green_intercept -- смещение прямой коррекции для канала Green
    blue_slope -- наклон прямой коррекции для канала Blue
    blue_intercept -- смещение прямой коррекции для канала Blue

    Возвращает:
    Корректированное изображение.
    """
    # Создание пустого массива той же формы, что и исходное изображение
    corrected_image = np.zeros_like(image)

    # Применение коррекции к каждому каналу изображения
    corrected_image[:, :, 0] = np.clip(image[:, :, 0] * blue_slope + blue_intercept, 0, 255)
    corrected_image[:, :, 1] = np.clip(image[:, :, 1] * green_slope + green_intercept, 0, 255)
    corrected_image[:, :, 2] = np.clip(image[:, :, 2] * red_slope + red_intercept, 0, 255)

    return corrected_image


# Загрузка изображения
image = cv2.imread('D:/Prog/Lab1_1/dog.jpeg')

# Коэффициенты наклона и смещения для каждого канала (можно настроить по желанию)
red_slope = 1.2
red_intercept = 10
green_slope = 0.8
green_intercept = 5
blue_slope = 0.9
blue_intercept = 0

# Применение линейной цветокоррекции
corrected_image = linear_color_correction(image, red_slope, red_intercept, green_slope, green_intercept, blue_slope,
                                          blue_intercept)

# Отображение исходного и скорректированного изображений
cv2.imshow('Input Image', image)
cv2.imshow('Corrected Image', corrected_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
