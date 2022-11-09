from deepface import DeepFace

choice_backend = 0
choice_metric = 2
backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface',
            'mediapipe']  # opencv или ssd - скорость \ retinaface и mtcnn - качество
metrics = ["cosine", "euclidean", "euclidean_l2"]  # методы сравнения


def get_attributes(img1):
    # результат определение атрибуты лица
    res_attributes = DeepFace.analyze(img_path=img1, actions=("age", "emotion"),
                                      detector_backend=backends[choice_backend])
    return res_attributes


def get_is_similar(img1, img2):
    # результат сравнения двух лиц
    res_compare = DeepFace.verify(img1_path=img1, img2_path=img2, distance_metric=metrics[choice_metric],
                                  detector_backend=backends[choice_backend])
    return res_compare


def get_similars(img1):
    # распознование лица из базы данных \ ищет похожие
    df = DeepFace.find(img_path=img1, db_path="images",
                       detector_backend=backends[choice_backend]).identity
    res_list_recognition = []
    for i in range(len(df)):
        res_list_recognition.append(df[i])
    return res_list_recognition


def main():
    #res1 = get_attributes("images/durov1.jpg")
    #res2 = get_is_similar("images/durov1.jpg", "images/durov2.jpg")
    #res3 = get_similars("images/durov1.jpg")
    print("------------------")
    print(res)
    pass


if __name__ == '__main__':
    main()
