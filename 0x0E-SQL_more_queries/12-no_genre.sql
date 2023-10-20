-- script to lists all shows caontained in hbtn_0d_tvshows without a genre liked.
-- Each record should display tv_shows.title - tv_show_genre.genre_id sorted in ascending order
SELECT s.title, g.genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g
ON s.id = g.show_id
WHERE g.genre_id IS NULL
ORDER BY s.title, g.genre_id;
