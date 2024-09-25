import unittest
import os
from external_dependencies.htmlformatter import *

# After start
from unittest.mock import *
# After end

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
        """ test using a blackbox test that accesses filesystem  """
        # After start
        data = [
            { "username": "admin", "date": "2020-02-20"},
            { "username": "guest", "date": "2020-02-29"},
            { "username": "john", "date": "2020-03-01"}
        ]
        HtmlFormatter().printReport(data)

        f = open("output.html","r")
        actual = f.read()
        self.assertEqual(actual,self.expected)
        # After end

class HtmlFormatterTestWithMocks(unittest.TestCase):
    # Uncommment:    def test_writes_to_file(self):
    # After start
    @patch('external_dependencies.htmlformatter.open')
    def test_writes_to_file(self, patch_open):
    # After end
        """test using mocks"""
        # After start
        data = [
            { "username": "admin", "date": "2020-02-20"}
        ]

        mock_file = Mock()
        patch_open.return_value = mock_file
        HtmlFormatter().printReport(data)
        calls = [ 
            call("<html><body>\n"), 
            call('<table border="1">\n'), 
            call("<tr><th>Username</th><th>Last login</th></tr>"),
            call("<tr>\n"),
            call('<td>admin</td>'),
            call('<td>2020-02-20</td>'),
            call("</tr>\n"),
            call("</tr></table>\n"),
            call("</body></html>\n")
            ]
        mock_file.write.assert_has_calls(calls)
        mock_file.close.assert_called()
        # After end

# After start
class TestableHtmlFormatter(HtmlFormatterReadyToSubclass):
    def __init__(self):
        self.text = ""

    def openFile(self):
        pass
    
    def writeToFile(self,f,text):
        self.text += text

    def closeFile(self,f):
        pass
# After end

class HtmlFormatterTestSubclassed(unittest.TestCase):
    def setUp(self):
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

    def test_outputs_are_identical(self):
        """ test using a testable subclass """
        # After start
        data = [
            { "username": "admin", "date": "2020-02-20"},
            { "username": "guest", "date": "2020-02-29"},
            { "username": "john", "date": "2020-03-01"}
        ]
        formatter = TestableHtmlFormatter()
        formatter.printReport(data)
        self.assertEqual(formatter.text,self.expected)
        # After end
