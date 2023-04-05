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

    private contractComponent(component:string): string {
        if (this.isZero(component))
            return "0";

        if (component.startsWith("0"))
            return this.contractComponent(component.substring(1));

        return component.toLowerCase();
    }

    contract(): string {
        var components = this.address.split(":")

        for(let i=0; i<components.length; i++)
            components[i] = this.contractComponent(components[i])
        return components.join(":");
    }
}