import { expect, test, describe } from 'vitest';

import * as changemethod from './changemethodsignature';

describe('CoordinateHelper', () => {
  test('0,0 is the beginning of the coordinate system', () => {
    expect(changemethod.CoordinateHelper.distance_from_beginning(0, 0)).to.equal(0);
  });

  test('1,1 distance is equal to the square root of 2', () => {
    expect(changemethod.CoordinateHelper.distance_from_beginning(1, 1)).to.be.closeTo(1.41, 2);
  });
});

// After start
describe('CoordinateHelperAfter', () => {
  test('0,0 is the beginning of the coordinate system', () => {
    expect(changemethod.CoordinateHelperAfter.distance_from_beginning(new changemethod.Point(0, 0))).to.equal(0);
  });

  test('1,1 distance is equal to the square root of 2', () => {
    expect(changemethod.CoordinateHelperAfter.distance_from_beginning(new changemethod.Point(1, 1))).to.be.closeTo(1.41, 2);
  });
});
// After end