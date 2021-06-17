-- RUN SIMPLE QUERIES --

SELECT * 
FROM customers


SELECT name, setting
FROM pg_settings
WHERE category = 'File Locations';


show data_directory;
