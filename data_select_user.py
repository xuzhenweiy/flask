import pymysql

def select_admin(username,password):

    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         database='test')

    cursor = db.cursor()

    sql = f"select * from admin where username='{username}' and password='{password}'"

    cursor.execute(sql)

    ret = cursor.rowcount

    if ret == 1:
        result = 1
    else:
        result = 0

    cursor.close()
    db.close()

    return ret


