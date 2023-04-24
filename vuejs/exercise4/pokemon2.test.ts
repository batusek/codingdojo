import { expect, test, vi } from 'vitest';
import { PokemonPedia } from "./pokemon";

global.fetch = vi.fn()

function createFetchResponse(data) {
    return { json: () => new Promise((resolve) => resolve(data)) }
  }

test("test with mocks", async () => {
    // const spy = vi.spyOn(global,'fetch').mockResolvedValue({"name": "pikachu"})
    fetch.mockResolvedValue(createFetchResponse({"name": "pikachu"}));

    var pedia = new PokemonPedia(); 
    var data = await pedia.investigate("pikachu")
    
    expect(data.name).toEqual("pikachu");
    expect(data.damage_class).toEqual("special");
    expect(data.is_legendary).toBeFalsy();
    expect(data.growth_rate).toEqual("medium");
});

