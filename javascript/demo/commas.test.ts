import { expect, test } from 'vitest'
import { formatNumber } from "./commas";

test("one prints without comma", () => {
    expect(formatNumber(1)).toEqual("1");
})

test("ten prints without comma", () => {
    expect(formatNumber(10)).toEqual("10");
})

test("hundred prints without comma", () => {
    expect(formatNumber(100)).toEqual("100");
})

test("thousand prints with one comma", () => {
    expect(formatNumber(1000)).toEqual("1,000");
})