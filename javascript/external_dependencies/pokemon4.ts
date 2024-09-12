import fetch from 'node-fetch'

export interface PokemonAPIService {
    fetch(url: string): Promise<any>;
}

class DefaultPokemonAPIService implements PokemonAPIService {
    public async fetch(url: string): Promise<any> {
        return await fetch(url);
    }
}

export class PokemonPedia {
    apiService: PokemonAPIService

    constructor(apiService?: PokemonAPIService) {
        this.apiService = apiService || new DefaultPokemonAPIService();
    }

    async investigate(name: string) {
        // See https://pokeapi.co/docs/v2 for API description
        const data_pokemon = await this.apiService.fetch('https://pokeapi.co/api/v2/pokemon/' + name + '/')
        var pokemon = await data_pokemon.json();

        const data_type = await this.apiService.fetch(pokemon.types[0].type.url);
        var type = await data_type.json()

        const data_species = await this.apiService.fetch(pokemon.species.url);
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