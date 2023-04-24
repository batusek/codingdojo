import { expect, test } from 'vitest'
import { PokemonPedia } from "./pokemon";

test("empty test", async () => {
    var pedia = new PokemonPedia(); 
    var data = await pedia.investigate("pikachu")
    
    expect(data.name).toEqual("pikachu");
    expect(data.damage_class).toEqual("special");
    expect(data.is_legendary).toBeFalsy();
    expect(data.growth_rate).toEqual("medium");
});

