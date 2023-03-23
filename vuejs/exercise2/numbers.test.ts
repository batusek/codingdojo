import { expect, test } from 'vitest'
import { NumbersInWords } from "./numbers";

test.each([
    [1, "one"],
    [2, "two"],
    [9, "nine"],
    [19, "nineteen"],
    [20, "twenty"],
    [21, "twenty one"],
    [99, "ninety nine"]
])("%i prints as %s", (number, expected) => {
    expect(NumbersInWords.printNumber(number)).toBe(expected);
})
