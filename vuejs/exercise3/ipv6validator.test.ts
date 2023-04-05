import { expect, test } from 'vitest'
import { IPv6Address } from "./ipv6validator"

test("happy path eight groups filled with non zero octets", () => {
    let input = "123f:123f:123f:123f:123f:123f:123f:123f"
    expect(new IPv6Address(input).contract()).toEqual(input);
});

test("double colon is a valid address that cannot be contracted", () => {
    let input = "::"
    expect(new IPv6Address(input).contract()).toEqual(input);
});

test("a group of four zeros should be contracted to one zero", () => {
    let input = "123f:123f:123f:123f:123f:123f:0000:123f"
    expect(new IPv6Address(input).contract()).toEqual("123f:123f:123f:123f:123f:123f:0:123f");
});

test("a group of three zeros should be contracted to one zero", () => {
    let input = "123f:123f:123f:123f:123f:123f:000:123f"
    expect(new IPv6Address(input).contract()).toEqual("123f:123f:123f:123f:123f:123f:0:123f");
});

test("leading zeros are removed", () => {
    let input = "123f:123f:123f:123f:123f:123f:023f:123f"
    expect(new IPv6Address(input).contract()).toEqual("123f:123f:123f:123f:123f:123f:23f:123f");
});

test("uppercase converted to lowercase", () => {
    let input = "123F:123F:123F:123F:123F:123F:123F:123F"
    expect(new IPv6Address(input).contract()).toEqual("123f:123f:123f:123f:123f:123f:123f:123f");
});

test("two subsequent zero components are contracted to double colon", () => {
    let input = "123f:123f:123f:123f:123f:0000:0000:123f"
    expect(new IPv6Address(input).contract()).toEqual("123f:123f:123f:123f:123f::123f");
});

test("three subsequent zero components are contracted to double colon", () => {
    let input = "123f:123f:123f:123f:0000:0000:0000:123f"
    expect(new IPv6Address(input).contract()).toEqual("123f:123f:123f:123f::123f");
});

test("four subsequent zero components are contracted to double colon", () => {
    let input = "123f:123f:123f:0000:0000:0000:0000:123f"
    expect(new IPv6Address(input).contract()).toEqual("123f:123f:123f::123f");
});

test("five subsequent zero components at the end are contracted to double colon", () => {
    let input = "123f:123f:123f:0000:0000:0000:0000:0000"
    expect(new IPv6Address(input).contract()).toEqual("123f:123f:123f::");
});

test("six subsequent zero components at the start are contracted to double colon", () => {
    let input = "0000:0000:0000:0000:0000:0000:123f:123f"
    expect(new IPv6Address(input).contract()).toEqual("::123f:123f");
});

test("seven subsequent zero components are contracted to double colon", () => {
    let input = "0000:0000:0000:0000:0000:0000:0000:123f"
    expect(new IPv6Address(input).contract()).toEqual("::123f");
});
