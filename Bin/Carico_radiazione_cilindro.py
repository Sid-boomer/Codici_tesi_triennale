# CALCOLA CARICO TERMICO DI RADIAIZONE CILINDRO INTERNO CON PARETI ESTERNE (ESCLUDO QUELLA DI BASE)
#PLOTTA CARICO RADIAZIONE VS EMISSIVITà PARETI CRIOSTATO
import numpy as np
import matplotlib.pyplot as plt


# Definizione costante di Stefan-Boltzmann
sigma = 5.670e-8  # W/m^2K^4


def main() :
    
    # Caratteristiche geometriche
    h_crio = 30.6e-2 # altezza parete criostato APPROX!!
    width_crio = 49.5e-2 # APPROX!!
    length_crio = 54.5e-2 # APPROX!!
    diam_cilindro = 10.5e-2 
    h_cilindro = 11.6e-2

    A1 = np.pi*diam_cilindro*h_cilindro + 2*np.pi*(diam_cilindro/2)**2 # superificie cilindro 
    A2 = 2*((width_crio*h_crio)+(length_crio*h_crio)) + (width_crio*length_crio) # superficie pareti crio
    T1 = 4 # temperatura cilindro
    T2 = 55 # temperatura pareti
    epsilon1 = 0.1 # emissività pareti !!APPROX
    epsilon2 = 0.1 # emissività cilindro !!APPROX

    # Calcolo di Q
    Q = (sigma * A1 * (T2**4 - T1**4)) / (1/epsilon1 + (A1/A2) * (1/epsilon2 - 1))           

    # Output del risultato
    print(f"Superificie interna criostato = {A1:.4e} m^2" )
    print(f"Superficie esterna criostato = {A2:.4e} m^2" )
    print(f"Q = {Q:.4e} W")

    #GRAFICO CARICO(EMISSIVITà)

    # Funzione carico(emissività pareti)
    def y(epsilon1):
        return ((sigma * A1 * (T2**4 - T1**4)) / (1/epsilon1 + (A1/A2) * (1/epsilon2 - 1)))
    
    # Intervallo di temperatura (dal NIST)
    epsilon_range = np.linspace(0.00000001, 1, 1000)

    # Valori di Q calcolati
    Q_values = y(epsilon_range)

    # Plot della funzione
    plt.plot(epsilon_range, Q_values, label='Q=f(ε)', color='blue')
    plt.title('Carico radiativo vs emissività pareti criostato')
    plt.xlabel('Emissività')
    plt.ylabel('Q (Watt)')
    plt.grid(True)
    plt.legend()
    #plt.show()
    plt.savefig("Carico_radiazione_cilindro.png")


if __name__ == "__main__":
  main ()
