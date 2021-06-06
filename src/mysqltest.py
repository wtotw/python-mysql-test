import mysql.connector

# コネクションの作成
conn = mysql.connector.connect(
    host='mysql',
    port='3306',
    user='root',
    password='password',
    database='news_main'
)

# コネクションが切れた時に再接続してくれるよう設定
conn.ping(reconnect=True)

# 接続できているかどうか確認
print(conn.is_connected())

sql = 'SELECT * FROM m_news'

try:
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
except(mysql.connector.errors.ProgrammingError) as e:
    print('エラー')
    print(e)

for t_rows in rows:
    print(t_rows)