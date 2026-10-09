class Pokemon:

    cantidad_pokemons = 0

    def __init__(self, nombre, tipo, ataque, defensa, salud):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = 1
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud

        Pokemon.cantidad_pokemons += 1
        print(f"¡{self.nombre} ha sido creado! 🐉")

    def __del__(self):
        print(f"{self.nombre} ha sido liberado ✨")

    def entrenar(self, *args):
        
        if len(args) > 3:
            print("Solo puedes indicar hasta 3 mejoras.")
            return

        mejoras = [5, 5, 10]

        for i, valor in enumerate(args):
            if not isinstance(valor, int) or isinstance(valor, bool) or valor < 0:
                print("Las mejoras deben ser enteros no negativos.")
                return
            mejoras[i] = valor

        self.nivel += 1
        self.ataque += mejoras[0]
        self.defensa += mejoras[1]
        self.salud += mejoras[2]

        print(f"\n¡{self.nombre} ha entrenado! 💪")
        print(f"Nuevo nivel: {self.nivel}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Salud: {self.salud}")

    def mostrar_info(self):
        print("\n" + "=" * 30)
        print(f"Nombre:  {self.nombre}")
        print(f"Tipo:    {self.tipo}")
        print(f"Nivel:   {self.nivel}")
        print(f"Ataque:  {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Salud:   {self.salud}")
        print("=" * 30)

    def atacar(self, objetivo):
        if self.salud <= 0:
            print(f"{self.nombre} no puede atacar porque está debilitado.")
            return

        if objetivo.salud <= 0:
            print(f"{objetivo.nombre} ya está debilitado.")
            return

        dano = max(1, self.ataque - objetivo.defensa // 2)
        objetivo.salud = max(0, objetivo.salud - dano)

        print(
            f"\n⚔️ {self.nombre} ataca a {objetivo.nombre} "
            f"y causa {dano} puntos de daño."
        )
        print(f"Salud restante de {objetivo.nombre}: {objetivo.salud}")

        if objetivo.salud == 0:
            print(f"¡{objetivo.nombre} ha sido debilitado!")

    @classmethod
    def total_pokemons(cls):
        
        print(f"\nTotal de Pokémon creados: {cls.cantidad_pokemons}")
