import sqlalchemy

engine = sqlalchemy.create_engine(DSN = 'postgresql://opavelo:gsxr1000@localhost:5432/postgres')
engine

connect = sqlalchemy.connect()
print(engine.table_names())

connection.execute('''INSERT INTO gerne
VALUES(1, 'Rock'),
(2, 'Pop'),
(3, 'Classics'),
(4, 'Rap'),
(5, 'Disco'),
(6, 'Rest shit');''')

connection.execute('''INSERT INTO performer
VALUES(1, 'Jony', 'pseudonym'),
(2, 'Zivert', 'pseudonym'),
(3, 'NILETTO', 'fdfdf'),
(4, 'Queen', 'pseudonym'),
(5, 'Scorpions', 'pseudonym'),
(6, 'Nirvana', 'pseudonym'),
(7, 'Prokofiev', 'pseudonym'),
(8, 'Vivaldi', 'pseudonym'),
(9, 'Mozart', 'pseudonym'),
(10, 'Eminem', 'pseudonym'),
(11, 'Dazl', 'pseudonym'),
(12, '50 Cent', 'pseudonym'),
(13, 'ABBA', 'pseudonym'),
(14, 'AQUA', 'pseudonym'),
(15, 'Modern Talking', 'pseudonym'),
(16, 'Something1', 'pseudonym'),
(17, 'Something2', 'pseudonym'),
(18, 'Something3', 'pseudonym');''')

connection.execute('''INSERT INTO performergerne
VALUES(1, 4),
(1, 5),
(1, 6),
(2, 1),
(2, 2),
(2, 3),
(3, 8),
(3, 9),
(3, 7),
(4, 10),
(4, 11),
(4, 12),
(5, 13),
(5, 14),
(5, 15),
(5, 16),
(5, 17),
(5, 18),
(6, 1),
(5, 2),
(5, 3);''')

connection.execute('''INSERT INTO album
VALUES(1, 'album1', 2010),
(2, 'album2', 2011),
(3, 'album3', 2012),
(4, 'album4', 2013),
(5, 'albuhm3', 2020),
(6, 'alkbum4', 2018),
(7, 'albutm3', 2008),
(8, 'a5lbum', 2018);''')

connection.execute('''INSERT INTO performeralbum
VALUES(1, 4),
(1, 5),
(6, 12);''')

connection.execute('''INSERT INTO tracks
VALUES(1, 'track1', 100, 1),
(2, 'track2', 150, 1),
(3, 'track3', 190, 1),
(4, 'track1', 90, 1),
(5,	"track2", 500, 2),
(6,	"track3", 200, 2),
(7,	"track1", 90,	3),
(8	"track2", 60,	3),
(9	"track3", 50,	3),
(10, "track1", 90,	4),
(11, "track2", 60,	4),
(12, "track3", 500,	4),
(13, "track1", 90,	5),
(14, "track2", 60,	5),
(15, "track3", 100,	5),
(16, "track1", 90,	6),
(17, "track2", 60,	6),
(18, "track3", 111,	6),
(19, "track1", 90,	7),
(20, "track2", 60,	7);''')

connection.execute('''INSERT INTO trackcollection
VALUES(1, 1),
(2,	1),
(3,	1),
(4,	1),
(5,	1),
(5,	2),
(7,	2),
(8,	2),
(7,	3),
(7,	4);''')

connection.execute('''INSERT INTO collection
VALUES(1, "SuperHITS", "2010-01-01"),
(2,	"SuperHITS 2",	"2011-12-01"),
(3,	"Gold Collection",	"2017-12-01"),
(4,	"Gold Collection",	"2018-12-01"),
(5,	"Road Collection",	"2017-12-01"),
(6,	"Road Collection 2",	"2014-12-01"),
(7,	"Road Collection 3",	"2019-02-01"),
(8,	"Best Singls",	"2015-10-01";''')








