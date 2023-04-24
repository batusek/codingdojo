import { expect, test } from 'vitest'
import { PokemonPedia } from "./pokemon3";

class TestablePokemonPedia extends PokemonPedia {
    urls: Map<string,string>;

    constructor(){
        super();
        this.urls = new Map();
    }

    public registerUri(uri: string, result: string) {
        this.urls.set(uri,result);
    }

    protected async fetchUrl(url) {
        for (const [uri, result] of this.urls.entries()) {
            if (url.includes(uri))
                return { 
                        json: async () => JSON.parse(result)
                    }
        }
        return Promise.reject(new Error('bad url ' + url));
    }
}

test("testing with inheritance", async () => {
    var pedia = new TestablePokemonPedia(); 
    pedia.registerUri("pokemon", JSON.stringify(
        {
            "name": "raichu", 
            "species": { "url": "species_url" },
            "types": [{ "type": { "url": "type_url"}}]
        }));

    pedia.registerUri("type", JSON.stringify(
        { "move_damage_class": { "name": "special" } }
    ));
    
    pedia.registerUri("species", JSON.stringify(
        { 
            "is_legendary": false, 
            "growth_rate": { "name": "high" } 
        }
    ));
    var data = await pedia.investigate("pikachu")

    expect(data.name).toEqual("raichu");
    expect(data.damage_class).toEqual("special");
    expect(data.is_legendary).toBeFalsy();
    expect(data.growth_rate).toEqual("high");
});

