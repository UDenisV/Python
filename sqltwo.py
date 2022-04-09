import sqlite3
import prettytable

conn = sqlite3.connect('school.db')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS classes")
cur.execute("DROP TABLE IF EXISTS students")
cur.execute("DROP TABLE IF EXISTS subjects")
cur.execute("DROP TABLE IF EXISTS marks")

cur.execute("PRAGMA foreign_keys = ON")

query = "CREATE TABLE IF NOT EXISTS classes (id INT NOT NULL PRIMARY KEY, class TEXT, num_of_stud INT, teacher TEXT)"
cur.execute(query)
cur.execute("INSERT INTO classes VALUES(1, '5А', 27, 'Панкратов Марк Александрович')")
cur.execute("INSERT INTO classes VALUES(2, '6А', 21, 'Шатилова Татьяна Николаевна')")
cur.execute("INSERT INTO classes VALUES(3, '7А', 20, 'Петров Тимофей Богданович')")
cur.execute("INSERT INTO classes VALUES(4, '8А', 32, 'Абрамова Анастасия Игоревна')")
cur.execute("INSERT INTO classes VALUES(5, '9А', 21, 'Михайлов Никита Арсентьевич')")
cur.execute("INSERT INTO classes VALUES(6, '10А', 22, 'Грачева Анна Евгеньевна')")
cur.execute("INSERT INTO classes VALUES(7, '11А', 31, 'Пономарева Таисия Артёмовна')")
cur.execute("INSERT INTO classes VALUES(8, '5Б', 23, 'Панкратов Марк Александрович')")
cur.execute("INSERT INTO classes VALUES(9, '6Б', 19, 'Шатилова Татьяна Николаевна')")
cur.execute("INSERT INTO classes VALUES(10, '7Б', 22, 'Петров Тимофей Богданович')")
cur.execute("INSERT INTO classes VALUES(11, '8Б', 26, 'Абрамова Анастасия Игоревна')")
cur.execute("INSERT INTO classes VALUES(12, '9Б', 23, 'Михайлов Никита Арсентьевич')")
cur.execute("INSERT INTO classes VALUES(13, '10Б', 20, 'Грачева Анна Евгеньевна')")
cur.execute("INSERT INTO classes VALUES(14, '11Б', 32, 'Пономарева Таисия Артёмовна')")
cur.execute("INSERT INTO classes VALUES(15, '5В', 27, 'Панкратов Марк Александрович')")
cur.execute("INSERT INTO classes VALUES(16, '6В', 23, 'Шатилова Татьяна Николаевна')")
cur.execute("INSERT INTO classes VALUES(17, '7В', 18, 'Петров Тимофей Богданович')")
cur.execute("INSERT INTO classes VALUES(18, '8В', 31, 'Абрамова Анастасия Игоревна')")
cur.execute("INSERT INTO classes VALUES(19, '9В', 28, 'Михайлов Никита Арсентьевич')")
cur.execute("INSERT INTO classes VALUES(20, '10В', 29, 'Грачева Анна Евгеньевна')")
cur.execute("INSERT INTO classes VALUES(21, '11В', 20, 'Пономарева Таисия Артёмовна')")

