#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Hypatia: Module ISBN Test [test]
#

__author__ = "Neko"
__license__ = 'LGPL http://www.gnu.org/licenses/lgpl.txt'

import unittest

import isbn

# Add incorrect 979 ISBN10 Fail
# Add valid digit incorrect Bookland code

isbn_ok = {
    '012345672X':    ['012345672X', '9780123456724', '978-0-12-345672-4', 'URN:ISBN:9780123456724', '10.978.012/3456724'],
    '9780387308869': ['0387308865', '9780387308869', '978-0-387-30886-9', 'URN:ISBN:9780387308869', '10.978.0387/308869'],
    '9780393334777': ['0393334775', '9780393334777', '978-0-393-33477-7', 'URN:ISBN:9780393334777', '10.978.0393/334777'],
    '9781593273880': ['1593273886', '9781593273880', '978-1-59327-388-0', 'URN:ISBN:9781593273880', '10.978.159327/3880'],
    '9788478447749': ['8478447741', '9788478447749', '978-84-7844-774-9', 'URN:ISBN:9788478447749', '10.978.847844/7749']
    }

isbn_nok = {
    'X123456781',
    '012345678X',
    '9780123456780',
    '9780123456781',
    '9790123456780',
    '9790123456781',
    '9890123456781'
    }


class ISBNTest(unittest.TestCase):

    def testISBNIn(self):
        for book in isbn_nok:
            self.assertFalse(isbn.ISBN.valid(book))

    def testISBNOut(self):
        for book in sorted(isbn_ok.keys()):
            id = isbn.ISBN(book)
            self.assertEqual(id.isbn10(), isbn_ok[book][0])
            self.assertEqual(id.isbn13(), isbn_ok[book][1])

    def testHyphen(self):
        for book in sorted(isbn_ok.keys()):
            id = isbn.ISBN(book)
            self.assertEqual(id.hyphen(), isbn_ok[book][2])

    def testURN(self):
        for book in sorted(isbn_ok.keys()):
            id = isbn.ISBN(book)
            self.assertEqual(id.urn(), isbn_ok[book][3])
            
    def testDOI(self):
        for book in sorted(isbn_ok.keys()):
            id = isbn.ISBN(book)
            self.assertEqual(id.doi(), isbn_ok[book][4])
            

if __name__ == '__main__':
    unittest.main()
