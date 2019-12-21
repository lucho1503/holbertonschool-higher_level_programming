-- this query list all genres and display the number of shows
SELECT name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre_id ORDER BY COUNT(*) DESC;
