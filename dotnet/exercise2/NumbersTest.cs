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

    }

}