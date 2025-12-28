-- 1. Get all the predictions
SELECT * FROM cardiodiagnosis

-- 2. Get all the predictions for the day.
SELECT * FROM cardiodiagnosis
WHERE date = CURRENT_DATE

--3. Get all the predictions for the day and sort them based on the highest probability percentage at
--the top
SELECT *
FROM cardiodiagnosis AS cd
WHERE DATE(cd.date) = 'date_value'
ORDER BY cd.cardioarrestdetected DESC

--4. Get all the unique cities.
SELECT DISTINCT ai.city AS Unique_Cities
FROM addressinfo AS ai

--5. Get all the members who are from a city 'Burgos'.
SELECT mi.firstname AS "Firstname", mi.lastname AS "Lastname",ai.city AS "City"
FROM memberinfo AS mi 
JOIN addressinfo AS ai ON mi.member_id = ai.memberinfo_member_id
WHERE ai.city = 'Burgos'

 --6. Get all the members who are from 'Flora' city
 SELECT mi.firstname AS "Firstname", mi.lastname AS "Lastname",ai.city AS "City"
FROM memberinfo AS mi 
JOIN addressinfo AS ai ON mi.member_id = ai.memberinfo_member_id
WHERE ai.city = 'Flora'

--7. Get the total number of blood tests done for Aisha
SELECT COUNT(*) AS "Number of bloodtests"
FROM memberinfo AS mi
JOIN cardiodiagnosis AS cd ON mi.member_id = cd.memberinfo_member_id 
JOIN bloodtest AS bt ON cd.cardio_id = bt.cardiodiagnosis_cardio_id
WHERE mi.firstname = 'aisha'
GROUP BY mi.firstname

--8. Get the X-ray details of Ajay whose cardio test was done on 26th of Jan 201
SELECT xr.*
FROM xray AS xr
JOIN ecgreport AS er USING(cardiodiagnosis_cardio_id)
JOIN cardiodiagnosis AS cd ON er.cardiodiagnosis_cardio_id = cd.cardio_id
JOIN memberinfo AS mi ON cd.memberinfo_member_id = mi.member_id
WHERE mi.firstname = 'ajay' AND DATE(er.date)='26-01-2019'

--9. Get all the members who are from cities 'Burgos' and 'Flora'.
SELECT mi.firstname AS "Firstname", mi.lastname AS "Lastname",ai.city AS "City"
FROM memberinfo AS mi 
JOIN addressinfo AS ai ON mi.member_id = ai.memberinfo_member_id
WHERE ai.city = 'Flora' OR ai.city = 'Burgos'

--10. Get the total number of blood tests done for Aberson.
SELECT COUNT(*) AS "Number of Blood Tests"
FROM bloodtest AS bt
JOIN cardiodiagnosis AS cd ON cd.cardio_id = bt.cardiodiagnosis_cardio_id
JOIN memberinfo AS mi ON mi.member_id = cd.memberinfo_member_id
WHERE mi.lastname = 'aberson'

--11. Get all address details for member ID M303
SELECT *
FROM addressinfo AS ai
WHERE ai.memberinfo_member_id = 'M303'

--12. Get all X-ray details for cardio ID CID122.
SELECT *
FROM xray AS xr
WHERE xr.cardiodiagnosis_cardio_id = 'cid122'

--13. Get all symptom details whose cardio ID is CID250 and CID300.
SELECT *
FROM symptom as sy
WHERE sy.cardiodiagnosis_cardio_id IN ('cid250','cid300')

--14. Get all symptom details for the month of July and year 2019
SELECT *
FROM symptom as sy
WHERE DATE(sy.date) BETWEEN '01-07-2019' AND '31-07-2019'

-- 15. Get X-ray details for the member with the last name "Dailley".
SELECT xr.*
FROM xray xr
JOIN cardiodiagnosis cd ON xr.cardiodiagnosis_cardio_id = cd.cardio_id
JOIN memberinfo mi ON cd.memberinfo_member_id = mi.member_id
WHERE mi.lastname = 'dailley';

--16. Get wearable device data details for cardio IDs between CID100 and CID200
SELECT *
FROM wearabledevicedata as wd 
WHERE wd.cardiodiagnosis_cardio_id BETWEEN 'cid100' AND 'cid200';

-- 17. Display all cardio diagnosis details where the first name starts with the letter "A".
SELECT cd.*,mi.firstname
FROM cardiodiagnosis cd
JOIN memberinfo mi ON cd.memberinfo_member_id = mi.member_id
WHERE mi.firstname LIKE 'a%';

-- 18. Display all cardio diagnosis details where the first name starts with "A" and ends with "A".
SELECT cd.*,mi.firstname
FROM cardiodiagnosis cd
JOIN memberinfo mi ON cd.memberinfo_member_id = mi.member_id
WHERE mi.firstname LIKE 'a%a';

-- 19. Get all the members from the MemberInfo table.
SELECT * FROM memberinfo;

