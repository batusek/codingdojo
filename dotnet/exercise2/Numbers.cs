using System;
using System.Collections.Generic;

namespace Numbers
{
    public class NumbersInWords
    {
        public static String PrintNumber(int number)
        {
            var ones = new List<String>() { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };

            return ones[number];
        }
    }
}
