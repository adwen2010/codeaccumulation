import tushare as ts  
from sqlalchemy import create_engine 
import MySQLdb as mydb

remoteconfig='mysql://root:123456@127.0.0.1/mydb?charset=utf8'
localconfig={'host':'localhost','port':3306,'user':'root','passwd':'123456','db':'mydb','charset':'utf8'}
basics_table = 'table_basics'

def getRemotebasic():
    engine = create_engine(remoteconfig)
    df = ts.get_stock_basics()
    df.to_sql(basics_table,engine,if_exists='append')

def getLocalbasic():
    conn=mydb.connect(**localconfig)
    cursor=conn.cursor()
    searchsql = 'select code from ' + basics_table
    count = cursor.execute(searchsql)
    res = cursor.fetchall()
    stock_all = []
    for i in res:
        stock_all.append(i[0])
    return stock_all

def gethistorytodb(stock_all):
    engine = create_engine(remoteconfig)
    for stock in stock_all:
        df = ts.get_hist_data(stock,start='2010-01-01',end='2020-03-08')
        table_name = "table_" + stock
        df.to_sql(table_name,engine,if_exists='append')

def get_today_all():
    engine = create_engine(remoteconfig)
    df = ts.get_today_all()#查看前一日的全部数据
    df.to_sql("table_today_all",engine,if_exists='append')

def compactiontables(stock_all):
    conn=mydb.connect(**localconfig)
    cursor=conn.cursor()
    #searchsql = ''
    #count = cursor.execute(searchsql)
    

def main():
    #获取前一日的全部数据
    get_today_all()


main()
    
    