query1 = "CREATE TABLE IF NOT EXISTS students (id INT NOT NULL PRIMARY KEY, familia TEXT, imya TEXT, otchestvo TEXT, id_classes INT, age INT, gender TEXT, FOREIGN KEY (id_classes) REFERENCES classes (id) ON UPDATE CASCADE)"
cur.execute(query1)
cur.execute("INSERT INTO students VALUES(01, 'Павлов', 'Станислав', 'Васильевна', 1, 15, 'Мальчик')")
cur.execute("INSERT INTO students VALUES(02, 'Громов', 'Марк', 'Артёмович', 2, 16, 'Мальчик')")
cur.execute("INSERT INTO students VALUES(03, 'Шестакова', 'Ирина', 'Данииловна', 3, 15, 'Девочка')")
cur.execute("INSERT INTO students VALUES(04, 'Соловьев', 'Давид', 'Кириллович', 4, 16, 'Мальчик')")
cur.execute("INSERT INTO students VALUES(05, 'Волков', 'Егор', 'Максимович', 5, 14, 'Мальчик')")
cur.execute("INSERT INTO students VALUES(06, 'Гончарова', 'Амира', 'Михайловна', 6, 15, 'Девочка')")
cur.execute("INSERT INTO students VALUES(07, 'Романов', 'Семён', 'Георгиевич', 7, 16, 'Мальчик')")
cur.execute("INSERT INTO students VALUES(08, 'Шувалов', 'Денис', 'Германович', 8, 15, 'Мальчик')")
cur.execute("INSERT INTO students VALUES(09, 'Зайцева', 'Диана', 'Викторовна', 9, 16, 'Девочка')")
cur.execute("INSERT INTO students VALUES(010, 'Афанасьев', 'Олег', 'Арсентьевич', 10, 14, 'Мальчик')")
cur.execute("INSERT INTO students VALUES(011, 'Алексеев', 'Марьям', 'Максимович', 11, 15, 'Мальчик')")
cur.execute("INSERT INTO students VALUES(012, 'Баженов', 'Иван', 'Дамирович', 12, 16, 'Мальчик')")
cur.execute("INSERT INTO students VALUES(013, 'Беляков', 'Сергей', 'Иванович', 13, 15, 'Мальчик')")
cur.execute("INSERT INTO students VALUES(014, 'Петров', 'Дмитрий', 'Игоревич', 14, 16, 'Мальчик')")
cur.execute("INSERT INTO students VALUES(015, 'Сорокина', 'Мирослава', 'Ильинична', 15, 14, 'Девочка')")
cur.execute("INSERT INTO students VALUES(016, 'Владимирова', 'Александра', 'Дмитриевна', 16, 15, 'Девочка')")
cur.execute("INSERT INTO students VALUES(017, 'Алексеева', 'Ксения', 'Игоревна', 17, 16, 'Девочка')")
cur.execute("INSERT INTO students VALUES(018, 'Федоров', 'Артём', 'Александрович', 18, 15, 'Мальчик')")
cur.execute("INSERT INTO students VALUES(019, 'Белова', 'Евгения', 'Артемьевна', 19, 16, 'Девочка')")
cur.execute("INSERT INTO students VALUES(020, 'Беляева', 'Елизавета', 'Григорьевна', 20, 14, 'Девочка')")
cur.execute("INSERT INTO students VALUES(021, 'Орлова', 'Виктория', 'Максимовна', 21, 15, 'Девочка')")
cur.execute("INSERT INTO students VALUES(022, 'Ефремов', 'Фёдор', 'Фёдорович', 1, 16, 'Мальчик')")
cur.execute("INSERT INTO students VALUES(023, 'Фокин', 'Никита', 'Игоревич', 2, 15, 'Мальчик')")
cur.execute("INSERT INTO students VALUES(024, 'Смирнова', 'Ева', 'Артёмовна', 3, 16, 'Девочка')")
cur.execute("INSERT INTO students VALUES(025, 'Широков', 'Богдан', 'Павлович', 4, 14, 'Мальчик')")

query2 = "CREATE TABLE IF NOT EXISTS subjects (id INT NOT NULL PRIMARY KEY, subject)"
cur.execute(query2)
cur.execute("INSERT INTO subjects VALUES(001, 'Русский язык')")
cur.execute("INSERT INTO subjects VALUES(002, 'Алгебра')")
cur.execute("INSERT INTO subjects VALUES(003, 'Геометрия')")
cur.execute("INSERT INTO subjects VALUES(004, 'Теория Вероятностей и Статистика')")
cur.execute("INSERT INTO subjects VALUES(005, 'Английский язык')")
cur.execute("INSERT INTO subjects VALUES(006, 'Информатика')")
cur.execute("INSERT INTO subjects VALUES(007, 'Биология')")
cur.execute("INSERT INTO subjects VALUES(008, 'География')")
cur.execute("INSERT INTO subjects VALUES(009, 'История')")
cur.execute("INSERT INTO subjects VALUES(0010, 'Литература')")
cur.execute("INSERT INTO subjects VALUES(0011, 'Физика')")
cur.execute("INSERT INTO subjects VALUES(0012, 'Физкультура')")
cur.execute("INSERT INTO subjects VALUES(0013, 'Химия')")

