import sqlite3
import os

class Database:
    # Initialize Database class
    def __init__ (self, reset=False):
        # Delete .db if reset is set to TRUE
        if reset == True:
            if os.path.exists( 'studentList.db' ):
                os.remove( 'studentList.db' )
        self.connection = sqlite3.connect('studentList.db')

    def create_tables(self):
        self.connection.execute(
          """ CREATE TABLE IF NOT EXISTS Students
          (STUDENT_ID       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
          FIRSTNAME        VARCHAR(50) NOT NULL,
          LASTNAME         VARCHAR(50) NOT NULL,
          BIRTHDAY         CHAR(10) NOT NULL);""")

    def addStudent(self, firstName, lastName, birthday):
      newStudent = """('%s', '%s', '%s')""" % (firstName, lastName, birthday)

      self.connection.execute(
          """ INSERT INTO Students (FIRSTNAME, LASTNAME, BIRTHDAY)
          VALUES %s;""" % newStudent)
