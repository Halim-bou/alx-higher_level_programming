-- script to lists all Comedy shows in the database hbtn_0d_tvshows
-- Each record display tv_shows.title and sorted in ascending order by the show title
SELECT tv.title
FROM tv_shows AS tv
INNER JOIN tv_show_genres AS s
ON tv.id = s.show_id
INNER JOIN tv_genres AS g
ON g.id = s.genre_id WHERE g.name = "Comedy"
ORDER BY tv.title;