query3 = "CREATE TABLE IF NOT EXISTS marks (id INT NOT NULL PRIMARY KEY, mark INT, id_students INT, id_subjects INT, FOREIGN KEY (id_subjects) REFERENCES subjects(id) ON UPDATE CASCADE, FOREIGN KEY (id_students) REFERENCES students(id) ON UPDATE CASCADE)"
cur.execute(query3)
cur.execute("INSERT INTO marks VALUES(0001, 5, 01, 001)")
cur.execute("INSERT INTO marks VALUES(0002, 4, 02, 002)")
cur.execute("INSERT INTO marks VALUES(0003, 2, 03, 003)")
cur.execute("INSERT INTO marks VALUES(0004, 5, 04, 004)")
cur.execute("INSERT INTO marks VALUES(0005, 3, 05, 005)")
cur.execute("INSERT INTO marks VALUES(0006, 4, 06, 006)")
cur.execute("INSERT INTO marks VALUES(0007, 4, 07, 007)")
cur.execute("INSERT INTO marks VALUES(0008, 3, 08, 008)")
cur.execute("INSERT INTO marks VALUES(0009, 2, 09, 009)")
cur.execute("INSERT INTO marks VALUES(00010, 5, 010, 0010)")
cur.execute("INSERT INTO marks VALUES(00011, 5, 011, 0011)")
cur.execute("INSERT INTO marks VALUES(00012, 5, 012, 0012)")
cur.execute("INSERT INTO marks VALUES(00013, 3, 013, 0013)")
cur.execute("INSERT INTO marks VALUES(00014, 4, 014, 001)")
cur.execute("INSERT INTO marks VALUES(00015, 2, 015, 002)")
cur.execute("INSERT INTO marks VALUES(00016, 2, 016, 003)")
cur.execute("INSERT INTO marks VALUES(00017, 4, 017, 004)")
cur.execute("INSERT INTO marks VALUES(00018, 3, 018, 005)")
cur.execute("INSERT INTO marks VALUES(00019, 5, 019, 006)")
cur.execute("INSERT INTO marks VALUES(00020, 4, 020, 007)")
cur.execute("INSERT INTO marks VALUES(00021, 3, 021, 008)")
cur.execute("INSERT INTO marks VALUES(00022, 3, 022, 009)")
cur.execute("INSERT INTO marks VALUES(00023, 5, 023, 0010)")
cur.execute("INSERT INTO marks VALUES(00024, 2, 024, 0011)")
cur.execute("INSERT INTO marks VALUES(00025, 4, 025, 0012)")

cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)
print('--------------------------------')
cur.execute("SELECT imya, familia, otchestvo FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)
print('--------------------------------')
cur.execute("SELECT * FROM students WHERE age=15 LIMIT 30")
rows = cur.fetchall()
for row in rows:
    print(row)
print('--------------------------------')
cur.execute("SELECT * FROM classes WHERE class<>'5А' AND num_of_stud>25")
rows = cur.fetchall()
for row in rows:
    print(row)
print('--------------------------------')
cur.execute("SELECT * FROM classes WHERE num_of_stud BETWEEN 20 AND 27")
rows = cur.fetchall()
for row in rows:
    print(row)
print('--------------------------------')
cur.execute("SELECT * FROM classes WHERE id>=7 AND teacher!='Шатилова Татьяна Николаевна' LIMIT 5")
rows = cur.fetchall()
for row in rows:
    print(row)
print('--------------------------------')
cur.execute("SELECT familia, imya, otchestvo FROM students WHERE age<18")
rows = cur.fetchall()
for row in rows:
    print(row)
print('--------------------------------')

conn.commit()
conn.close()
