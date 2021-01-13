# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id SERIAL PRIMARY KEY,
        start_time bigint NOT NULL,
        user_id varchar NOT NULL,
        level varchar,
        song_id varchar,
        artist_id varchar,
        session_id varchar,
        location varchar,
        user_agent varchar
    )
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id varchar(255) PRIMARY KEY,
        first_name varchar(255),
        last_name varchar(255),
        gender char(1),
        level varchar(255)
    )
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id varchar(255) PRIMARY KEY,
        title varchar(255),
        artist_id varchar(255),
        year int,
        duration float(5)  
    )
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id varchar(255) PRIMARY KEY,
        artist_name varchar(255),
        artist_location varchar(255),
        artist_latitude varchar(255),
        artist_longitude varchar(255)
    )
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time TIME PRIMARY KEY,
        hour varchar(2),
        day varchar(2),
        week varchar(2),
        month varchar(2),
        year varchar(4),
        weekday varchar(2)
    )
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (
    songplay_id,
    start_time,
    user_id,
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent)
    VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level) \
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE SET level = excluded.level
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration) \
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude) \
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")


time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday) \
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""
    SELECT songs.song_id, artists.artist_id
            FROM songs
            JOIN artists
            ON songs.artist_id = artists.artist_id
            WHERE songs.title = %s 
            AND artists.artist_name = %s
            AND songs.duration = %s ;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]