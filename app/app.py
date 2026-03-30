import time
from db.sqlite_db import init_sqlite, get_sqlite_data
from db.mysql_db import connect_mysql, init_mysql, get_mysql_data

# --- SQLite ---
sqlite_conn, sqlite_cursor = init_sqlite()

# --- MySQL ---
mysql_conn = connect_mysql()
mysql_cursor = init_mysql(mysql_conn)


# --- LOOP ---
while True:
    # SQLite
    sqlite_rows = get_sqlite_data(sqlite_cursor)
    print("SQLite:", sqlite_rows, flush=True)

    # MySQL
    if mysql_cursor:
        try:
            mysql_rows = get_mysql_data(mysql_cursor)
            print("MySQL:", mysql_rows, flush=True)
        except Exception as e:
            print("MySQL error:", e, flush=True)
    else:
        print("MySQL not connected", flush=True)

    time.sleep(10)
