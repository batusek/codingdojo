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
    fetch.mockResponse(JSON.stringify(
        {
            "name": "raichu", 
            "species": { "url": "species_url" },
            "types": [{ "type": { "url": "type_url"}}]
        })
    );

    var pedia = new PokemonPedia2(); 
    var data = await pedia.investigate("pikachu");

    // var data = fetchMocker.mockResponseOnce(
    //     () => pedia.investigate("pikachu")
    //         .then((res) => ({"name": "raichu"}))
    // );
    console.log(data);
    
    expect(data.name).toEqual("raichu");
    expect(data.damage_class).toEqual("special");
    expect(data.is_legendary).toBeFalsy();
    expect(data.growth_rate).toEqual("medium");
});
