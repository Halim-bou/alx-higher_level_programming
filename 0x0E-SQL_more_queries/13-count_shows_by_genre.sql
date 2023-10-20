-- script to lists all genres from hbtn_0d_tvshows and display th number of shows linked to each.
-- Each record display <TV Show genre> - <Number of shows linked to this genre> with first colum called genre and second is number_of_shows sorted in descending orde by the number of shows linked.
SELECT g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS tv
ON g.id = tv.genre_id
GROUPE BY g.name ORDER BY number_of_shows DESC;
