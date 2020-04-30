using System;
using System.Collections.Generic;
using System.Text;

namespace Numbers
{
    public class NumbersInWords
    {
        private String PrintOnes(int number)
        {
            var ones = new List<String>() { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" };

            return ones[number];

        }
        public String PrintNumber(int number)
        {
            var tens = new List<String>() { "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" };
            var result = new StringBuilder();

            if (number>=100) {
                result.Append(PrintOnes(number/100)).Append(" hundred");
                var remainder = number % 100;
                if (remainder>0) 
                    result.Append(" and ").Append(PrintNumber(remainder));
            } else if (number>=20) {
                result.Append(tens[number/10]);
                var remainder = number % 10;
                if (remainder > 0)
                    result.Append(" ").Append(PrintOnes(remainder));
            } else {
                result.Append(PrintOnes(number));
            }
            
            return result.ToString();
        }
    }
}
