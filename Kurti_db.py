import sqlite3


def nauja_db():
    conn = sqlite3.connect("rezultatai.db")
    c = conn.cursor()
    with conn:
        c.execute("""CREATE TABLE IF NOT EXISTS rezultatai (
                    vardas text,
                    sunkumas text,
                    taskai integer
                    )""")
