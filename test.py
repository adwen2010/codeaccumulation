import tushare as ts  
from sqlalchemy import create_engine 
import MySQLdb as mydb

#print(ts.__version__)
#pro = ts.pro_api("7f2a07d7a5331b296eca1d4209aeb78a67e5cff7127a70ce33eafd59")
#df = pro.daily(ts_code='600977',start_date='20200301',end_date='20200306')
#data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
#ts.get_hist_data('600977')
#print(df)

#res = ts.get_stock_basics()
#print(res)
#res = ts.get_hist_data('600997',start='2020-03-01',end='2020-03-08')
#for k in res:
    #print(k)
#print(res)

#engine = create_engine('mysql://root:123456@127.0.0.1/world?charset=utf8')
#df = ts.get_stock_basics()
#df.to_sql("basics",engine,if_exists='append')

#df = ts.get_hist_data('600998',start='2020-03-01',end='2020-03-08')
#存入数据库
#df.to_sql('table_600998',engine,if_exists='append')


conn=mydb.connect(host='localhost',port=3306,user='root',passwd='123456',db='world',charset='utf8')
cursor=conn.cursor()
count = cursor.execute('select * from city')
for count in range(count):
    res = cursor.fetchone()
    print(res)