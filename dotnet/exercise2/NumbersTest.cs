using Xunit;

namespace Numbers 
{
    public class NumbersTest
    {
        [Fact]
        public void NormalYearIsNotLeapYear()
        {
            Assert.Equal("one",Numbers.PrintNumber(1));
        }
    }

}