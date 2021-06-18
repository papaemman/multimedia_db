-- RUN SIMPLE QUERIES --

SELECT * 
FROM customers


SELECT name, setting
FROM pg_settings
WHERE category = 'File Locations';

show data_directory;

-- Check all rows from actors table in images db
SELECT *
FROM public.actors;

-- Count the total number of rows for actors table
SELECT COUNT(*)
FROM public.actors;

-- Count the total actors
SELECT COUNT(DISTINCT actor)
FROM public.actors;

-- Check all unique actors in db
SELECT DISTINCT actor
FROM public.actors;

-- Count total faces per photo (image_path)
SELECT image_path, COUNT(*) as total_faces
FROM public.actors
GROUP BY image_path
ORDER BY total_faces DESC;


# Filter rows for a specific image_path
SELECT *
FROM public.actors
WHERE image_path LIKE 'data/actors/Anne Hathaway/Anne Hathaway_46.jpg'