import { expect, test, describe } from 'vitest';
import { statSync } from 'fs';

import { Exporter } from './replaceconstructor';

describe('Exporter', () => {
  test('data are written to storage', () => {
    const exporter = new Exporter();
    exporter.export(new Uint8Array([1, 2, 3, 4, 5]));

    const fileSize = statSync('export.csv').size;
    expect(fileSize).toBe(5);
  });
});