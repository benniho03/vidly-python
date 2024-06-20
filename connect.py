import psycopg2
import pandas as pd

def connect():
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect("postgresql://gruppe2:on21-6:d2@db-postgresql-fra1-94996-do-user-6859634-0.c.db.ondigitalocean.com:25060/gruppe2") as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def get_all_videos():
    try:
        db = connect()
        cur = db.cursor()

        # SQL-Abfrage ausführen
        cur.execute("SELECT * FROM videos")
        videos = cur.fetchall()

        # Spaltennamen abrufen
        column_names = [desc[0] for desc in cur.description]

        # Daten in ein DataFrame laden
        df_videos = pd.DataFrame(videos, columns=column_names)
        return df_videos

    except Exception as e:
        print(e)
    finally:
        if db is not None:
            cur.close()
            db.close()
            print('Database connection closed.')

def get_all_videos_ml():
    try:
        db = connect()
        cur = db.cursor()

        # SQL-Abfrage ausführen
        cur.execute("""SELECT
                    videos.duration,
                    videos.titlecharlength,
                    videos.descriptioncharlength,
                    videos."publishedAt",
                    videos."viewCount",
                    videos."commentCount",
                    videos."likeCount",
                    channels."viewCount" AS "totalChannelViews",
                    channels."subscriberCount",
                    channels."videoCount"
                    FROM videos INNER JOIN channels ON videos.channel = channels.id""")
        videos = cur.fetchall()

        # Spaltennamen abrufen
        column_names = [desc[0] for desc in cur.description]
        # Daten in ein DataFrame laden
        df_videos = pd.DataFrame(videos, columns=column_names)
        return df_videos

    except Exception as e:
        print(e)
    finally:
        if db is not None:
            cur.close()
            db.close()
            print('Database connection closed.')


if __name__ == '__main__':
    videos = get_all_videos_ml()
    print(videos)

def get_videos_no_music():
    try:
        db = connect()
        cur = db.cursor()

        # SQL-Abfrage ausführen
        cur.execute("SELECT * FROM videos WHERE NOT categoryid = 10")
        videos = cur.fetchall()

        # Spaltennamen abrufen
        column_names = [desc[0] for desc in cur.description]

        # Daten in ein DataFrame laden
        df_videos = pd.DataFrame(videos, columns=column_names)
        return df_videos

    except Exception as e:
        print(e)
    finally:
        if db is not None:
            cur.close()
            db.close()
            print('Database connection closed.')
