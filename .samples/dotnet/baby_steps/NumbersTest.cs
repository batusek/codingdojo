using Xunit;

// Kata instructions: https://www.codewars.com/kata/54fa4e210609868fce0002bf

namespace Numbers 
{
    public class NumbersTest
    {
        [Theory]
        [InlineData(1, "one")]
        [InlineData(2, "two")]
        [InlineData(19, "nineteen")]
        [InlineData(20, "twenty")]
        [InlineData(21, "twenty one")]
        [InlineData(99, "ninety nine")]
        [InlineData(100, "one hundred")]
        [InlineData(999, "nine hundred and ninety nine")]
        public void PrintNumberUniversalTest(int input, string expected)
        {
            Assert.Equal(expected,new NumbersInWords().PrintNumber(input));
        }
    }

}