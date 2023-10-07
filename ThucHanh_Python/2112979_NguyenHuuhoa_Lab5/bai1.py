import pyodbc
import sqlite3


connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\\SQLEXPRESS;DATABASE=QLSinhVien; UID=sa;PWD=sa;Encrypt=no'

def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn

def close_connection(conn):
    if conn:
        conn.close()

def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """select + from lop"""
        cursor.execute(select_query)
        records = cursor.fetchall()

        print(f"Danh sách các lớp là: ")
        for row in records:
            print("+", 50)
            print("Mã lớp: ", row[0])
            print("Tên lớp: ", row[1])
        
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

get_all_class()