#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Rushabh Doshi
Implement test case for all the programs
"""
from HW10_Rushabh_Doshi import Repository

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
                         ['10103', '10115', '10172', '10175', '10183', '11399', '11461', '11658', '11714', '11788'])

    def test_student_count_course(self):
        """ Test the courses in the course section """
        new_repo = Repository("C:/Users/Rushabh/Desktop/810").student_cont["10172"].stud_courses.keys()
        self.assertEqual(list(new_repo), ['SSW 555', 'SSW 567'])
    
    def test_major_table(self):
        """ Test the major table in the class """
        new_repo = Repository("C:/Users/Rushabh/Desktop/810")
        self.assertEqual(new_repo.major_table(), [['SFEN', ['SSW 540', 'SSW 564', 'SSW 555', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']], ['SYEN', ['SYS 671', 'SYS 612', 'SYS 800'], ['SSW 810', 'SSW 565', 'SSW 540']]])

    def test_student_table(self):
        """ Test the number of student in the class """
        new_repo = Repository("C:/Users/Rushabh/Desktop/810")
        self.assertEqual(new_repo.stud_table(), [['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], {'SSW 555', 'SSW 540'}, None], ['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], {'SSW 555', 'SSW 540'}, None], ['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], {'SSW 540', 'SSW 564'}, {'CS 545', 'CS 501', 'CS 513'}], ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], {'SSW 555', 'SSW 540'}, {'CS 545', 'CS 501', 'CS 513'}], ['10183', 'Chapman, O', 'SFEN', ['SSW 689'], {'SSW 567', 'SSW 555', 'SSW 540', 'SSW 564'}, {'CS 545', 'CS 501', 'CS 513'}], ['11399', 'Cordova, I', 'SYEN', ['SSW 540'], {'SYS 671', 'SYS 612', 'SYS 800'}, None], ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], {'SYS 671', 'SYS 612'}, {'SSW 810', 'SSW 565', 'SSW 540'}], ['11658', 'Kelly, P', 'SYEN', ['SSW 540'], {'SYS 671', 'SYS 612', 'SYS 800'}, None], ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], {'SYS 671', 'SYS 612', 'SYS 800'}, {'SSW 810', 'SSW 565', 'SSW 540'}], ['11788', 'Fuller, E', 'SYEN', ['SSW 540'], {'SYS 671', 'SYS 612', 'SYS 800'}, None]])

    def test_instructor_table(self):
        """ Test the instructor table in the class """
        new_repo = Repository("C:/Users/Rushabh/Desktop/810")
        self.assertEqual(new_repo.inst_table(), [['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4], ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3], ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 3], ['98764', 'Feynman, R', 'SFEN', 'SSW 687', 3], ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1], ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1], ['98763', 'Newton, I', 'SFEN', 'SSW 555', 1], ['98763', 'Newton, I', 'SFEN', 'SSW 689', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2], ['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1]])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
