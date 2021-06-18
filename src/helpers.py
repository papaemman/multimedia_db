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

## Create a collage (helper function)

def create_collage(width, height, listofimages, k):
    cols = 3
    rows = int(k/cols)
    thumbnail_width = width//cols
    thumbnail_height = height//rows
    size = thumbnail_width, thumbnail_height
    new_im = Image.new('RGB', (width, height))
    ims = []
    for p in listofimages:
        im = Image.open(p)
        im.thumbnail(size)
        ims.append(im)
    i = 0
    x = 0
    y = 0
    for col in range(cols):
        for row in range(rows):
            print(i, x, y)
            new_im.paste(ims[i], (x, y))
            i += 1
            y += thumbnail_height
        x += thumbnail_width
        y = 0

    new_im.show()