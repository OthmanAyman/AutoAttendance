import sqlite3
import datetime


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(
            'DB.db', detect_types=sqlite3.PARSE_DECLTYPES)
        self.cur = self.conn.cursor()
#       Create tables
        self.cur.execute("CREATE TABLE IF NOT EXISTS Students (id INTEGER PRIMARY KEY , name TEXT NOT NULL UNIQUE, "
                         "email TEXT)")

        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Courses ("
            "id INTEGER PRIMARY KEY, name TEXT UNIQUE,"
            "day TEXT, start date , hours INTEGER)")

        self.cur.execute("CREATE TABLE IF NOT EXISTS C_S ( "
                         "student_id INTEGER , "
                         "course_id INTEGER, "
                         "FOREIGN KEY (student_id) REFERENCES Students (id),"
                         "FOREIGN KEY (course_id) REFERENCES Courses (id))")

        self.cur.execute("CREATE TABLE IF NOT EXISTS Attendance ("
                         "student_id INTEGER , "
                         "course_id INTEGER, "
                         "present INTEGER ,"
                         "[time] timestamp,"
                         "FOREIGN KEY (student_id) REFERENCES Students (id),"
                         "FOREIGN KEY (course_id) REFERENCES Courses (id))")
        self.conn.commit()

        # insert data###################################
    def insert_student(self, name, email):
        # the NULL parameter is for the auto-incremented id
        self.cur.execute(
            "INSERT INTO Students VALUES(NULL,?,?)", (name, email))
        self.conn.commit()

    def insert_course(self, name, day, start, hours):
        # the NULL parameter is for the auto-incremented id
        r = self.search(course=name)
        if r is None:
            self.cur.execute(
                "INSERT INTO Courses VALUES(NULL,?,?,?,?)", (name, day, start, hours))
            self.conn.commit()
        else:
            pass

    def insert_c_s(self, student, course, email=None):

        self.cur.execute("SELECT id FROM Students WHERE name = ? OR email = ? ",
                         (student, email,))
        student = self.cur.fetchone()[0]

        self.cur.execute("SELECT id FROM Courses WHERE name = ?  ", (course,))
        course = self.cur.fetchone()[0]

        self.cur.execute("INSERT INTO C_S VALUES(?,?)", (student, course,))
        self.conn.commit()

    def insert_attendance(self, student, course, present=0, email=None):

        self.cur.execute("SELECT id FROM Students WHERE name = ? OR email = ? ",
                         (student, email,))
        student = self.cur.fetchone()[0]

        self.cur.execute("SELECT id FROM Courses WHERE name = ?  ", (course,))
        course = self.cur.fetchone()[0]

        self.cur.execute("INSERT INTO Attendance VALUES(?,?,?,?)",
                         (student, course, present, datetime.datetime.now()))
        self.conn.commit()

    ## SHOW DATA ###################################
    def view_students(self):
        self.cur.execute("SELECT * FROM Students")
        rows = self.cur.fetchall()

        return rows

    def view_courses(self):
        self.cur.execute("SELECT * FROM Courses")
        rows = self.cur.fetchall()

        return rows

    def view_c_s(self, course):
        self.cur.execute("SELECT id FROM Courses WHERE name = ?  ",
                         (course,))
        course = self.cur.fetchone()[0]

        self.cur.execute(
            "SELECT S.id,S.name FROM Students as S ,Courses as C ,C_S as CS"
            " WHERE CS.student_id = S.id AND CS.course_id= C.id AND C.id=?", (course,))
        rows = self.cur.fetchall()

        return rows

    def search(self, student=None, course=None, year=None, month=None, day=None):
        exe = """SELECT S.id ,S.name, C.name,A.present,A.time FROM Attendance as A, Students as S ,Courses as C
                WHERE A.student_id=S.id AND A.course_id=C.id """
        if course:
            self.cur.execute("SELECT id FROM Courses WHERE name = ? ",
                             (course, ))
            course = self.cur.fetchone()
            if course is None:
                return None
            else:
                course = self.cur.fetchone()[0]

            exe += f" AND course_id = {course} "

        if student:
            self.cur.execute("SELECT id FROM Students WHERE name = ?  ",
                             (student,))
            student = self.cur.fetchone()[0]
            exe += f" AND student_id = {student} "

        if year:
            year = year
            exe += f" AND ('%y', time) = {year} "

        if month:
            month = int(month)
            exe += f" AND SUBSTR(time,4,2) = {month} "

        if day:
            day = day
            exe += f" AND ('%d', time) = {day} "

        self.cur.execute(exe)
        rows = self.cur.fetchall()
        return rows

    def delete_student(self, student):
        self.cur.execute("DELETE FROM Students WHERE name = ?", (student,))
        self.conn.commit()

    def delete_course(self, course):
        self.cur.execute("DELETE FROM Courses WHERE name = ? ", (course,))
        self.conn.commit()

    def delete_attendace(self, student=None, course=None, year=None, month=None, day=None):
        exe = "DELETE FROM Attendance WHERE (present=1 OR present=0) "
        if course:
            self.cur.execute("SELECT id FROM Courses WHERE name = ? ",
                             (course, ))
            course = self.cur.fetchone()[0]
            exe += f" AND course_id = {course} "

        if student:
            self.cur.execute("SELECT id FROM Students WHERE name = ? OR email = ? ",
                             (student, email,))
            student = self.cur.fetchone()[0]
            exe += f" AND student_id = {student} "

        if year:
            year = str(year)
            exe += f" AND ('%y', time) = {year} "

        if month:
            month = str(month)
            exe += f" AND ('%m', time) = {month} "

        if day:
            day = str(day)
            exe += f" AND ('%d', time) = {day} "

        self.cur.execute(exe)
        self.conn.commit()

    def destroy(self):
        exe = 'DELETE FROM Students'
        self.cur.execute(exe)
        self.conn.commit()
        exe = 'DELETE FROM Courses'
        self.cur.execute(exe)
        self.conn.commit()
        exe = 'DELETE FROM C_S'
        self.cur.execute(exe)
        self.conn.commit()
        exe = 'DELETE FROM Attendance'
        self.cur.execute(exe)
        self.conn.commit()

    # destructor-->now we close the connection to our database here

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    # k = Database()
    # k.destroy()

    # k.insert_student(name='ahmad', email='ahmad@mail.co')
    # k.insert_student(name='fatma', email='fatma@mail.co')
    # k.insert_student(name='omer', email='omer@mail.co')
    # k.insert_student(name='huda', email='huda@mail.co')
    # # l = k.view_students()
    # # for i in l:
    # #     # i = i.split()
    # #     print(i)
    # k.insert_course(name='math', day='sunday', start='10:30', hours=1.5)
    # k.insert_course(name='phy', day='monday', start='9:30', hours=1.5)
    # l = k.view_courses()
    # for i in l:
    #     # i = i.split()
    #     print(i)
    #
    # k.insert_c_s(student='ahmad', course='math')
    # k.insert_c_s(student='fatma', course='math')
    # k.insert_c_s(student='omer', course='math')
    #
    # k.insert_c_s(student='omer', course='phy')
    # k.insert_c_s(student='huda', course='phy')
    #
    # k.insert_attendance(student='omer', course='math', present=1)
    # k.insert_attendance(student='fatma', course='math', present=1)
    # k.insert_attendance(student='ahmad', course='math', present=0)

    # print(k.search(month=5))

    # l = k.view_c_s(course='phy')
    # print('physics students:', l)
    # for i in l:
    #     # i = i.split()
    #     print(i)
    #
    # l = k.view_c_s(course='phy')
    # print('physics Students:')
    # for i in l:
    #     # i = i.split()
    #     print(i)
    pass
