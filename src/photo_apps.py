## Photo Applications 

# 1. Photo Retrieval
# 2. Photo Clustering

import sys
sys.path.append('.')

## Load libraries
import pickle
from tqdm import tqdm
tqdm.pandas()
from collections import Counter
import numpy as np
import pandas as pd
import psycopg2
from src.helpers import extract_photo_descriptors


## Connect to DB
con = psycopg2.connect(
    host = "localhost",
    database = "images",
    user = "postgres",
    password = "pass",
    port = 5432
)


# Cursor
cur = con.cursor()

# Load all data from actors dataset
cur.execute("SELECT * FROM actors")
df = pd.DataFrame(cur.fetchall(), columns = ["id", "face_encoding", "image_path", "actor"])
print(f"There are {len(df)} faces in actors DB")

# Decode face_encoding vector
df["face_encoding"] = df["face_encoding"].apply(lambda x: pickle.loads(x))

df.head()

# Check a single face encoding
df["face_encoding"][0]


## // Photo Retrieval //

# Distances:
# - euclidean
# - cosine
# - minkowski
# - jensenshannon
# - mahalanobis

from scipy.spatial.distance import minkowski, euclidean, cityblock, cosine, mahalanobis

# User provides a new image:


query_image = "data/query_images/nicolas_cage.jpeg"
query_image = "data/query_images/me.png"
query_image = "data/query_images/prof_tiakas.png"


from PIL import Image
im = Image.open(query_image)
im.show()

query = extract_photo_descriptors(query_image)[0]
len(query)

type(query)
query.keys()

# Calculate distances
distances = df["face_encoding"].progress_apply(lambda x: euclidean(query["face_encoding"], x))
df["distance"] = distances

# Return top-k most similar images
topk = 9
topk_actors = df.sort_values("distance")[:topk]["actor"].values.tolist()
Counter(topk_actors)

topk_image_paths = df.sort_values("distance")[:topk]["image_path"].values.tolist()
topk_image_paths
len(topk_image_paths)

## Create a collage
from PIL import Image, ImageDraw

collage = Image.new("RGBA", (1500,1500), color=(255,255,255,255))
lst = [100, 200, 300, 400, 500, 600, 700, 800, 900]

c=0
for i in range(0,1500,500):
    for j in range(0,1500,500):
        file = topk_image_paths
        file = str(topk_image_paths[c])
        photo = Image.open(file).convert("RGBA")
        photo = photo.resize((500,500))        
        
        collage.paste(photo, (i,j))
        c+=1

collage.show()

