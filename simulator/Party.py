from Pokemon import Pokemon


class Party:
    def __init__(self):
        self._party = []
        self.MAX_SIZE = 6
        self.MIN_SIZE = 1
    
    @property
    def party(self):
        return self._party
    
    def add(self, pokemon: Pokemon) -> None:
        if len(self._party) < self.MAX_SIZE:
            self._party.append(pokemon)
    
    def remove(self, pokemon: Pokemon) -> None:
        if len(self._party) > self.MIN_SIZE:
            for i, pkmn in enumerate(self._party):
                if pkmn == pokemon:
                    del self._party[i]
                    break