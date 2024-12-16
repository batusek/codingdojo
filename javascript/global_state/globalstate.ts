import { config } from 'dotenv';

export class Configuration {
  static getValue(key: string): string | undefined {
    config({ path: 'global_state/.env' });
    return process.env[key];
  }
}

