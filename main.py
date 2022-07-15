from distutils.util import execute
import sqlite3

dbname = "test.db"
conn = sqlite3.connect(dbname)

# sqliteを操作するカーソルオブジェクトの作成
cur = conn.cursor()

cur.execute('SELECT * FROM persons')

# dbへ情報コミット
for row in cur:
    print(row[1])

# db接続を切断
cur.close()
conn.close()
