import sqlite3


def fetch_customers_with_high_grades(db_name):
    try:
        # Подключение к базе данных
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        print("Connected to SQLite")

        # Выполнение запроса для выбора записей, где grade > 200, отсортированных по id
        cursor.execute("SELECT * FROM customers WHERE grade > 200 ORDER BY id")
        rows = cursor.fetchall()

        # Вывод информации о количестве записей
        print(f"Total rows are:   {len(rows)}")
        if len(rows) > 0:
            print("Printing each row")

        # Печать каждой строки
        for row in rows:
            print(f"Id:  {row[0]}")
            print(f"Name:  {row[1]}")
            print(f"City:  {row[2]}")
            print(f"Grade:  {row[3]}")
            print(f"Seller:  {row[4]}\n\n")

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        # Закрытие соединения
        if conn:
            conn.close()
            print("The SQLite connection is closed")


if __name__ == "__main__":
    fetch_customers_with_high_grades("q1.db")
