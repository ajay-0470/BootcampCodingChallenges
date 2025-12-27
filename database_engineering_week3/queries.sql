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

