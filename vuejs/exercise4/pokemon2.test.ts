import createFetchMock from 'vitest-fetch-mock';
import { vi } from 'vitest';

const fetchMocker = createFetchMock(vi);
fetchMocker.enableMocks();

import { expect, test } from 'vitest';
import { PokemonPedia2 } from "./pokemon2";


function createFetchResponse(data) {
    return { json: () => new Promise((resolve) => resolve(data)) }
  }

test("test with mocks", async () => {
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

    // fetch.mockResponse(pokemon_response);

    var pedia = new PokemonPedia2(); 
    fetch.mockResponse((req) =>
          req.url.includes("pokemon") ? 
          Promise.resolve(pokemon_response)
          : req.url.includes("type") ? 
          Promise.resolve(type_response)
          : req.url.includes("species") ? 
          Promise.resolve(species_response)
          : Promise.reject(new Error('bad url'))
    );

    var data = await pedia.investigate("pikachu");

    // var data = fetchMocker.mockResponseOnce(
    //     () => pedia.investigate("pikachu")
    //         .then((res) => ({"name": "raichu"}))
    // );
    console.log(data);
    
    expect(data.name).toEqual("raichu");
    expect(data.damage_class).toEqual("special");
    expect(data.is_legendary).toBeFalsy();
    expect(data.growth_rate).toEqual("high");
});
