import unittest
from unittest.mock import *
import os
from htmlformatter3 import *

class TestableHtmlFormatter(HtmlFormatter):
    def __init__(self):
        self.text = ""

    def openFile(self):
        pass
    
    def writeToFile(self,f,text):
        self.text += text

    def closeFile(self,f):
        pass

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

    # test using a blackbox test that accesses filesystem
    def test_files_are_identical(self):
        data = [
            { "username": "admin", "date": "2020-02-20"},
            { "username": "guest", "date": "2020-02-29"},
            { "username": "john", "date": "2020-03-01"}
        ]
        HtmlFormatter().printReport(data)

        with open("output.html","r") as f:
            actual = f.read()
        self.assertEqual(actual,self.expected)

    # test using a testable subclass
    def test_outputs_are_identical(self):
        data = [
            { "username": "admin", "date": "2020-02-20"},
            { "username": "guest", "date": "2020-02-29"},
            { "username": "john", "date": "2020-03-01"}
        ]
        formatter = TestableHtmlFormatter()
        formatter.printReport(data)
        self.assertEqual(formatter.text,self.expected)

