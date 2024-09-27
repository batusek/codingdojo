import { expect, test } from 'vitest';
import { Configuration, ConfigurationReadyToTest } from './globalstate';

test('should get DB name', () => {
    expect(Configuration.getValue('DB_NAME')).to.equal('dev');
});

test('should get DB user', () => {
    expect(Configuration.getValue('DB_USER')).to.equal('developer');
});


// After start
class TestableConfiguration extends ConfigurationReadyToTest {
    config

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
    ConfigurationReadyToTest.setInstance(configuration);
    expect(ConfigurationReadyToTest.getValue('DB_NAME')).to.equal('internalDB');
});

test('should get DB user with custom instance', () => {
    const configuration = new TestableConfiguration();
    configuration.config['Database'] = {
        DB_NAME: 'internalDB',
        DB_USER: 'internalUser',
    };
    ConfigurationReadyToTest.setInstance(configuration);
    expect(ConfigurationReadyToTest.getValue('DB_USER')).to.equal('internalUser');
});
// After end
