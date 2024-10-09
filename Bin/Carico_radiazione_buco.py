# CALCOLA CARICO TERMICO DI RADIAZIONE SUPPONENDO BUCO 1CM 300K TO AREA 1CM 4K
import numpy as np


# Definizione costante di Stefan-Boltzmann
sigma = 5.670e-8  # W/m^2K^4


def main() :
    
    # Caratteristiche geometriche
    A1 = 1e-2
    A2 = 1e-1
    T1 = 300 # temperatura ext
    T2 = 4 # temperatura int
    epsilon1 = 0.1 # emissività
    epsilon2 = 0.1 # emissività

    # Calcolo di Q
    Q = (sigma * A1 * (T2**4 - T1**4)) / (1/epsilon1 + (A1/A2) * (1/epsilon2 - 1))           

    # Output del risultato
    print(f"Q = {Q:.4e} W")

if __name__ == "__main__":
  main ()
