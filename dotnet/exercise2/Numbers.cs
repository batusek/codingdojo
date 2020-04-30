using System;
using System.Collections.Generic;

namespace Numbers
{
    public class NumbersInWords
    {
        public static String PrintNumber(int number)
        {
            var ones = new List<String>() { "one", "two" };

            return ones[number-1];
        }
    }
}
