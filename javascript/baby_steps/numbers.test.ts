import { expect, test } from 'vitest'
import { NumbersInWords } from "./numbers";

// After start
test.each([
    [1, "one solution"],
    [2, "two"],
    [9, "nine"],
    [19, "nineteen"],
    [20, "twenty"],
    [21, "twenty one"],
    [99, "ninety nine"],
    [100, "one hundred"],
    [135, "one hundred and thirty five"],
    [987, "nine hundred and eighty seven"]
])("%i prints as %s", (number, expected) => {
    expect(NumbersInWords.printNumber(number)).toBe(expected);
})
// After end

test("1 prints as one", () => {
    expect(NumbersInWords.printNumber(1)).toBe("one");
})