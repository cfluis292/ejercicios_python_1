import os
import time

for h in range(24):
    for m in range(60):
        for s in range(60):
            # Limpiamos la pantalla (funciona en Windows y Mac/Linux)
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("      CRONÓMETRO      ")
            print("{h:02d}:{m:02d}:{s:02d}")
            
            time.sleep(1)