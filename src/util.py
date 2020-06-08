import pymysql
import pandas as pd
from sqlalchemy import create_engine
# 打开数据库连接


class MySQLCon:
    def __init__(self, user='root', password = '', host='localhost', port='3306', database='gplay'):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def get_app_info(self, app_id=1):
        engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(self.user, self.password,
                                                                       self.host, self.port,
                                                                       self.database))
        try:
            # 执行SQL语句
            sql = "SELECT * FROM gplay_info WHERE app_id = %d" % (1)
            df_read = pd.read_sql_query(sql, engine)
            return df_read.ix[0]
        except:
            # 发生错误时回滚
            Exception("Error: unable to fetch data")
            return "error"

    def insert_classification_from_pandas(self, data):
        engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(self.user, self.password,
                                                                       self.host, self.port,
                                                                       self.database))
        con = engine.connect()
        data.to_sql(name='privacy_classification', con=con, if_exists='append', index=False)

    def get_classification_data(self, category):
        engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(self.user, self.password,
                                                                       self.host, self.port,
                                                                       self.database))
        sql = "SELECT * FROM privacy_classification WHERE category = '%s'" % (category)
        df_read = pd.read_sql_query(sql, engine)
        return df_read


def get_label_count(user = 'root', password = '', host='localhost', port='3306', database='gplay', category="all"):
    database = MySQLCon(user, password, host, port, database)
    result = database.get_classification_data(category)
    label_count = result.groupby('label').count()['data_id']
    sum_val = label_count.sum()
    label_result = {'label_'+str(i): round((label_count[str(i)]/sum_val), 2) for i in range(len(label_count))}
    return label_result





