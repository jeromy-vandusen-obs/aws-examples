import os
import pymysql

host = os.environ["DB_HOST"]
username = os.environ["DB_USERNAME"]
password = os.environ["DB_PASSWORD"]
database = os.environ["DB_NAME"]

connection = pymysql.connect(host, user=username, passwd=password, db=database, connect_timeout=5)

def select_row(id):
    sql = "select * from some_table where some_key = %d"
    with connection.cursor() as cursor:
        cursor.execute(sql, (id,))
        return cursor.fetchone()

def select_rows(value):
    sql = "select * from some_table where some_value = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql, (value,))
        return cursor.fetchall()

def insert_row(item):
    sql = "insert into some_table (id, name, code) values (%d, %s, %s)"
    with connection.cursor() as cursor:
        cursor.execute(sql, (item["id"], item["name"], item["code"]))
    connection.commit()

def update_row(id, newValue):
    sql = "update some_table set some_value = %s where id = %d"
    with connection.cursor() as cursor:
        cursor.execute(sql, (newValue, id))
    connection.commit()

def delete_row(id):
    sql = "delete from some_table where some_key = %d"
    with connection.cursor() as cursor:
        cursor.execute(sql, (id,))
    connection.commit()

def lambda_handler(event, context):
    item_count = len(select_rows("test"))
    return "Found %d rows." %(item_count)
