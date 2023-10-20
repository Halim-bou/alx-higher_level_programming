-- script to uses the hbtn_0d_tvshows database to lists all genres of shows Dexter.
-- Each record display tv_genre.name sorted in ascending order by the genre name
SELECT g.name
FROM tv_genres AS g
INNER JOIN tv_show_genres AS s
ON g.id =s.genre_id
INNER JOIN tv_shows AS tv
ON tv.id = s.show_id WHERE tv.title = "Dexter"
ORDER BY g.name;
