

import os
import time

for h in range(24):
    for m in range(60):
        for s in range(60):
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("      CRONÓMETRO      ")
            print(f"       {h:02d}:{m:02d}:{s:02d}")
            
            time.sleep(1)