/* SQL common clauses */

SELECT id, log_feature log, volume vol
FROM log_feature lf;

SELECT id, resource_type
FROM resource_type rt
ORDER BY 1,2 ASC
LIMIT 5;

SELECT id, resource_type
FROM resource_type rt 
ORDER BY 1 DESC 
LIMIT 5; 


SELECT id, resource_type
FROM resource_type rt 
ORDER BY 1 ASC, 2 DESC
LIMIT 5; 


SELECT COUNT(*)numbers_row, COUNT(DISTINCT(id)) id_unique, COUNT(DISTINCT(severity_type)) severity_type_unique  
FROM severity_type st;

SELECT id, log_feature, volume 
FROM log_feature lf 
WHERE (volume BETWEEN 100 AND 300) AND log_feature = 'feature 201'
ORDER BY volume;



















