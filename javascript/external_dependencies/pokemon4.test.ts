import { expect, test } from 'vitest'
import { PokemonPedia, PokemonAPIService } from "./pokemon4";

class TestPokemonApiService implements PokemonAPIService {
    urls: Map<string,string>;

    constructor(){
        this.urls = new Map();
    }

    public registerUri(uri: string, result: string) {
        this.urls.set(uri,result);
    }

    public async fetch(url: string) {
        for (const [uri, result] of this.urls.entries()) {
            if (url.includes(uri))
                return { json: async () => JSON.parse(result) }
        }
        return Promise.reject(new Error('bad url ' + url));
    }
}

test("integration test", async () => {
    var apiService = new TestPokemonApiService()
    apiService.registerUri("pokemon", JSON.stringify(
        {
            "name": "raichu", 
            "species": { "url": "species_url" },
            "types": [{ "type": { "url": "type_url"}}]
        }));

    apiService.registerUri("type", JSON.stringify(
        { "move_damage_class": { "name": "special" } }
    ));
    
    apiService.registerUri("species", JSON.stringify(
        { 
            "is_legendary": false, 
            "growth_rate": { "name": "high" } 
        }
    ));
    var pokemonPedia = new PokemonPedia(apiService); 
    var data = await pokemonPedia.investigate("pikachu")

    expect(data.name).toEqual("raichu");
    expect(data.damage_class).toEqual("special");
    expect(data.is_legendary).toBeFalsy();
    expect(data.growth_rate).toEqual("high");
});

