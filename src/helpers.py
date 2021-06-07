## Helper Functions 
import face_recognition

def extract_photo_descriptors(image_path):

    # Create an encoding of facial features that can be compared to other faces
    picture = face_recognition.load_image_file(file=image_path)
    
    res = []
    for face_encoding in face_recognition.face_encodings(picture):
        res.append({"face_encoding":face_encoding,
                    "image_path": image_path, 
                    "actor":image_path.split("/")[2]})
    
    return res