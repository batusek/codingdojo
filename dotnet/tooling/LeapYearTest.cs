using Xunit;

namespace LeapYear 
{
    public class LeapYearTest
    {
        [Theory]
        [InlineData(1789, false)]
        [InlineData(1788, true)]
        [InlineData(1800, false)]
        [InlineData(2000, true)]
        public void LeapYearTestCases(int year, bool expected)
        {
            Assert.Equal(expected,LeapYear.IsLeapYear(year));
        }
    }

}