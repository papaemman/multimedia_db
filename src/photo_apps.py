#################################################
#                                               #
#   Photo Retrieval based on Face similarity    #
#                                               #
#################################################

## Append pat to Python path
import sys
sys.path.append('.')

## Load libraries
import pickle
from tqdm import tqdm
tqdm.pandas()
from collections import Counter
from PIL import Image, ImageDraw
import numpy as np
import pandas as pd
import psycopg2
from src.helpers import extract_photo_descriptors, create_collage


## Connect to PostgreSQL DB
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

# Check Dataframe
df.head()

# Check a single face encoding
df["face_encoding"][0]


## Identify Similar Images based on different distance measures

# Distances:
# 1. minkowski 
# 2. euclidean 
# 3. cityblock (manhattan)
# 4. cosine
# 5 mahalanobis

from scipy.spatial.distance import minkowski, euclidean, cityblock, cosine, mahalanobis


## User provides a new image ():

query_image = "data/query_images/arnold.jpg"
query_image = "data/query_images/jennifer_aniston.jpeg"
query_image = "data/query_images/nicolas_cage.jpeg"
query_image = "data/query_images/me.png"

# Show image
im = Image.open(query_image)
im.show()

# Extract descriptor vector from face in image
query = extract_photo_descriptors(query_image)[0]

type(query)
query.keys()

## Calculate distances
distances = df["face_encoding"].progress_apply(lambda x: euclidean(query["face_encoding"], x))
df["distance"] = distances

# Return top-k (6, 12, 20) most similar images
topk = 12
topk_actors = df.sort_values("distance")[:topk]["actor"].values.tolist()
Counter(topk_actors)

# Extract topk images paths
topk_image_paths = df.sort_values("distance")[:topk]["image_path"].values.tolist()
topk_image_paths

# Create collage of returned images
create_collage(550, 400, topk_image_paths, k = topk)



