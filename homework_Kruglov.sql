SELECT gern_name, COUNT(performer_id) FROM gerne
JOIN performergerne ON gerne.id = performergerne.gerne_id
GROUP BY gern_name;

SELECT COUNT(track_name) FROM tracks
WHERE album_id = (SELECT id FROM album
WHERE creation_date = 2020 OR creation_date = 2019);

SELECT alb_name, AVG(track_length) FROM tracks
JOIN album ON tracks.album_id = album.id
GROUP BY alb_name;

SELECT per_name, alb_name  FROM performer
JOIN performeralbum ON performer.id = performeralbum.performer_id
JOIN album ON performeralbum.album_id = album.id
WHERE creation_date != 2020;

SELECT DISTINCT col_name, per_name FROM collection
JOIN trackcollection ON trackcollection.collection_id = collection.id
JOIN tracks ON trackcollection.track_id = tracks.id
JOIN album ON tracks.album_id = album.id
JOIN performeralbum ON performeralbum.album_id = album.id
JOIN performer ON performer.id = performeralbum.performer_id
WHERE per_name = 'Queen';

SELECT per_name, alb_name, COUNT(gerne_id) FROM performer
JOIN performergerne ON performer.id = performergerne.performer_id
JOIN performeralbum ON performer.id = performeralbum.performer_id
JOIN album ON performeralbum.album_id = album.id
GROUP BY per_name, alb_name
HAVING COUNT(gerne_id)>1;

SELECT track_name FROM tracks
LEFT JOIN trackcollection ON tracks.id = trackcollection.track_id
WHERE trackcollection.track_id IS NULL;

SELECT per_name FROM tracks
JOIN performeralbum ON tracks.album_id = performeralbum.album_id
JOIN performer ON performer.id = performeralbum.performer_id
WHERE track_length = (SELECT MIN(track_length) FROM tracks);

SELECT alb_name, COUNT(qwer.id) 
FROM tracks AS qwer
JOIN album ON qwer.album_id = album.id
GROUP BY alb_name
ORDER BY COUNT(qwer.id) ASC
LIMIT 1;

SELECT alb_name, count FROM (SELECT alb_name, COUNT(qwer.id) 
FROM tracks AS qwer
JOIN album ON qwer.album_id = album.id
GROUP BY alb_name) AS qwer
WHERE qwer.count = 3;

WITH new_table AS (SELECT alb_name, COUNT(tracks.id) AS cnt
FROM tracks
JOIN album ON tracks.album_id = album.id
GROUP BY alb_name)
SELECT alb_name, cnt FROM new_table
WHERE cnt = (SELECT MIN(cnt) FROM new_table);

















