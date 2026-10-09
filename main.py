from clases.pokemon import Pokemon


pokemons = []


def capturar_pokemon():
    
    print("\n--- Capturar Pokémon 🐉 ---")
    nombre = input("Nombre: ").strip()
    tipo = input("Tipo: ").strip()

    if not nombre or not tipo:
        print("El nombre y el tipo no pueden estar vacíos.")
        return

    try:
        ataque = int(input("Ataque inicial: "))
        defensa = int(input("Defensa inicial: "))
        salud = int(input("Salud inicial: "))

        if ataque < 0 or defensa < 0 or salud <= 0:
            print("Ataque y defensa deben ser >= 0; salud debe ser > 0.")
            return
    except ValueError:
        print("Error: debes introducir números enteros.")
        return

    nuevo_pokemon = Pokemon(nombre, tipo, ataque, defensa, salud)
    pokemons.append(nuevo_pokemon)
    print(f"¡{nombre} se ha unido al equipo!")


def seleccionar_pokemon():
    
    if not pokemons:
        print("\nNo hay Pokémon disponibles.")
        return None

    print("\n--- Pokémon disponibles ---")
    for i, pokemon in enumerate(pokemons, start=1):
        print(
            f"{i}. {pokemon.nombre} "
            f"(Nivel {pokemon.nivel}, Salud {pokemon.salud})"
        )

    try:
        opcion = int(input("Selecciona el número del Pokémon: "))
        if 1 <= opcion <= len(pokemons):
            return pokemons[opcion - 1]
        print("Número fuera de rango.")
    except ValueError:
        print("Debes introducir un número entero.")
    return None


def entrenar_pokemon():
    pokemon = seleccionar_pokemon()
    if pokemon is None:
        return

    print("\n--- Entrenamiento 💪 ---")
    print("1. Entrenamiento predeterminado")
    print("2. Personalizar las mejoras")
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        pokemon.entrenar()
    elif opcion == "2":
        try:
            cantidad = int(input("¿Cuántas estadísticas quieres mejorar? (1-3): "))
            if cantidad not in (1, 2, 3):
                print("Debes elegir entre 1 y 3 estadísticas.")
                return

            nombres = ["ataque", "defensa", "salud"]
            mejoras = []
            for i in range(cantidad):
                valor = int(input(f"Mejora para {nombres[i]}: "))
                if valor < 0:
                    print("La mejora no puede ser negativa.")
                    return
                mejoras.append(valor)

            pokemon.entrenar(*mejoras)
        except ValueError:
            print("Introduce números enteros válidos.")
    else:
        print("Opción no válida.")


def mostrar_todos():
    if not pokemons:
        print("\nNo hay Pokémon capturados.")
        return

    print("\n--- Información de los Pokémon 📋 ---")
    for pokemon in pokemons:
        pokemon.mostrar_info()


def liberar_pokemon():
    pokemon = seleccionar_pokemon()
    if pokemon is None:
        return

    nombre = pokemon.nombre
    pokemons.remove(pokemon)
    print(f"{nombre} ha sido retirado del equipo.")
    del pokemon


def combatir():
    if len(pokemons) < 2:
        print("\nNecesitas al menos dos Pokémon para combatir.")
        return

    print("\nSelecciona al Pokémon atacante:")
    atacante = seleccionar_pokemon()
    if atacante is None:
        return

    print("\nSelecciona al Pokémon objetivo:")
    objetivo = seleccionar_pokemon()
    if objetivo is None:
        return

    if atacante is objetivo:
        print("Un Pokémon no puede atacarse a sí mismo.")
        return

    atacante.atacar(objetivo)


def menu():
    while True:
        print("\n" + "=" * 40)
        print("       POKÉMON SIMULATOR 🎮")
        print("=" * 40)
        print("1. Capturar Pokémon 🐉")
        print("2. Entrenar Pokémon 💪")
        print("3. Ver todos los Pokémon 📋")
        print("4. Calcular total de Pokémon 🧮")
        print("5. Liberar Pokémon 🕊️")
        print("6. Combatir ⚔️")
        print("7. Salir 🚪")
        print("=" * 40)

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            capturar_pokemon()
        elif opcion == "2":
            entrenar_pokemon()
        elif opcion == "3":
            mostrar_todos()
        elif opcion == "4":
            Pokemon.total_pokemons()
        elif opcion == "5":
            liberar_pokemon()
        elif opcion == "6":
            combatir()
        elif opcion == "7":
            print("\n¡Gracias por jugar Pokémon Simulator! 👋")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
