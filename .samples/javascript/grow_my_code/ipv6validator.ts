// After start
class IPv6ParsingError extends Error {
    constructor(message:string) {
        super(message);
        this.name = "IPv6ParsingError";
    }
}
// After end

export class IPv6Address {
    // After start
    address: string;

    // After end
    constructor(input:string) {
        // After start
        this.address = input;
        // After end
    }

    isValid(): boolean {
        throw Error("Not implemented");
    }

    // After start
    private isZero(component:string): boolean {
       return /^0+$/.test(component) 
    }

    private expandComponents(components: string[]): string[] {
        if (components.length==8)
            return components

        var expanded: string[] = [];
        if (components.length<8)
            for (var i=0; i<components.length; i++)
                if (components[i]!='')
                    expanded.push(components[i])
                else
                    for(var j=0; j<8-components.length; j++)
                        expanded.push("0")

        return expanded

    }

    private contractComponent(component:string): string {
        component = component.toLowerCase();
        if (!/^[0-9a-f]+$/.test(component))
            throw new IPv6ParsingError("invalid character")

        if (this.isZero(component))
            return "0";

        if (component.startsWith("0"))
            return this.contractComponent(component.substring(1));

        return component;
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

    // After end
    contract(): string | boolean {
        // Uncomment:      throw Error("Not implemented");
        // After start
        if (this.address =="::")
            return this.address

        var components = this.address.split(":")

        try {
            if (components.length>8)
                throw new IPv6ParsingError("Too many groups")
            
            components = this.expandComponents(components);

            for(let i=0; i<components.length; i++)
                components[i] = this.contractComponent(components[i])   

            var intermediate = components.join(":");
            return this.contractZeros(intermediate);
        } catch (e) {
            if (e instanceof IPv6ParsingError)
                return false;

            throw e;
        }
        // After end
    }
}