import { expect, test, vi } from 'vitest';
import { PokemonPedia } from "./pokemon2";

test("test with mocks", async () => {

    const nameResponse = {
        name: "machop's name",
        types: [
            {
                type: {
                    url: "some-url",
                }
            }
        ],
        species: {
            url: "spec-url",
        }
	};
    const typeResponse = {
        move_damage_class: {
            name: "dmg",
        },
	};
    const speciesResponse = {
        is_legendary: false,
        growth_rate: {
            name: "gr",
        },
	};

    global.fetch = vi.fn().mockImplementationOnce(() =>
        Promise.resolve({
          json: () => Promise.resolve(nameResponse),
        })
      ).mockImplementationOnce(() =>
        Promise.resolve({
          json: () => Promise.resolve(typeResponse),
        })
      ).mockImplementationOnce(() =>
        Promise.resolve({
          json: () => Promise.resolve(speciesResponse),
        })
      );

    const pedia = new PokemonPedia();
       
    const machop = await pedia.investigate("machop");
    expect(machop.damage_class).equals("dmg");
    expect(machop.growth_rate).equals("gr");
    expect(machop.is_legendary).toBeFalsy();
    expect(machop.name).equals("machop's name");
});
