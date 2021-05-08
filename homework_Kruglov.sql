SELECT name, creation_date FROM album
WHERE creation_date = 2018;

SELECT track_name, track_length FROM tracks
ORDER BY track_length DESC
LIMIT 1;

SELECT track_name, track_length FROM tracks
WHERE track_length = (SELECT max(track_length) FROM tracks);

SELECT track_name, track_length FROM tracks
WHERE track_length >= 210;

SELECT * FROM collection
WHERE creation_date BETWEEN '2018-01-01' AND '2020-12-31';

SELECT performer FROM performer
WHERE performer NOT LIKE '% %';

SELECT track_name FROM tracks
WHERE track_name iLIKE '%my%'
OR track_name iLIKE '%мой%';





