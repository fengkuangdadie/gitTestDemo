import pymysql

#拿到了一个客户端
client = pymysql.Connect(
    user="root",
    password="111",
    host="127.0.0.1",
    port=3306,
    db="py1808",
    charset="utf8"
)

def show_tables():
    # 需要一个游标（鼠标的作用）
    cursor = client.cursor()
    #要执行的sql语句
    sql = "show tables;"
    # 执行sql 通过游标去执行
    res = cursor.execute(sql)
    # 执行结果在游标里
    real_res = cursor.fetchall()
    # 打印结果
    print(real_res)
    # print(res)

def chang_pla_age():
    #获取游标
    cursor = client.cursor()
    try:
        # 你要执行的sql
        cursor.execute("UPDATE player  SET age=33 WHERE id=1")
        cursor.execute("UPDATE player  SET age=33 WHERE id=4")
    except Exception as e:
        #sql出现异常  需要回滚
        print("进入异常")
        client.rollback()
    else:
        #如果没有错误 就commit结果
        print("正常提交")
        client.commit()

def get_pla_msg(p_id):
    cursor = client.cursor()
    #拼接sql语句
    sql = "SELECT * FROM player WHERE id>{sid}".format(
        sid=p_id
    )
    #执行sql语句
    cursor.execute(sql)
    #取结果
    #res = cursor.fetchall()
    # print(cursor.description)
    cols = [i[0] for i in cursor.description]
    print(cols)
    res_data = []
    for row in cursor.fetchall():
        tmp = zip(cols,row)
        dic_data = dict(tmp)
        res_data.append(dic_data)
    #返回结果
    return res_data
if __name__=="__main__":
    # chang_pla_age()
    res = get_pla_msg(3)
    print(res)



















