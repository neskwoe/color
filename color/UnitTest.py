from DBConnection import MySQL
import datetime as ds
import time

ts = time.time()

sqlcursor = MySQL('Btest')

sqlcursor.sql_insert('Twitter_Content', [ds.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'),
                                         'test2', 'Bone Ou', 1, 1, 1])

result = sqlcursor.select_data('select * from Twitter_Content')

print(result)
