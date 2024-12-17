import { expect, test } from 'vitest'
import { formatNumber } from "./commas";

test("one prints without comma", () => {
    expect(formatNumber(1)).toEqual("1");
})

test("ten prints without comma", () => {
    expect(formatNumber(10)).toEqual("10");
})