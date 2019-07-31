from DBConnection import MySQL

sqlcursor = MySQL('Btest')

result = sqlcursor.select_data('select * from Twitter_Content')

print(result)
