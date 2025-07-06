import os
import shutil

# Configuración inicial
base_dir = os.getcwd()  # Directorio actual (ajusta si es necesario)
template_folder = "Trade_001"
readme_template = os.path.join(template_folder, "README.md")

# Verificar si la carpeta base existe
if not os.path.exists(template_folder):
    print(f"Error: No existe la carpeta base '{template_folder}'")
    exit(1)

# Leer el contenido base del README.md
try:
    with open(readme_template, 'r', encoding='utf-8') as file:
        template_content = file.read()
except FileNotFoundError:
    print(f"Error: No se encontró {readme_template}")
    exit(1)

# Crear desde Trade_002 hasta Trade_100
for i in range(2, 101):
    # Formatear el número con 3 dígitos (002, 003, ..., 100)
    folder_num = f"{i:03d}"
    folder_name = f"Trade_{folder_num}"
    folder_path = os.path.join(base_dir, folder_name)
    
    # Crear carpeta si no existe
    os.makedirs(folder_path, exist_ok=True)
    
    # Crear README.md personalizado
    new_readme_path = os.path.join(folder_path, "README.md")
    
    # Reemplazar referencias al número de trade (ej: "001" → "002")
    new_content = template_content.replace("001", folder_num)
    
    with open(new_readme_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
    
    print(f"Creado: {folder_name}/README.md")

print("¡Proceso completado! Se crearon 99 carpetas.")