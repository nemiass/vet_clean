# Abre el archivo y cuenta líneas y caracteres
line_number = 0
char_position = 0
problematic_line = None

with open('C:/Users/user/Desktop/dev/other-projets/vet/vet_back/app/.env', 'r', encoding='utf-8', errors='replace') as file:
    for line in file:
        line_number += 1
        char_position += len(line)  # Contar caracteres en la línea
        if char_position >= 85:  # Si la posición excede 85, es la línea problemática
            problematic_line = line
            break

if problematic_line:
    print(f"Línea: {line_number}, Contenido: {problematic_line.strip()}")
else:
    print("El archivo tiene menos de 85 caracteres.")
