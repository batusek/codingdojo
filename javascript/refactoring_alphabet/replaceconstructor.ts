import { writeFileSync } from 'fs';

// Simulating cloud storage with a file (imagine an actual cloud storage implementation)
class CloudStorage {
  constructor(public name: string) {}

  write(data: Uint8Array): void {
    writeFileSync(this.name, data);
  }
}

export class Exporter {
  storage: CloudStorage;

  constructor() {
    // TODO: replace a direct constructor call with a factory call
    this.storage = new CloudStorage('export.csv');
  }

  export(data: Uint8Array): void {
    this.storage.write(data);
  }
}

