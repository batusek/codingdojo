using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace Formatters
{
    public class HtmlFormatter
    {
        public static void PrintReport(List<(String username, String date)> data)
        {
            using (System.IO.StreamWriter fs = new System.IO.StreamWriter(System.IO.File.Create("output.html")))
            {
                fs.WriteLine("<html><body>");
                fs.WriteLine("<table border=\"1\">");
                fs.WriteLine("<tr><th>Username</th><th>Last login</th></tr>");
                foreach(var row in data)
                {
                    fs.WriteLine("<tr>");
                    fs.WriteLine($"<td>{row.username}</td>");
                    fs.WriteLine($"<td>{row.date}</td>");
                    fs.WriteLine("</tr>");
                }

                fs.WriteLine("</tr></table>");
                fs.WriteLine("</body></html>");
            }            
        }

        public static void Main(String[] argv) {
            var data = new List<(String username, String date)> 
            {
                ( "admin", "2020-02-20" ),
                ( "guest", "2020-02-29" ),
                ( "john", "2020-03-01" )
            };
            HtmlFormatter.PrintReport(data);
        }
    }
}
