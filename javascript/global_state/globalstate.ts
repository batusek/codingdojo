import { config } from 'dotenv';

export class Configuration {
  static getValue(key: string): string | undefined {
    config({ path: 'global_state/.env' });
    return process.env[key];
  }
}

// After start
// Singleton Pattern
export class ConfigurationAsSingleton {
  static instance(): ConfigurationAsSingleton {
    if (!this._instance) {
      this._instance = new Configuration();
    }
    return this._instance;
  }

  getValue(key: string): string | undefined {
    return process.env[key];
  }

  static get(key: string): string | undefined {
    return this.instance().getValue(key);
  }
}

// Configuration for Testing (After start)
export class ConfigurationReadyToTest {
  static instance(): ConfigurationReadyToTest {
    if (!this._instance) {
      this._instance = new Configuration();
    }
    return this._instance;
  }

  static setInstance(instance: ConfigurationReadyToTest): void {
    this._instance = instance;
  }

  getValue(key: string): string | undefined {
    return process.env[key];
  }

  static get(key: string): string | undefined {
    return this.instance().getValue(key);
  }
}
// After end