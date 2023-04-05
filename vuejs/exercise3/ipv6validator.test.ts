import { expect, test } from 'vitest'
import { IPv6Validator } from "./ipv6validator"

test("happy path eight groups filled with non zero octets", () => {
    let input = "123f:123f:123f:123f:123f:123f:123f:123f"
    expect(IPv6Validator.contract(input)).toEqual(input);
});

test("double colon is a valid address that cannot be contracted", () => {
    let input = "::"
    expect(IPv6Validator.contract(input)).toEqual(input);
});

test("a group of four zeros should be contracted to one zero", () => {
    let input = "123f:123f:123f:123f:123f:123f:0000:123f"
    expect(IPv6Validator.contract(input)).toEqual("123f:123f:123f:123f:123f:123f:0:123f");
});

test("a group of three zeros should be contracted to one zero", () => {
    let input = "123f:123f:123f:123f:123f:123f:000:123f"
    expect(IPv6Validator.contract(input)).toEqual("123f:123f:123f:123f:123f:123f:0:123f");
});
