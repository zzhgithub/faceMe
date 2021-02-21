import face_recognition
import os
from multiprocessing import Pool

dir = "pic"

known_face_encodings = [
]
known_face_names = [
]


def dd(v):
    deal(v[0], v[1])


def deal(root, f):
    tmp_image = face_recognition.load_image_file(os.path.join(root, f))
    tmp_me = face_recognition.face_encodings(tmp_image)
    if len(tmp_me) > 0:
        known_face_encodings.append(tmp_me[0])
        known_face_names.append(os.path.join(root, f))


def addRoot(list, root):
    ret = []
    for v in list:
        ret.append((root, v))
    return ret


def addAll(sub_dir):
    for root, dirs, files in os.walk(sub_dir):
        pool = Pool()
        pool.map(dd, addRoot(files, root))
        pool.close()
        pool.join()

        for d in dirs:
            addAll(os.path.join(root, d))


if __name__ == '__main__':
    addAll(dir)
    # test image
    biden_image = face_recognition.load_image_file("WechatIMG1993.png")
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

    matches = face_recognition.compare_faces(known_face_encodings, biden_face_encoding, tolerance=0.6)
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
        print(name)
