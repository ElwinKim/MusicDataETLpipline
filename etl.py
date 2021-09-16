import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    '''
        Read JSON format file and extract data from song files for artists table and songs table.
        And insert data to database
            Parameters:
                cur: Database conncetion object
                filepath: file address and name where the files are located
    '''

    df = pd.read_json(filepath, lines=True)

    artist_data = list(df[["artist_id", "artist_name", "artist_location",
                       "artist_latitude", "artist_longitude"]].values[0])
    cur.execute(artist_table_insert, artist_data)

    song_data = list(
        df[["song_id", "title", "artist_id", "year", "duration"]].values[0])
    cur.execute(song_table_insert, song_data)


def process_log_file(cur, filepath):
    '''
        1. Extract timestamp data(as a column 'ts') from a log file and convert to date data.
        2. Extract user data from a log file and convert to date data.
        3. Load timestamp and user data to songplays table.
            Parameters:
                cur: cursor class that allows Python code to execute PostgreSQL command in a database session
                filepath: file address and name where the files are located
    '''

    df = pd.read_json(filepath, lines=True)

    df = df[df['page'] == 'NextSong']

    t = pd.to_datetime(df.ts, unit="ms")

    time_data = (df.ts, t.dt.hour, t.dt.day, t.dt.weekofyear,
                 t.dt.month, t.dt.year, t.dt.weekday)
    column_labels = ('start_time', 'hour', 'day',
                     'week', 'month', 'year', 'weekday')
    time_df = pd.DataFrame(dict(zip(column_labels, time_data)))

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    user_list = df[['userId', 'firstName', 'lastName',
                    'gender', 'level']].drop_duplicates()
    column_labels = ('user_id', 'first_name', 'last_name',
                     'gender', 'level')
    user_list = user_list.values.tolist()
    user_df = pd.DataFrame(user_list, columns=column_labels)

    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    for index, row in df.iterrows():

        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        songplay_data = (row.ts, row.userId, row.level, songid,
                         artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    '''
            Accessing to filepath, and executing specific functions which is from a parameter. 
            Parameters:
                conn: data conncetion obejcet for using commit() class
                cur: cursor class that allows Python code to execute PostgreSQL command in a database session
                filepath: file address and name where the files are located
                func: To execute functions 
    '''
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    '''
            Main class for Connecting database and executing functions
            Parameters:
    '''
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb user=student password=student123")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
