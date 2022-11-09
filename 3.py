from deepface import DeepFace


def face_verify(img1, img2):
    try:
        metrics = ["cosine", "euclidean", "euclidean_l2"]  # методы сравнения
        backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']  # ...

        # результат определение атрибуты лица
        res_attributes = DeepFace.analyze(img_path=img1, actions=("age", "emotion"))

        # результат сравнения двух лиц
        res_compare = DeepFace.verify(img1_path=img1, img2_path=img2, distance_metric=metrics[2])

        # распознование лица из базы данных \ ищет похожие
        df = DeepFace.find(img_path=img1, db_path="C:/Users/Centr/Desktop/images", detector_backend=backends[4]).identity
        res_list_recognition = []
        for i in range(len(df)):
            res_list_recognition.append(df[i])

        return #///

    except Exception as _ex:
        return _ex


def main():
    resu = face_verify(img1="C:/Users/Centr/Desktop/images/durov1.jpg", img2="C:/Users/Centr/Desktop/images/durov2.jpg")
    print("------------------")
    print(resu)
    pass


if __name__ == '__main__':
    main()
