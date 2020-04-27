using Xunit;

namespace LeapYear 
{
    public class LeapYearTest
    {
        [Fact]
        public void NormalYearIsNotLeapYear()
        {
            Assert.False(LeapYear.IsLeapYear(1789));
        }
    }

}