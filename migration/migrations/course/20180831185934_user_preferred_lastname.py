def up(config, conn, semester, course):
    with conn.cursor() as cursor:
        cursor.execute("ALTER TABLE users ADD COLUMN IF NOT EXISTS user_preferred_lastname character varying")

def down(config, conn, semester, course):
    with conn.cursor() as cursor:
        cursor.execute("ALTER TABLE users DROP COLUMN IF EXISTS user_preferred_lastname")
