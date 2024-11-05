

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


SELECT *  
FROM dsstudent.sql_join
ORDER BY id ASC;









DROP TABLE dsstudent.sql_join; 