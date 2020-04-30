using Xunit;

namespace Numbers 
{
    public class NumbersTest
    {
        [Theory]
        [InlineData(1, "one")]
        [InlineData(2, "two")]
        [InlineData(9, "nine")]
        public void PrintNumberUniversalTest(int input, string expected)
        {
            Assert.Equal(expected,NumbersInWords.PrintNumber(input));
        }
    }

}