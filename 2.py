from deepface import DeepFace


def face_verify(img1, img2):
    try:
        metrics = ["cosine", "euclidean", "euclidean_l2"]  # методы сравнения

        # результат определение атрибуты лица
        res_attributes = DeepFace.analyze(img_path=img1, actions=("age", "emotion"))

        # результат сравнения двух лиц
        res_compare = DeepFace.verify(img1_path=img1, img2_path=img2, distance_metric=metrics[1])

        return res_attributes

    except Exception as _ex:
        return _ex


def main():
    print(face_verify(img1="C:/Users/Centr/Desktop/images/durov1.jpg", img2="C:/Users/Centr/Desktop/images/durov2.jpg"))


if __name__ == '__main__':
    main()
