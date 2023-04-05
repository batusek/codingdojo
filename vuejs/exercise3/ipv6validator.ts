export class IPv6Validator {
    static isValid(input: string): boolean {
        throw Error("Not implemented");
    }

    static isZero(component:string): boolean {
       return /^0+$/.test(component) 
    }

    static contract(input: string): string {
        var components = input.split(":")

        for(let i=0; i<components.length; i++)
            if (IPv6Validator.isZero(components[i]))
                components[i] = "0"
        return components.join(":");
    }
}