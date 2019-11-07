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

    def get_courses(self):
        return self.stud_courses.keys()

    def get_grades(self, course):
        return self.stud_courses.get(course)


    def set_req_missing_courses(self, courses):
        self.missing_req_courses = courses

    def get_req_missing_courses(self):
        return self.missing_req_courses

    def set_ele_missing_courses(self, courses):
        self.missing_ele_courses = courses

    def get_ele_missing_courses(self):
        return self.missing_ele_courses

    def p_student(self):
        """ Printing Student data """

        return [self.cwid, self.name, self.major, sorted(self.stud_courses.keys()), self.missing_req_courses, self.missing_ele_courses]


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

    def get_courses(self):
        return self.inst_courses.keys()

    def get_students(self, course):
        return self.inst_courses.get(course)


    def p_instructor(self):
        """ Printing Instructor data """
        for course, count in self.inst_courses.items():
            yield [self.cwid, self.name, self.dept, course, count]


class Majors:
    def __init__(self):
        self.majors_req_dat = {}
        self.majors_ele_dat = {}
 
    def major_required(self, major, code, course):
        if code == 'R':
            self.majors_req_dat.setdefault(major, []).append(course)
        elif code == 'E':
            self.majors_ele_dat.setdefault(major, []).append(course)
        
    def req_courses_missing(self, student):
        for key, value in student.items():
            courseTaken = set([c for c in student[key].get_courses()])
            studentMajor = student[key].major
            diff = set(self.majors_req_dat[studentMajor]) - courseTaken 
            student[key].set_req_missing_courses(diff)
        return student

    def ele_courses_missing(self, student):
        for key, value in student.items():
            courseTaken = set([c for c in student[key].get_courses()])
            studentMajor = student[key].major
            diff = set(self.majors_ele_dat[studentMajor]) - courseTaken 
            if len(diff) < len(self.majors_ele_dat[studentMajor]):
                student[key].set_ele_missing_courses(None)
            else:
                student[key].set_ele_missing_courses(diff)
        return student

        

class Repository:

    def __init__(self, directory):

        self.directory = directory
        self.student_cont = {}
        self.instructor_cont = {}
        self.analyze_students()
        self.analyze_instructor()
        self.analyze_grade()
        self.analyze_majors()
        self.major_table()
        self.stud_table()
        self.inst_table()

    def analyze_students(self):
        """ Adding the student deatils into a container """

        if not os.path.exists(self.directory):
            raise FileNotFoundError("No such directory")

        if "students.txt" not in os.listdir(self.directory):
            raise FileNotFoundError("No such Student file found")

        for student in self.file_reading_gen("students.txt", 3, ";"):
            
            self.student_cont[student[0]] = Student(student[0], student[1], student[2])

    def analyze_instructor(self):
        """ Adding the Instructor deatils into a container """

        if not os.path.exists(self.directory):
            raise FileNotFoundError("No such directory")

        if "instructors.txt" not in os.listdir(self.directory):
            raise FileNotFoundError("No such Instructor file found")

        for instructors in self.file_reading_gen("instructors.txt", 3, "|"):
            self.instructor_cont[instructors[0]] = Instructor(instructors[0], instructors[1], instructors[2])

    def analyze_grade(self):
        """ Adding the grade deatils into a container """

        if not os.path.exists(self.directory):
            raise FileNotFoundError("No such directory")

        if "grades.txt" not in os.listdir(self.directory):
            raise FileNotFoundError("No such grade file found")

        for grades in self.file_reading_gen("grades.txt", 4, "|"):
            try:
                student_instance = self.student_cont[grades[0]]
                student_instance.add_Stud_course(grades[1], grades[2])
            except KeyError:
                print(f"'{grades[0]}' key not present in student file'")
            
            try:
                instructor_instance = self.instructor_cont[grades[3]]
                instructor_instance.add_instr_course(grades[1])
            except KeyError:
                print(f"'{grades[3]}' key not present in instructor file")


    def analyze_majors(self):
        if not os.path.exists(self.directory):
            raise FileNotFoundError("No such directory")

        if "majors.txt" not in os.listdir(self.directory):
            raise FileNotFoundError("No such Instructor file found")
        
        x = Majors()
        for major in self.file_reading_gen("majors.txt", 3, sep = "\t"):
            x.major_required(major[0], major[1], major[2])
        self.major_req = x.majors_req_dat
        self.major_ele = x.majors_ele_dat
        self.student_cont = x.req_courses_missing(self.student_cont)
        self.student_cont = x.ele_courses_missing(self.student_cont)

    def major_table(self):
        """ Print the Student data in a pretty table """
        pt = PrettyTable(field_names=['Dept', 'Required', 'Electives'])
        li = []
        for key, value in self.major_req.items():
            try:
                pt.add_row([key, value, self.major_ele[key]])
                li.append([key, value, self.major_ele[key]])
            except:
                pt.add_row([key, value,[]])
                li.append([key, value,[]])
        return(li)

    def stud_table(self):
        """ Print the Student data in a pretty table """
        pt = PrettyTable(field_names=['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', 'Remaining electives'])
        li = []
        for i in self.student_cont.values():
            pt.add_row(i.p_student())
            li.append(i.p_student())
        return(li)

    def inst_table(self):
        """ Print the instructor data in a pretty table """
        pt = PrettyTable(field_names = ['CWID', 'Name', 'Dept', 'Course', 'Student'])
        li = []
        for i in self.instructor_cont.values():
            for j in i.p_instructor():
                pt.add_row(j)
                li.append(j)
        return(li)
    
    def file_reading_gen(self, path, fields, sep, header=True):
        try:
            fp = open(path, 'r')
        except FileNotFoundError:
            raise FileNotFoundError
        else:
            with fp:
                line_num = 0
                if header:
                    line_num += 1
                    fp.readline()
                for line in fp.readlines():
                    line_sep = line.strip('\n').split(sep)
                    line_num += 1
                    if len(line_sep) != fields:
                        raise ValueError(fp + " has " + str(len(line_sep)) + " fields on line " +
                                        str(line_num) + " but expected " + str(fields))

                    yield (tuple(line_sep))

def main():
    Repository("C:/Users/Rushabh/Desktop/810")


if __name__ == "__main__":
    main()
