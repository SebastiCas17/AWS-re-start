# hemoglobin_analysis.py
# Script para analizar la secuencia de la hemoglobina beta humana
# Este programa:
# 1. Lee una secuencia de aminoacidos desde un archivo de texto
# 2. Muestra informacion basica de la proteina
# 3. Calcula la composicion de aminoacidos
# 4. Calcula el peso molecular aproximado
# 5. Calcula el porcentaje de aminoacidos hidrofobicos
# 6. Guarda los resultados en un archivo JSON

import json

# ---------------------------------------------------
# Ejercicio 2: Cargar la secuencia limpia desde archivo
# ---------------------------------------------------

with open("hemoglobin_clean.txt", "r") as file:
    sequence = file.read().strip()

# ---------------------------------------------------
# Ejercicio 4: Mostrar informacion de la secuencia
# ---------------------------------------------------

protein_name = "Hemoglobin subunit beta [Homo sapiens]"

print("ANALISIS DE HEMOGLOBINA BETA HUMANA")
print("------------------------------------")
print("Proteina:", protein_name)
print("Longitud de la secuencia:", len(sequence))
print("Primeros 30 aminoacidos:", sequence[:30])
print()

# ---------------------------------------------------
# Ejercicio 5: Calcular composicion de aminoacidos
# ---------------------------------------------------

# Lista de los 20 aminoacidos estandar
amino_acids = list("ACDEFGHIKLMNPQRSTVWY")

amino_count = {}

for aa in amino_acids:
    amino_count[aa] = sequence.count(aa)

print("COMPOSICION DE AMINOACIDOS")
print("---------------------------")

for aa, count in amino_count.items():
    print(aa, ":", count)

print()

# ---------------------------------------------------
# Ejercicio 6: Diccionario de pesos moleculares
# ---------------------------------------------------

mw_table = {
    "A": 89.09, "C": 121.16, "D": 133.10, "E": 147.13,
    "F": 165.19, "G": 75.03, "H": 155.16, "I": 131.17,
    "K": 146.19, "L": 131.17, "M": 149.21, "N": 132.12,
    "P": 115.13, "Q": 146.15, "R": 174.20, "S": 105.09,
    "T": 119.12, "V": 117.15, "W": 204.23, "Y": 181.19
}

# ---------------------------------------------------
# Ejercicio 7: Funcion para calcular peso molecular
# ---------------------------------------------------

def calculate_molecular_weight(seq):
    """
    Calcula el peso molecular aproximado de una proteina.
    Se resta el peso de las moleculas de agua formadas
    durante los enlaces peptidicos.
    """

    water = 18.02
    total_weight = 0

    for aa in seq:
        total_weight += mw_table.get(aa, 0)

    molecular_weight = total_weight - (len(seq) - 1) * water

    return round(molecular_weight, 2)


# Calcular peso molecular
mol_weight = calculate_molecular_weight(sequence)

print("PESO MOLECULAR")
print("----------------")
print("Peso molecular aproximado:", mol_weight, "Da")
print()

# ---------------------------------------------------
# Ejercicio 9: Porcentaje de aminoacidos hidrofobicos
# ---------------------------------------------------

hydrophobic = ["A", "V", "I", "L", "M", "F", "W", "Y"]

hydrophobic_count = 0

for aa in hydrophobic:
    hydrophobic_count += sequence.count(aa)

hydrophobic_percent = (hydrophobic_count / len(sequence)) * 100

print("AMINOACIDOS HIDROFOBICOS")
print("-------------------------")
print("Cantidad:", hydrophobic_count)
print("Porcentaje:", round(hydrophobic_percent, 2), "%")
print()

# ---------------------------------------------------
# Ejercicio 8: Guardar resultados en JSON
# ---------------------------------------------------

results = {
    "protein_name": protein_name,
    "sequence_length": len(sequence),
    "amino_acid_count": amino_count,
    "molecular_weight_Da": mol_weight,
    "hydrophobic_count": hydrophobic_count,
    "hydrophobic_percent": round(hydrophobic_percent, 2)
}

with open("hemoglobin_results.json", "w") as file:
    json.dump(results, file, indent=4)

print("Resultados guardados en hemoglobin_results.json")