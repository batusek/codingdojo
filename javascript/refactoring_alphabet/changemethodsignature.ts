// TODO: Change method signature to 
// distanceFromBeginning(point: Point): number
// Do it in _multiple_ steps in such a way that your tests NEVER fail

export class CoordinateHelper {
    static distance_from_beginning(x:number, y:number): number {
      return Math.sqrt(x * x + y * y);
    }
  }
  
