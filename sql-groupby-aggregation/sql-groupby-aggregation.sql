

CREATE TEMPORARY TABLE dsstudent.sql_join
SELECT t.id, t.location, t.fault_severity, et.event_type, st.severity_type,  rt.resource_type, lf.log_feature, lf.volume
FROM train t 
LEFT OUTER JOIN severity_type st  
ON t.id = st.id
LEFT OUTER JOIN resource_type rt 
ON rt.id = t.id
LEFT OUTER JOIN log_feature lf 
ON lf.id = t.id
LEFT OUTER JOIN event_type et  
ON et.id = t.id;


SELECT location, COUNT(DISTINCT(event_type)) num_unique_event_type
FROM dsstudent.sql_join
GROUP BY location
ORDER BY location ASC;

SELECT location, SUM(volume) total_volume
FROM dsstudent.sql_join
GROUP BY location
ORDER BY total_volume DESC
LIMIT 3;

SELECT fault_severity, COUNT(DISTINCT(location)) num_of_unique_locations
FROM train t
GROUP BY fault_severity
ORDER BY fault_severity ASC;


SELECT fault_severity, COUNT(DISTINCT(location)) num_of_unique_locations
FROM train t
GROUP BY fault_severity
HAVING fault_severity > 1
ORDER BY fault_severity ASC;

SELECT Attrition, MIN(Age) min_age, MAX(Age) max_age, AVG(Age) avg_age
FROM employee e 
GROUP BY Attrition;

SELECT Attrition, Department, COUNT(*) as num_quantity
FROM employee e
WHERE Attrition IS NOT NULL
GROUP BY Attrition, Department
ORDER BY Attrition; 

SELECT Attrition, Department, COUNT(*) as num_quantity
FROM employee e
WHERE Attrition IS NOT NULL 
GROUP BY Attrition, Department
HAVING COUNT(*) > 100
ORDER BY Attrition; 











DROP TABLE dsstudent.sql_join; 