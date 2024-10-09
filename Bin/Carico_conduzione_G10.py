# Carico conduzione tra astine G10 e piastra 55K e 4K
import numpy as np

def main() :
    
    # Caratteristiche geometriche cilindretti G10 
    diam = 8e-3
    l = 30e-3 # lunghezza cilindretti
    A = np.pi * (diam/2)**2
    n = 5 # numero di cilindretti
    
    #Conductivity integral
    conductivity_integral = 17 # 77K to OK da dispense  !!SOVRASTIMA (nostro caso: 55 to 4K)


    # Calcolo di Q
    Q = A/l * conductivity_integral * n        

    # Output del risultato
    print(f"Q = {Q:.4e} W")

if __name__ == "__main__":
  main ()

