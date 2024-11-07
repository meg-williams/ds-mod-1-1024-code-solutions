

SELECT * FROM log_feature;


CREATE TEMPORARY TABLE dsstudent.sql_conditional_logic
SELECT volume, 
		CASE 
			WHEN volume < 100 THEN ' low'
			WHEN volume > 500 THEN 'high' /* low and large do not go to gether */
			ELSE 'medium'
		END volume_1
FROM log_feature; 

SELECT volume_1, COUNT(volume_1) 'value_counts'
FROM dsstudent.sql_conditional_logic
GROUP BY volume_1;

SELECT * FROM employee;

SELECT EmployeeNumber
FROM employee;

CREATE TEMPORARY TABLE dsstudent.sql_c
SELECT volume, 
		CASE 
			WHEN volume < 100 THEN ' low'
			WHEN volume > 500 THEN 'high' /* low and large do not go to gether */
			ELSE 'medium'
		END volume_1
FROM log_feature; 

SELECT EmployeeNumber, 
		HourlyRate,
		CASE 
			WHEN HourlyRate >= 80 THEN 'high hourly rate'
			WHEN HourlyRate < 40 THEN 'low hourly rate'
			ELSE 'medium hourly rate'
		END HourlyRate_1
FROM employee;

SELECT Gender, 
		CASE 
			WHEN Gender = 'Female' THEN '0'
			Else '1'
		END Gender_1
FROM employee;
		

