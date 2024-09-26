import fetch from 'node-fetch'
import { expect, test } from 'vitest'
import { PokemonPedia } from "./pokemon";

globalThis.fetch = fetch; // we use a default browser fetch for fetching

test("integration test", async () => {
    // Uncomment:   expect(true).toBeFalsy();
    // After start
    var pokemonPedia = new PokemonPedia(); 
    var data = await pokemonPedia.investigate("pikachu")

    expect(data.name).toEqual("pikachu");
    expect(data.damage_class).toEqual("special");
    expect(data.is_legendary).toBeFalsy();
    expect(data.growth_rate).toEqual("medium");
    // After end
});

