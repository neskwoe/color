from DBConnection import SqlConn
import datetime as ds
import time

ts = time.time()

sqlcursor = SqlConn('Btest')

fields = sqlcursor.field_retrieve('Twitter_Content')
values = [ds.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'),
                                         'test2', 'Bone Ou', 1, 1, 1]

sqlinput = dict(zip(fields, values))

sqlstatement = sqlcursor.get_i_sql('Twitter_Content', sqlinput)

sqlcursor.execute(sqlstatement)

sqlcursor.commit()


