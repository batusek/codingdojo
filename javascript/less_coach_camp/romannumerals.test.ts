import { expect, test, describe } from 'vitest'
import { romanNumeral } from "./romannumerals";

describe("Roman Numerals", () => {
  test("1 -> I", () => {
    expect(romanNumeral(1)).toEqual("I");
  })
  
test("2 -> II", () => {
    expect(romanNumeral(2)).toEqual("II");
  })
test("3 ->  III", () => {
    expect(romanNumeral(3)).toEqual("III");
  })
test("4-> IV", () => {
  expect(romanNumeral(4)).toEqual("IV");
})
test("5-> V", () => {
  expect(romanNumeral(5)).toEqual("V");
})

})
