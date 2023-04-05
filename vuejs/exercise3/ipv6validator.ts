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

    contractZeros(output: string): string {
        var result = output;
        result = result.replace("0:0:0:0:0:0:0","")
        result = result.replace("0:0:0:0:0:0","")
        result = result.replace("0:0:0:0:0","")
        result = result.replace("0:0:0:0","")
        result = result.replace("0:0:0","")
        result = result.replace("0:0","")

        if (/^[0-9a-f]:$/.test(result.slice(-2)))
            result = result + ":"

        if (/^:[0-9a-f]$/.test(result.slice(0,2)))
            result = ":" + result
        return result;
    }

    contract(): string {
        var components = this.address.split(":")

        for(let i=0; i<components.length; i++)
            components[i] = this.contractComponent(components[i])   

        var intermediate = components.join(":");
        return this.contractZeros(intermediate);
    }
}