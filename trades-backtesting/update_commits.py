import os
import subprocess
from tqdm import tqdm  # Para barra de progreso

REPO_PATH = r"C:\Users\hacki\Downloads\Backtesting\backtestingNQ\trades-backtesting"

def update_commit_messages():
    # Cambiar al directorio del repositorio
    os.chdir(REPO_PATH)
    
    # Procesar cada trade del 1 al 100
    for i in tqdm(range(1, 101), desc="Actualizando commits"):
        trade_folder = f"Trade #{i}"
        
        # Verificar si la carpeta existe
        if os.path.exists(trade_folder):
            # Entrar a la carpeta del trade
            os.chdir(trade_folder)
            
            # Crear archivo temporal para forzar commit
            open(f".update_{i}", 'a').close()
            
            # Modificar el commit
            subprocess.run([
                "git", "add", f".update_{i}",
                "git", "commit", "--amend", "-m", f"Backtesting NQ 2025 Trade #{i}", "--no-edit"
            ])
            
            # Volver al directorio principal
            os.chdir("..")
    
    # Subir todos los cambios
    subprocess.run(["git", "push", "origin", "main", "--force-with-lease"])

if __name__ == "__main__":
    update_commit_messages()