-- 20. Get all the addresses of members.
SELECT * FROM addressinfo;

-- 21. Get a list of wearable device information.
SELECT * FROM wearabledevicedata;

-- 22. Get a list of all the blood tests done.
SELECT * FROM bloodtest;

-- 23. Get a list of members who are aged greater than 50.
SELECT * FROM memberinfo 
WHERE age > 50;

-- 24. Get a list of addresses for the city 'Flora'.
SELECT * FROM addressinfo 
WHERE city = 'Flora';

-- 25. Get a list of all unique states.
SELECT DISTINCT state FROM addressinfo;

-- 26. Get the total number of members in the database.
SELECT COUNT(*) AS total_members FROM memberinfo;

-- 27. Get the total number of blood tests done.
SELECT COUNT(*) AS total_blood_tests FROM bloodtest;

--28. Get the average cholesterol level for members.
SELECT AVG(serumcholesterol) AS avg_cholesterol FROM bloodtest;

-- 29. Get the maximum peak value in symptoms.
SELECT MAX(oldpeak) AS max_peak FROM symptom;

-- 30. Get the list of tests done between January 1, 2015, and January 31, 2019.
SELECT * FROM bloodtest
WHERE date BETWEEN '2015-01-01' AND '2019-01-31';

-- 31. Get the number of males and females aged between 50 and 60.
SELECT gender,COUNT(*) AS "Count of people aged between 50-60"
FROM memberinfo 
WHERE age BETWEEN 50 AND 60
GROUP BY gender;


-- 32. Get the list of tests where blood pressure is between 100 and 200.
SELECT * FROM bloodtest as bt
WHERE bt.bloodpressure BETWEEN 100 AND 200;

-- 33. Get the list of symptoms diagnosed for patients.
SELECT * FROM symptom;

-- 34. Get the average age of patients in the database.
SELECT AVG(age) AS avg_age FROM memberinfo;

--35. Get the total number of cities for each state available.
SELECT state,COUNT(*) AS "Number of cities"
FROM addressinfo AS ai
GROUP BY ai.state

--36. Get the number of patients in the following age groups:
--o 10-20
--o 20-30
--o 30-40
--o 40-50
--o 50-60
--o 60-70
SELECT
    CASE
        WHEN age >= 10 AND age < 20 THEN '10–20'
        WHEN age >= 20 AND age < 30 THEN '20–30'
        WHEN age >= 30 AND age < 40 THEN '30–40'
        WHEN age >= 40 AND age < 50 THEN '40–50'
        WHEN age >= 50 AND age < 60 THEN '50–60'
        WHEN age >= 60 AND age < 70 THEN '60–70'
    END AS age_group,
    COUNT(*) AS patient_count
FROM memberinfo AS mi
WHERE age >= 10 AND age < 70
GROUP BY age_group
ORDER BY age_group;


--37. Get the list of members and their addresses.
SELECT mi.*, ai.address_id, ai.city, ai.state, ai.country, ai.pincode
FROM memberinfo mi
JOIN addressinfo ai ON mi.member_id = ai.memberinfo_member_id
ORDER BY mi.member_id

--38. Get the list of members and their cardio history.
SELECT mi.*, cd.*
FROM memberinfo mi
JOIN cardiodiagnosis cd ON mi.member_id = cd.memberinfo_member_id;

--39. Get the list of members and their disease.
SELECT mi.*, dd.*
FROM memberinfo mi
JOIN cardiodiagnosis cd ON mi.member_id = cd.memberinfo_member_id
JOIN diseasedetail dd ON cd.cardio_id = dd.cardiodiagnosis_cardio_id;

--40. Get the list of females diagnosed with a heart attack.
SELECT  mi.*
FROM memberinfo mi
JOIN cardiodiagnosis cd ON mi.member_id = cd.memberinfo_member_id
WHERE mi.gender = '0' AND cd.cardioarrestdetected = 1;

--41. Get the list of female members and their cardio information for those aged above 50
SELECT mi.*, cd.*
FROM memberinfo mi
JOIN cardiodiagnosis cd ON mi.member_id = cd.memberinfo_member_id
WHERE mi.gender = '0' AND mi.age > 50;

--42. Get the list of males who have blood pressure > 140 and have not had a heart attack.
SELECT  mi.*
FROM memberinfo mi
JOIN cardiodiagnosis cd ON mi.member_id = cd.memberinfo_member_id
JOIN bloodtest bt ON cd.cardio_id = bt.cardiodiagnosis_cardio_id
WHERE mi.gender = '1' 
  AND bt.bloodpressure > 140 
  AND cd.cardioarrestdetected = 0;

  --43. Get the list of members who had a heart attack from the state "Mountain Province".
  SELECT  mi.*
