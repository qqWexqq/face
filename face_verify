from deepface import DeepFace

choice_backend = 0
choice_metric = 2
backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface',
            'mediapipe']  # opencv или ssd - скорость \ retinaface и mtcnn - качество
metrics = ["cosine", "euclidean", "euclidean_l2"]  # методы сравнения

def face_analyze(img1):
    try:
        res_attributes = DeepFace.analyze(img_path=img1, actions=("age", "emotion"), detector_backend=backends[0])

        return res_attributes

    except Exception as _ex:
        return _ex


def get_similar_faces(img1, img2):
    try:
        # результат сравнения двух лиц
        res_compare = DeepFace.verify(img1_path=img1, img2_path=img2, distance_metric=metrics[choice_metric],
                                      detector_backend=backends[choice_backend])
        return res_compare
    except Exception as _ex:
        return _ex


def find_face_in_base(img1):
    # распознование лица из базы данных \ ищет похожие
    df = DeepFace.find(img_path=img1, db_path="images",
                       detector_backend=backends[choice_backend]).identity
    res_list_recognition = []
    for i in range(len(df)):
        res_list_recognition.append(df[i])
    return res_list_recognition
