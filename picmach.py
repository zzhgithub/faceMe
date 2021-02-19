import face_recognition

# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
biden_image = face_recognition.load_image_file("biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Load me pic
zzh_image = face_recognition.load_image_file("zzh.jpeg")
zzh_face_encoding = face_recognition.face_encodings(zzh_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding,
    zzh_face_encoding
]
known_face_names = [
    "Barack Obama",
    "Joe Biden",
    "Zhou ZiHao"
]


# test image
biden_image = face_recognition.load_image_file("biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

matches = face_recognition.compare_faces(known_face_encodings, biden_face_encoding)
if True in matches:
    first_match_index = matches.index(True)
    name = known_face_names[first_match_index]
    print(name)
