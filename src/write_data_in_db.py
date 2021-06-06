## ---- Write data in PostgreSQL database ---- 

# // Steps: //
# 1. Find all paths
# 2. Extract photo descriptor vectors for every face
# 3. Write in Postgresql db


## Load modules
import sys
sys.path.append('.')

import os
import pickle
from tqdm import tqdm
import pandas as pd
import numpy as np
import psycopg2
import psycopg2.extras
import face_recognition
from src.helpers import extract_photo_descriptors


## Find all paths
paths_ls = []

for dirname, _, filenames in os.walk('data/actors/'):
    for filename in filenames:
            paths_ls.append(os.path.join(dirname, filename))

print(len(paths_ls))


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

# Create new Table in images database
cur.execute(
    """
    CREATE TABLE actors (
        id SERIAL PRIMARY KEY,
        face_encoding BYTEA,
        image_path VARCHAR,
        actor VARCHAR
    )
    """)

# Rollback after invalid transaction
# cur.execute("ROLLBACK")

for image_path in tqdm(paths_ls):

    try:
        faces_info = extract_photo_descriptors(image_path)
        # print(f"There are {len(faces_info)} faces in this photo")

        for i in range(len(faces_info)):
            cur.execute(
                """
                INSERT INTO actors(face_encoding, image_path, actor)
                VALUES (%s, %s,  %s)
                """, 
                (pickle.dumps(faces_info[i]['face_encoding']), faces_info[i]['image_path'], faces_info[i]['actor'])
            )
    except:
        pass
    
# Commit the transaction
con.commit()

# Close the cursor
cur.close()

# Close the connection
con.close()