FROM memberinfo mi
JOIN addressinfo ai ON mi.member_id = ai.memberinfo_member_id
JOIN cardiodiagnosis cd ON mi.member_id = cd.memberinfo_member_id
WHERE ai.state = 'Mountain Province' AND cd.cardioarrestdetected = 1;

--44. Get the list of male members and their diseases with symptoms for those aged less than 40
SELECT mi.*, dd.* ,s.*
FROM memberinfo mi
JOIN cardiodiagnosis cd ON mi.member_id = cd.memberinfo_member_id
JOIN diseasedetail dd ON cd.cardio_id = dd.cardiodiagnosis_cardio_id
JOIN symptom s ON cd.cardio_id = s.cardiodiagnosis_cardio_id
WHERE mi.gender = '1' AND mi.age < 40;


--45. Get the count of members from "Mountain Province" aged between 50 and 60
SELECT COUNT( mi.member_id) AS member_count
FROM memberinfo mi
JOIN addressinfo ai ON mi.member_id = ai.memberinfo_member_id
WHERE ai.state = 'Mountain Province' AND mi.age BETWEEN 50 AND 60;

--46. Get the count of male and female members who have blood pressure > 140 and have been
--detected with a heart attack.

SELECT mi.gender, COUNT( mi.member_id) AS count
FROM memberinfo mi
JOIN cardiodiagnosis cd ON mi.member_id = cd.memberinfo_member_id
JOIN bloodtest bt ON cd.cardio_id = bt.cardiodiagnosis_cardio_id
WHERE bt.bloodpressure > 140 AND cd.cardioarrestdetected = 1
GROUP BY mi.gender;

--47. Get the average blood pressure of people aged between 40-50 and 50-60.
SELECT 
    CASE 
        WHEN mi.age BETWEEN 40 AND 50 THEN '40-50'
        WHEN mi.age BETWEEN 51 AND 60 THEN '50-60'
    END AS age_group,
    AVG(bt.bloodpressure) AS avg_blood_pressure
FROM memberinfo mi
JOIN cardiodiagnosis cd ON mi.member_id = cd.memberinfo_member_id
JOIN bloodtest bt ON cd.cardio_id = bt.cardiodiagnosis_cardio_id
WHERE mi.age BETWEEN 40 AND 60
GROUP BY age_group;

--48. Get the list of diseases for people with high blood pressure in the range of 120-180, sorted by
--gender.
SELECT mi.gender, dd.disease_id, dd.diagnoseddate, bt.bloodpressure
FROM memberinfo AS mi
JOIN cardiodiagnosis cd ON mi.member_id = cd.memberinfo_member_id
JOIN diseasedetail dd ON cd.cardio_id = dd.cardiodiagnosis_cardio_id
JOIN bloodtest bt ON cd.cardio_id = bt.cardiodiagnosis_cardio_id
WHERE bt.bloodpressure BETWEEN 120 AND 180
ORDER BY mi.gender;

--49. Get the count of people who have had their X-rays every month from the state of "Special
--Province".
SELECT COUNT(*) AS people_with_xrays_every_month
FROM (
    SELECT 
        mi.member_id,
        COUNT(DISTINCT DATE_TRUNC('month', x.date)) AS months_with_xray
    FROM xray x
    JOIN cardiodiagnosis cd 
        ON cd.cardio_id = x.cardiodiagnosis_cardio_id
    JOIN memberinfo mi 
        ON mi.member_id = cd.memberinfo_member_id
    JOIN addressinfo ai 
        ON ai.memberinfo_member_id = mi.member_id
    WHERE ai.state = 'Special Province'
    GROUP BY mi.member_id
) t
WHERE months_with_xray >= 12;

--50. Get the average age of people diagnosed with a heart attack for each state, broken down by male
--and female.
SELECT ai.state, mi.gender, AVG(mi.age) AS avg_age
FROM memberinfo mi
JOIN addressinfo ai ON mi.member_id = ai.memberinfo_member_id
JOIN cardiodiagnosis cd ON mi.member_id = cd.memberinfo_member_id
WHERE cd.cardioarrestdetected = 1
GROUP BY ai.state, mi.gender
ORDER BY ai.state, mi.gender;

--51. Get the count of people for each state diagnosed with a heart attack, who have a slope value of 2,
--and have had at least one X-ray and one symptom.

SELECT ai.state, COUNT(DISTINCT mi.member_id) AS patient_count
FROM memberinfo mi
JOIN addressinfo ai ON mi.member_id = ai.memberinfo_member_id
JOIN cardiodiagnosis cd ON mi.member_id = cd.memberinfo_member_id
JOIN wearabledevicedata wd ON cd.cardio_id = wd.cardiodiagnosis_cardio_id
JOIN xray xr ON cd.cardio_id = xr.cardiodiagnosis_cardio_id
JOIN symptom s ON cd.cardio_id = s.cardiodiagnosis_cardio_id
WHERE cd.cardioarrestdetected = 1 AND wd.slope = 2
GROUP BY ai.state
ORDER BY ai.state;

