export class NumbersInWords {
    static printNumber(number: number) {
        const ones = ["one","two"];
        return ones[number-1];
    }
}