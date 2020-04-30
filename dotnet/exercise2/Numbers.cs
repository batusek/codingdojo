using System;
using System.Collections.Generic;
using System.Text;

namespace Numbers
{
    public class NumbersInWords
    {
        private static String PrintOnes(int number)
        {
            var ones = new List<String>() { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" };

            return ones[number];

        }
        public static String PrintNumber(int number)
        {
            var tens = new List<String>() { "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" };
            var result = new StringBuilder();

            if (number<20) {
                result.Append(PrintOnes(number));
            } else {
                result.Append(tens[number/10]);
                var remainder = number % 10;
                if (remainder > 0)
                    result.Append(" ").Append(PrintOnes(remainder));
            }
            
            return result.ToString();
        }
    }
}
