-- script that lists all shows and all genres linked to that show from the database hbtn_0d_shows.
-- dislay null when show have no genre, each record display tv_shows.title - tv_genres.name and sorted in ascending order by show title and genre name.
SELECT tv.title, g.name
FROM tv_shows AS tv
LEFT JOIN tv_show_genres AS s
ON tv.id = s.show_id
LEFT JOIN tv_genres AS g
ON s.genre_id = g.id ORDER BY tv.title, g.name;
