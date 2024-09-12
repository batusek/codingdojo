class HtmlFormatter:
    def printReport(self, data :list):
        f = open("output.html","w")

        f.write("<html><body>\n")
        f.write('<table border="1">\n')
        f.write("<tr><th>Username</th><th>Last login</th></tr>")
        for row in data:
            f.write("<tr>\n")
            f.write(f'<td>{row["username"]}</td>')
            f.write(f'<td>{row["date"]}</td>')
            f.write("</tr>\n")


        f.write("</tr></table>\n")
        f.write("</body></html>\n")
        f.close()


if __name__ == '__main__':
    data = [
        { "username": "admin", "date": "2020-02-20"},
        { "username": "guest", "date": "2020-02-29"},
        { "username": "john", "date": "2020-03-01"}
    ]
    HtmlFormatter().printReport(data)
