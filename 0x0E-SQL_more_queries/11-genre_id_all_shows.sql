-- script to lists all shows caontained in the database hbt_od_tvshows.
-- Each record should display tv_show.title - tv_show_genre.genre_id sorted must be ascending order, display NULL
SELECT s.title, g.genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id;
