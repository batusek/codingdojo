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

    private contractOneGroupOfZeros(input: string, group: string, replacement: string = ""): string|boolean {
        var output = input.replace(group,replacement)
        if (output.length==input.length)
            return false;

        return output
    }

    private contractZeros(output: string): string {
        var result = output;
        var replacements = [
            ["0:0:0:0:0:0:0:0","::"],
            ["0:0:0:0:0:0:0",""],
            ["0:0:0:0:0:0",""],
            ["0:0:0:0:0",""],
            ["0:0:0:0",""],
            ["0:0:0",""],
            ["0:0",""],
        ]

        for (var i=0; i<replacements.length;i++) {
            var contracted = this.contractOneGroupOfZeros(result,replacements[i][0], replacements[i][1])
            if (contracted) {
                result = contracted.toString();
                break;
            }
        }

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