export class NumbersInWords {
    static printNumber(number: number) {
        const ones = ["zero","one","two","threee","four","five","six","seven","eight","nine"];
        return ones[number];
    }
}