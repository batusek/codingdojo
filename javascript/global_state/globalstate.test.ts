import { expect, test } from 'vitest';
// import { Configuration, ConfigurationReadyToTest } from './globalstate';
import * as config from './globalstate';

test('should get DB name', () => {
    expect(config.Configuration.getValue('DB_NAME')).to.equal('dev');
});

test('should get DB user', () => {
    expect(config.Configuration.getValue('DB_USER')).to.equal('developer');
});


