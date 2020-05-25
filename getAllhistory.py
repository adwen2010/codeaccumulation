import tushare as ts  
from sqlalchemy import create_engine 
import MySQLdb as mydb

remoteconfig='mysql://root:123456@127.0.0.1/mydb?charset=utf8'
localconfig={'host':'localhost','port':3306,'user':'root','passwd':'123456','db':'mydb','charset':'utf8'}
basics_table = 'table_basics'
createtablesql=" ( `date` text,  `open` double DEFAULT NULL,  `high` double DEFAULT NULL,  `close` double DEFAULT NULL,  `low` double DEFAULT NULL,  `volume` double DEFAULT NULL,  `price_change` double DEFAULT NULL,  `p_change` double DEFAULT NULL,  `ma5` double DEFAULT NULL,  `ma10` double DEFAULT NULL,  `ma20` double DEFAULT NULL,  `v_ma5` double DEFAULT NULL,  `v_ma10` double DEFAULT NULL,  `v_ma20` double DEFAULT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"

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

def gethistorytodb(stock):
    try:
        engine = create_engine(remoteconfig)
        df = ts.get_hist_data(stock,start='2018-01-01',end='2020-03-15')
        table_name = 'table_'+stock
        if df :
            df.to_sql(table_name,engine,if_exists='append')
        else:
            print(table_name+" no hisdata")
    except:
        print(stock+' error')

def createtables(stock):
    table_name = "table_" + stock
    strsql = 'create table ' + table_name + createtablesql
    conn=mydb.connect(**localconfig)
    cursor=conn.cursor()
    try:
        count = cursor.execute(strsql)
        return True
    except :
        return False

def main():
    #从本地数据库读出代码列表
    stock_all = getLocalbasic()
    #print(stock_all)
    for stock in stock_all:
        if True == createtables(stock):
            #获取所有stock的历史记录
            print(stock)
            gethistorytodb(stock)

def getone(stock):
    engine = create_engine(remoteconfig)
    df = ts.get_hist_data(stock,start='2018-01-01',end='2020-03-15')
    if df :
        print(df)
        table_name = 'table_'+stock
        df.to_sql(table_name,engine,if_exists='append')

main()