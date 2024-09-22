class HtmlFormatter:
    def printReport(self, data :list):
        f = self.openFile()

        self.writeToFile(f, "<html><body>\n")
        self.writeToFile(f, '<table border="1">\n')
        self.writeToFile(f, "<tr><th>Username</th><th>Last login</th></tr>")
        for row in data:
            self.writeToFile(f, "<tr>\n")
            self.writeToFile(f, f'<td>{row["username"]}</td>')
            self.writeToFile(f, f'<td>{row["date"]}</td>')
            self.writeToFile(f, "</tr>\n")


        self.writeToFile(f, "</tr></table>\n")
        self.writeToFile(f, "</body></html>\n")
        self.closeFile(f)

    def openFile(self):
        f = open("output.html","w")
        return f

    def writeToFile(self, f, text):
        f.write(text)

    def closeFile(self, f):
        f.close()


if __name__ == '__main__':
    data = [
        { "username": "admin", "date": "2020-02-20"},
        { "username": "guest", "date": "2020-02-29"},
        { "username": "john", "date": "2020-03-01"}
    ]
    HtmlFormatter().printReport(data)
