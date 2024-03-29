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


class Prefix:
    """A Prefix() is equal to any path it is a prefix of.

    This class can be compared to a string.
    The comparison will return True if all path elements of the
    Prefix are found at the beginning of the string being compared.

    Two Prefixes can not be compared.
    """

    __no_side_effects__ = 1

    def __init__(self, path):
        path_list = path.split('/')
        self.length = len(path_list)
        self.path = path_list

    def __eq__(self, o):
        other_path = o.split('/')
        if other_path and ' ' in other_path[-1]:
            # don't include logged username in comparison
            pos = other_path[-1].rfind(' ')
            other_path[-1] = other_path[-1][:pos]
        return other_path[:self.length] == self.path

    def __ne__(self, o):
        return not self.__eq__(o)

    def __repr__(self):
        # makes failing tests easier to read
        return "Prefix('%s')" % '/'.join(self.path)
