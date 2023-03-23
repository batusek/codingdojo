import { expect, test } from 'vitest'
import { NumbersInWords } from "./numbers";

test("1 prints as one", () => {
    expect(NumbersInWords.printNumber(1)).toBe("one");
})

test("2 prints as two", () => {
    expect(NumbersInWords.printNumber(2)).toBe("two");
})
