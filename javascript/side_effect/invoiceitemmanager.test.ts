import { expect, test, describe, beforeEach } from 'vitest';
import { readFileSync, unlinkSync } from 'fs';

import { InvoiceItemManager } from './invoiceitemmanager';

describe('InvoiceItemManager', () => {
    beforeEach(() => {
        try {
            unlinkSync('invoice_items.csv'); // Remove file before each test
        } catch (err) {
            if (err.code === 'ENOENT') { // Ignore if file doesn't exist
            // File not found, proceed
            } else {
            throw err; // Re-throw other errors
            }
        }
    });

  test('calculation integration test', () => {
    const manager = new InvoiceItemManager();
    manager.saveItemTotalAmount(1, 3, 0.2);

    const text = readFileSync('invoice_items.csv', 'utf-8'); // Read file contents
    const total = parseFloat(text.split(';').slice(-1)[0]);

    expect(total).toBeCloseTo(3.6, 2);
  });
});

