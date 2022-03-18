-- Write a script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv.title, genre.genre_id FROM tv_shows
AS tv LEFT JOIN tv_show_genres
AS genre ON tv.id = genre.show_id
ORDER BY tv.title, genre.genre_id ASC;
