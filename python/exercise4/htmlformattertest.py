import unittest
import os
from htmlformatter import *


class HtmlFormatterTest(unittest.TestCase):
    def setUp(self):
        if os.path.exists("output.html"):
            os.remove("output.html")
        self.expected = """<html><body>
<table border="1">
<tr><th>Username</th><th>Last login</th></tr><tr>
<td>admin</td><td>2020-02-20</td></tr>
<tr>
<td>guest</td><td>2020-02-29</td></tr>
<tr>
<td>john</td><td>2020-03-01</td></tr>
</tr></table>
</body></html>
"""

    def test_files_are_identical(self):
        data = [
            { "username": "admin", "date": "2020-02-20"},
            { "username": "guest", "date": "2020-02-29"},
            { "username": "john", "date": "2020-03-01"}
        ]
        HtmlFormatter().printReport(data)

        f = open("output.html","r")
        actual = f.read()
        self.assertEquals(actual,self.expected)

if __name__ == '__main__':
    unittest.main()
