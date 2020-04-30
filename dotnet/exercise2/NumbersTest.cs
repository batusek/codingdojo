using Xunit;

namespace Numbers 
{
    public class NumbersTest
    {
        [Fact]
        public void OneReadsAsOne()
        {
            Assert.Equal("one",NumbersInWords.PrintNumber(1));
        }

        [Fact]
        public void TwoReadsAsTwo()
        {
            Assert.Equal("two",NumbersInWords.PrintNumber(2));
        }
    }

}