equipo_local = "Venezuela"
equipo_visitante = "Brasil"
goles_local = 2
goles_visitante = 1

print(equipo_local, goles_local, "-", goles_visitante, equipo_visitante)

if goles_local > goles_visitante:
    print("Gana", equipo_local)
elif goles_local < goles_visitante:
    print("Gana", equipo_visitante)
else:
    print("Empate")