-- lists all shows
-- use hbtn_0d_tvshows;
SELECT tv_show_genres.genre_id, tv_shows.title FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;