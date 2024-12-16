import { expect, describe, test } from 'vitest';

import { PriceCalculator, Item } from './extractmethod';
import { PriceCalculatorAfter } from './extractmethod';

describe('PriceCalculator', () => {
  const createCalculator = () => new PriceCalculator(0.1);

  test('zero list means zero price', () => {
    const calculator = createCalculator();
    expect(calculator.calculateTotalPrice([])).toBe(0);
  });

  test('a taxable item uses price quanity and tax', () => {
    const item: Item = new Item(4, 2, true);
    const calculator = createCalculator();
    expect(calculator.calculateTotalPrice([item])).toBe(8.8);
  });

  test('a non-taxable item ignores tax', () => {
    const item: Item = new Item(4, 2, false);
    const calculator = createCalculator();
    expect(calculator.calculateTotalPrice([item])).toBe(8);
  });

  test('multiple items are summed non-taxable item ignores tax', () => {
    const item1: Item = new Item(4, 2, false);
    const item2: Item = new Item(3, 3, false);
    const calculator = createCalculator();
    expect(calculator.calculateTotalPrice([item1, item2])).toBe(17);
  });
});

