#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Rushabh Doshi
Implement test case for all the programs
"""
from HW09_Rushabh_Doshi import Repository

import unittest


class TestRepository(unittest.TestCase):

    def test_repository_creation(self):
        """ Test if the repository is created """
        new_repo = Repository('stevens')
        self.assertEqual(new_repo.directory, "stevens")


class TestStudent(unittest.TestCase):

    def test_student_count(self):
        """ Test the number of student in the class """
        new_repo = Repository('stevens').student_cont.keys()
        self.assertEqual(list(new_repo),
                         ['10103', '10115', '10172', '10175', '10183', '11399', '11461', '11658', '11714', '11788'])

    def test_student_count_course(self):
        """ Test the courses in the course section """
        new_repo = Repository('stevens').student_cont["10172"].stud_courses.keys()
        self.assertEqual(list(new_repo), ['SSW 555', 'SSW 567'])

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
