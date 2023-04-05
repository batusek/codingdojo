export class IPv6Address {
    address: string;

    constructor(input:string) {
        this.address = input;
    }

    isValid(): boolean {
        throw Error("Not implemented");
    }

    private isZero(component:string): boolean {
       return /^0+$/.test(component) 
    }

    contract(): string {
        var components = this.address.split(":")

        for(let i=0; i<components.length; i++)
            if (this.isZero(components[i]))
                components[i] = "0"
        return components.join(":");
    }
}