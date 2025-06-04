// For testing with mocks, no change in the production code is needed
export class PokemonPedia {
    async investigate(name: string) {
        // See https://pokeapi.co/docs/v2 for API description
        const data_pokemon = await fetch('https://pokeapi.co/api/v2/pokemon/' + name + '/')
        var pokemon = await data_pokemon.json();

        const data_type = await fetch(pokemon.types[0].type.url);
        var type = await data_type.json()

        const data_species = await fetch(pokemon.species.url);
        var species = await data_species.json()

        const result = {
            name: pokemon.name,
            damage_class: type.move_damage_class.name,
            is_legendary: species.is_legendary,
            growth_rate: species.growth_rate.name
          };

        return result;
    }
}