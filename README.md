# Information Retrieval system

## Information Retrieval System, on a Multimedia Database (images) using PostgreSQL and Python.

<img src="assets/python_postgresql.gif">

## System Architecture

<img src="assets/System’s Architecture diagram.png">

### Compenents

1. Web Scraper (Selenium: <https://selenium-python.readthedocs.io/>)

2. Face Recognition: <https://github.com/ageitgey/face_recognition>  
    The world's simplest facial recognition api for Python and the command line

3. psycopg2: <https://www.psycopg.org/>  
    PostgreSQL database adapter for the Python programming language

---
<br>

## Information Retrieval System

Input Image:

Output Images:

Check more examples here: <data/query_images>

<br>

---

<br>

## Project's Structure

```bash
.
├── assets
├── data
├── docs
├── LICENSE
├── notebooks
├── output
├── README.md
└── src
```

---

## Data 

```bash
├── data
│   ├── actors
│   │   ├── Alec Baldwin
│   │   ├── Al Pacino
│   │   ├── Amy Adams
│   │   ├── Angelina Jolie
│   │   ├── Anne Hathaway
...
```

<img src="output/images1.png">

---
<br>

## PostgreSQL Database and pgAdmin4

<img src="output/sql-queries-pgAdmin4-screenshots/pgAdmin4.png">

---
<br>

## Face recognistion Tasks

### 1. Face detection

<img src="assets/face_detection.png">

### 2. Face crop

<img src="assets/face_crop.png">

### 2. Face encoding

<img src="assets/face_recognition_ebmeddings.png">
