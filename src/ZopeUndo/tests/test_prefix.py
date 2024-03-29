##############################################################################
#
# Copyright (c) 2001, 2002 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################

import unittest

from ZopeUndo.Prefix import Prefix


class PrefixTest(unittest.TestCase):

    def test(self):
        p1 = Prefix("/a/b")

        # test "==" (__eq__) operator
        for equal in ("/a/b", "/a/b/c", "/a/b/c/d"):
            self.assertEqual(p1, equal)
        for notEqual in ("", "/a/c", "/a/bbb", "///"):
            self.assertNotEqual(p1, notEqual)

        # test "!=" (__ne__) operator
        for equal in ("/a/b", "/a/b/c", "/a/b/c/d"):
            self.assertFalse(p1 != equal)
        for notEqual in ("", "/a/c", "/a/bbb", "///"):
            self.assertTrue(p1 != notEqual)

        p2 = Prefix("")
        for equal in ("", "/", "/def", "/a/b", "/a/b/c", "/a/b/c/d"):
            self.assertEqual(p2, equal)

    def test_username_info(self):
        # Zope Collector 1810; user paths have username appended
        p1 = Prefix('/a/b')
        for equal in ('/a/b spam', '/a/b/c spam', '/a/b/c/b spam'):
            self.assertEqual(p1, equal)
        for notEqual in (" spam", "/a/c spam", "/a/bbb spam", "/// spam"):
            self.assertNotEqual(p1, notEqual)

        p2 = Prefix("")
        for equal in (" eggs", "/ eggs", "/def eggs", "/a/b eggs",
                      "/a/b/c eggs", "/a/b/c/d eggs"):
            self.assertEqual(p2, equal)

    def test__repr__(self):
        p1 = Prefix('/a/b')
        self.assertEqual(repr(p1), "Prefix('/a/b')")
