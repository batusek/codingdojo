import { expect, test } from 'vitest';
// import { Configuration, ConfigurationReadyToTest } from './globalstate';
import * as config from './globalstate';

test('should get DB name', () => {
    expect(config.Configuration.getValue('DB_NAME')).to.equal('dev');
});

test('should get DB user', () => {
    expect(config.Configuration.getValue('DB_USER')).to.equal('developer');
});


// After start
class TestableConfiguration extends config.ConfigurationReadyToTest {
    config: Record<string, any>;

    constructor() {
        super();
        this.config = {};
    }

    protected getValueInstance(key: string): string | undefined {
        return this.config['Database'][key]
    }
}

test('should get DB name with custom instance', () => {
    const configuration = new TestableConfiguration();
    configuration.config['Database'] = {
        DB_NAME: 'internalDB',
        DB_USER: 'internalUser',
    };
    config.ConfigurationReadyToTest.setInstance(configuration);
    expect(config.ConfigurationReadyToTest.getValue('DB_NAME')).to.equal('internalDB');
});

test('should get DB user with custom instance', () => {
    const configuration = new TestableConfiguration();
    configuration.config['Database'] = {
        DB_NAME: 'internalDB',
        DB_USER: 'internalUser',
    };
    config.ConfigurationReadyToTest.setInstance(configuration);
    expect(config.ConfigurationReadyToTest.getValue('DB_USER')).to.equal('internalUser');
});
// After end
