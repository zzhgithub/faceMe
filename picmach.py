import face_recognition
import os

dir = "pic"

# Load a sample picture and learn how to recognize it.
# obama_image = face_recognition.load_image_file("pic/obama.jpg")
# obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
# biden_image = face_recognition.load_image_file("pic/biden.jpg")
# biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Load me pic
# zzh_image = face_recognition.load_image_file("pic/zzh.jpeg")
# zzh_face_encoding = face_recognition.face_encodings(zzh_image)[0]
known_face_encodings = [
]
known_face_names = [
]


def addAll(sub_dir):
    for root, dirs, files in os.walk(sub_dir):
        for f in files:
            tmp_image = face_recognition.load_image_file(os.path.join(root, f))
            tmp_encoding = face_recognition.face_encodings(tmp_image)[0]
            known_face_encodings.append(tmp_encoding)
            known_face_names.append(os.path.join(root, f))
        for d in dirs:
            sub_dir(os.path.join(root, d))


addAll(dir)

# test image
biden_image = face_recognition.load_image_file("WechatIMG1993.png")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

matches = face_recognition.compare_faces(known_face_encodings, biden_face_encoding, tolerance=0.8)
if True in matches:
    first_match_index = matches.index(True)
    name = known_face_names[first_match_index]
    print(name)
