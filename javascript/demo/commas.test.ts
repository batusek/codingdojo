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

test("ten millions prints with two commas", () => {
    expect(formatNumber(10000000)).toEqual("10,000,000");
})

test("thirty five millions prints with two commas", () => {
    expect(formatNumber(35353535)).toEqual("35,353,535");
})