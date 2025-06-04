// After start
import createFetchMock from 'vitest-fetch-mock';
// After end
import { expect, test, vi } from 'vitest';
import { PokemonPedia } from "./pokemon2";

// After start
const fetchMocker = createFetchMock(vi);
fetchMocker.enableMocks();
// After end

test("test with mocks", async () => {
    // After start
    var pokemon_response = JSON.stringify(
        {
            "name": "raichu", 
            "species": { "url": "species_url" },
            "types": [{ "type": { "url": "type_url"}}]
        });

    var type_response = JSON.stringify(
        { "move_damage_class": { "name": "special" } }
    );

    var species_response = JSON.stringify(
        { 
            "is_legendary": false, 
            "growth_rate": { "name": "high" } 
        }
    );

    var pokemonPedia = new PokemonPedia(); 
    fetch.mockResponse((req) =>
          req.url.includes("pokemon") ? 
          Promise.resolve(pokemon_response)
          : req.url.includes("type") ? 
          Promise.resolve(type_response)
          : req.url.includes("species") ? 
          Promise.resolve(species_response)
          : Promise.reject(new Error('bad url'))
    );

    var data = await pokemonPedia.investigate("pikachu");
    
    expect(data.name).toEqual("raichu");
    expect(data.damage_class).toEqual("special");
    expect(data.is_legendary).toBeFalsy();
    expect(data.growth_rate).toEqual("high");
    // After end
});
