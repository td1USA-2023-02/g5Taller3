import pulp

problema = pulp.LpProblem("Dieta", pulp.LpMinimize)

# las Variables de decisión son:
x1 = pulp.LpVariable("Manzanas", 0, 6, pulp.LpInteger)
x2 = pulp.LpVariable("Plátanos", 0, 4, pulp.LpInteger)
x3 = pulp.LpVariable("Yogur", 0, 2, pulp.LpInteger)

# la Función objetivo es:
problema += 0.5 * x1 + 0.4 * x2 + 1.2 * x3

# Restricciones del modelo:
problema += 50 * x1 + 89 * x2 + 150 * x3 >= 2000
problema += 1.2 * x1 + 1.1 * x2 + 3.4 * x3 >= 80

#___________________________________________
problema.solve()

print("Estado:", pulp.LpStatus[problema.status])
print("Costo total diario: $", pulp.value(problema.objective))
print("Cantidad de manzanas a consumir diariamente:", int(pulp.value(x1)))
print("Cantidad de plátanos a consumir diariamente:", int(pulp.value(x2)))
print("Cantidad de yogur a consumir diariamente:", int(pulp.value(x3)))



print("No se encontró una solución óptima. Toca revisar las restricciones del problema.")
