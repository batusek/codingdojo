// TODO: Change method signature to 
// distanceFromBeginning(point: Point): number
// Do it in _multiple_ steps in such a way that your tests NEVER fail

export class CoordinateHelper {
    static distance_from_beginning(x:number, y:number): number {
      return Math.sqrt(x * x + y * y);
    }
  }
  
  // After start
export class Point {
    x: number
    y: number

    constructor(x: number, y: number) {
      this.x = x;
      this.y = y;
    }
  }
  
  export class CoordinateHelperAfter {
    static distance_from_beginning(point: Point) {
      return Math.sqrt(point.x * point.x + point.y * point.y);
    }
  }
  // After end