#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Rushabh Doshi
Implement Student, Instructor class and read line to line data from the file and store in a repository
"""

from collections import defaultdict
import os
from prettytable import PrettyTable


class Student:
    """ Class provides information about each student """

    def __init__(self, cwid, name, major):
        self.cwid = cwid
        self.name = name
        self.major = major
        self.stud_courses = defaultdict(str)

    def add_Stud_course(self, course, grade):
        """ Adding course """

        self.stud_courses[course] = grade

    def p_student(self):
        """ Printing Student data """

        return [self.cwid, self.name, sorted(self.stud_courses.keys())]


class Instructor:
    """ Class provides information about each instructor """

    def __init__(self, cwid, name, dept):
        self.cwid = cwid
        self.name = name
        self.dept = dept
        self.inst_courses = defaultdict(int)

    def add_instr_course(self, course):
        """ Adding Instructor course """
        self.inst_courses[course] += 1

    def p_instructor(self):
        """ Printing Instructor data """
        for course, count in self.inst_courses.items():
            yield [self.cwid, self.name, self.dept, course, count]


class Repository:

    def __init__(self, directory):

        self.directory = directory
        self.student_cont = {}
        self.instructor_cont = {}
        self.analyze_students()
        self.analyze_instructor()
        self.analyze_grade()
        self.stud_table()
        self.inst_table()

    def analyze_students(self):
        """ Adding the student deatils into a container """

        if not os.path.exists(self.directory):
            raise FileNotFoundError("No such directory")

        if "students.txt" not in os.listdir(self.directory):
            raise FileNotFoundError("No such Student file found")

        for student in self.file_reading_gen("students.txt", 3, "\t"):
            self.student_cont[student[0]] = Student(student[0], student[1], student[2])

    def analyze_instructor(self):
        """ Adding the Instructor deatils into a container """

        if not os.path.exists(self.directory):
            raise FileNotFoundError("No such directory")

        if "instructors.txt" not in os.listdir(self.directory):
            raise FileNotFoundError("No such Instructor file found")

        for instructors in self.file_reading_gen("instructors.txt", 3, "\t"):
            self.instructor_cont[instructors[0]] = Instructor(instructors[0], instructors[1], instructors[2])

    def analyze_grade(self):
        """ Adding the grade deatils into a container """

        if not os.path.exists(self.directory):
            raise FileNotFoundError("No such directory")

        if "grades.txt" not in os.listdir(self.directory):
            raise FileNotFoundError("No such grade file found")

        for grades in self.file_reading_gen("grades.txt", 4, "\t"):
            student_instance = self.student_cont[grades[0]]
            student_instance.add_Stud_course(grades[1], grades[2])

            instructor_instance = self.instructor_cont[grades[3]]
            instructor_instance.add_instr_course(grades[1])

    def stud_table(self):
        """ Print the Student data in a pretty table """
        pt = PrettyTable(field_names=['CWID', 'Name', 'Completed Courses'])

        for i in self.student_cont.values():
            pt.add_row(i.p_student())

        print(pt)

    def inst_table(self):
        """ Print the instructor data in a pretty table """
        pt = PrettyTable(field_names=['CWID', 'Name', 'Dept', 'Course', 'Student'])

        for i in self.instructor_cont.values():
            for j in i.p_instructor():
                pt.add_row(j)

        print(pt)

    def file_reading_gen(self, path, fields, sep, header=False):
        """ Find the tuples after passing file and return the tuple after seperating fields """
        file_name = os.path.join(self.directory, path)
        try:
            file = open(file_name, "r")
        except FileNotFoundError:
            raise FileNotFoundError
        else:
            with file as fp:
                line_no = 0
                if header:
                    line_no += 1
                    header_line = fp.readline()
                    if header_line.strip('\n').split(sep) != fields:
                        print (file_name + " has " + str(len(header_line.strip('\n').split(
                            sep))) + " fields on line " + str(line_no) + " but expected " + str(fields))

                for line in fp.readlines():
                    a = line.strip('\n')
                    a = a.split(sep)
                    line_no += 1
                    if len(a) != fields:
                        print (file_name + " has " + str(len(a)) + " fields on line " + str(
                            line_no) + " but expected " + str(fields))

                    yield (tuple(a))


def main():
    Repository("C:/Users/Rushabh/Desktop/810/Stevens")


if __name__ == "__main__":
    main()
