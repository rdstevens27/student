#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Rushabh Doshi
Implement test case for all the programs
"""
from HW11_Rushabh_Doshi import Repository

import unittest


class TestRepository(unittest.TestCase):

    def test_repository_creation(self):
        """ Test if the repository is created """
        new_repo = Repository("C:/Users/Rushabh/Desktop/810")
        self.assertEqual(new_repo.directory, "C:/Users/Rushabh/Desktop/810")


class TestStudent(unittest.TestCase):

    def test_student_count(self):
        """ Test the number of student in the class """
        new_repo = Repository("C:/Users/Rushabh/Desktop/810").student_cont.keys()
        self.assertEqual(list(new_repo),
                         ['10103', '10115', '10183',  '11714'])

    def test_student_count_course(self):
        """ Test the courses in the course section """
        new_repo = Repository("C:/Users/Rushabh/Desktop/810").student_cont["10103"].stud_courses.keys()
        self.assertEqual(list(new_repo), ['SSW 810','CS 501' ])
    
    def test_major_table(self):
        print('\nTest: Major Table\n')
        new_repo = Repository("C:/Users/Rushabh/Desktop/810")
        self.assertEqual(new_repo.major_table(), [['SFEN', ['SSW 540', 'SSW 810', 'SSW 555'], ['CS 501', 'CS 546']], ['CS', ['CS 570', 'CS 546'], ['SSW 810', 'SSW 565']]])

    def test_student_table(self):
        new_repo = Repository("C:/Users/Rushabh/Desktop/810")
        self.assertEqual(new_repo.stud_table(), [['10103', 'Jobs, S', 'SFEN', ['CS 501', 'SSW 810'], {'SSW 540', 'SSW 555'}, None], ['10115', 'Bezos, J', 'SFEN', ['CS 546', 'SSW 810'], {'SSW 540', 'SSW 555'}, None], ['10183', 'Musk, E', 'SFEN', ['SSW 555', 'SSW 810'], {'SSW 540'}, {'CS 501', 'CS 546'}], ['11714', 'Gates, B', 'CS', ['CS 546', 'CS 570', 'SSW 810'], set(), None]])
    
    def test_instructor_table(self):
        new_repo = Repository("C:/Users/Rushabh/Desktop/810")
        self.assertEqual(new_repo.inst_table(), [['98764', 'Cohen, R', 'SFEN', 'CS 546', 1], ['98763', 'Rowland, J', 'SFEN', 'SSW 810', 4], ['98763', 'Rowland, J', 'SFEN', 'SSW 555', 1], ['98762', 'Hawking, S', 'CS', 'CS 501', 1], ['98762', 'Hawking, S', 'CS', 'CS 546', 1], ['98762', 'Hawking, S', 'CS', 'CS 570', 1]])
   
    def test_Instructor_table_db(self):
        print("testing the method in class repository")
        stevens = Repository("C:/Users/Rushabh/Desktop/810")
        self.assertEqual(stevens.instructor_table_db('810_startup.db'), [('98764', 'Cohen, R', 'SFEN', 'CS 546', 1), ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1), ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4), ('98762', 'Hawking, S', 'CS', 'CS 501', 1), ('98762', 'Hawking, S', 'CS', 'CS 546', 1), ('98762', 'Hawking, S', 'CS', 'CS 570', 1)])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
