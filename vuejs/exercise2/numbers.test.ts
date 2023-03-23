import { expect, test } from 'vitest'
import { NumbersInWords } from "./numbers";

test("1 prints as one", () => {
    expect(NumbersInWords.printNumber(1)).toBe("one");
})

