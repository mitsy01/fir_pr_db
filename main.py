import sqlite3

def test_db_query():
    try:
        sql_con = sqlite3.connect("my_test.db")
        cursor = sql_con.cursor()

        with open("create_table.txt") as fh:
        # with open("insert_data.txt") as fh:
        # with open("select_data.txt") as fh:
            query = fh.read()

        cursor.execute(query)
        students = cursor.fetchall()
        for student in students:
            print(f"{student = }")

        cursor.close()
        # print("Дані успішно записано.")

    except sqlite3.Error as error:
        print("Виникла помилка:", error)

    finally:
        if sql_con:
            sql_con.close()
            print("Робота з базою даних завершено.")


def insert_data(first_name: str, last_name: str, age: int = None, grade: int = None):
    try:
        sql_con = sqlite3.connect("my_test.db")
        cursor = sql_con.cursor()
        
        query = "INSERT INTO Students (first_name, last_name, age, grade) VALUES (?, ?, ?, ?)"
        
        data = (first_name, last_name, age, grade)
        
        cursor.execute(query, data)
        sql_con.commit()
        cursor.close()
        print("Дані записані.")
    
    except sqlite3.Error as error:
        print("Помилка", error)
        
    finally:
        if sql_con:
            sql_con.close()
            print("Запит на підключення до бази даних закрит.")


test_db_query()
insert_data("Міша", "Еврік", 15, 76)
insert_data("Айзен", "Соловенко", 16, 100)
insert_data("Крістіна", "Шихоїн", 15, 98)
insert_data("окаріХ"[::-1], "іздніШ"[::-1], 17, 92)
insert_data("Даніїл", "Хаченко", 15, grade=1)
insert_data("Гін", "Маляренко", 15,99)
insert_data("Їзмаіл", "Годженко",18 , 21)
insert_data("Кіріл", "Баранов", 42, 42)
insert_data("Яхве", "чивоййеГ"[::-1], 15 , grade=100)