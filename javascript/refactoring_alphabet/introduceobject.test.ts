import { expect, test, describe } from 'vitest';

import { CostCalculator } from './introduceobject';

describe('CostCalculator', () => {
  test('light item small distance', () => {
    const calculator = new CostCalculator();
    expect(calculator.calculateShippingCost(8, 3)).toBe(5.3);
  });

  test('light item large distance', () => {
    const calculator = new CostCalculator();
    expect(calculator.calculateShippingCost(8, 30)).toBe(8);
  });

  test('heavy item small distance', () => {
    const calculator = new CostCalculator();
    expect(calculator.calculateShippingCost(15, 3)).toBe(10.3);
  });

  test('heavy item large distance', () => {
    const calculator = new CostCalculator();
    expect(calculator.calculateShippingCost(15, 30)).toBe(13);
  });
});