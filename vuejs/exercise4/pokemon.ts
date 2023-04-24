import fetch from 'node-fetch'

export class PokemonPedia {
    async investigate(name) {
        const data = await fetch('https://pokeapi.co/api/v2/pokemon/' + name + '/')
        var pokemon = await data.json();

        const data_type = await fetch(pokemon.types[0].type.url);
        var type = await data_type.json()

        const result = {
            pokemon: pokemon,
            type: type,
            name: pokemon.name,
            damage_class: type.move_damage_class.name
          };

        return result;
    }
}