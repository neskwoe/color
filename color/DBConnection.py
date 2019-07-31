#import MySQLdb
import pymysql.cursors
from bs4 import BeautifulSoup
import io
import os

class MySQL():

    def __init__(self, database): #类的初始化操作

        module_path = os.path.dirname(__file__)

        path = module_path + '/config.xml'

        configfile = io.open(path, encoding='utf-8')

        connectioninf = BeautifulSoup(configfile, 'lxml')

        server = connectioninf.find('server').getText()

        profile = connectioninf.find('profile').getText()

        pwd = connectioninf.find('pwd').getText()

        self.db = pymysql.connect(host=server,
                        user=profile,
                        password=pwd,
                        db=database,
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)

        self.cursor = self.db.cursor()

    def DB_close(self):

         self.db.close()

    def sql_insert(self, table_name, values):

        print('insert in process')

        req = self.sql_retrevefields(table_name)

        field = ''

        for f in req:

            field = field + ',' + f[0]

        sql = 'insert into ' + table_name + '(' + field[1:len(field)] + ') values(' + values + ')'

        self.cursor.execute(sql)

        self.db.commit()

        print('insert done')

    def sql_retrevefields(self, table_name):

        print('retrieving field name of table' + table_name)

        sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '" + table_name + "';"

        self.cursor.execute(sql)

        resultlist = []

        for row in self.cursor.fetchall():

            resultlist.append(row)

        return resultlist

    def select_data(self, sql):

        self.cursor.execute(sql)

        result = self.cursor.fetchall()

        resultList = []

        for i in result:

            resultList.append(i)

        # 得到的结果是字典格式
        return resultList