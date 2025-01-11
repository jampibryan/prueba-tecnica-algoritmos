
class Pecera:
    def calcular_tamanios_validos(self, largo_min: int, largo_max: int, largo_peces: list) -> int:
        """
        Calcula la cantidad de tamaños válidos para el pez "Jhon".
        Un tamaño válido es aquel que no pone a Jhon en peligro 
            ni permite que él coma a otros peces.
        """
        contador_tamanios_validos = 0

        # Itera sobre todos los posibles tamaños para Jhon en el rango [largo_min, largo_max]
        for tamanio_jhon in range(largo_min, largo_max + 1):
            tamanio_valido = True

            # Verifica si hay conflictos de canibalismo contra otros peces
            for tamanio_pez in largo_peces:
                if (2 * tamanio_jhon <= tamanio_pez <= 10 * tamanio_jhon or 
                    2 * tamanio_pez <= tamanio_jhon <= 10 * tamanio_pez):
                    tamanio_valido = False
                    break

            if tamanio_valido:
                contador_tamanios_validos += 1

        return contador_tamanios_validos


def procesar_archivo():
    """
    Lee los datos del archivo de entrada, procesa cada caso,
        y escribe los resultados en el archivo de salida.
    """
    # Archivos de entrada y salida
    input_file = "./input/problema_01_input.txt"
    output_file = "./output/problema_01_output.txt"

    # Crea una instancia de la clase Pecera
    pecera = Pecera()

    try:
        # Abrir archivos de entrada y salida
        with open(input_file, 'r') as entrada, open(output_file, 'w') as salida:
            for linea in entrada:
                # Divide la línea en partes separadas por ";"
                partes = linea.strip().split(';')

                # Valida que la línea tenga exactamente 3 partes
                if len(partes) != 3:
                    raise ValueError(f"Formato inválido en la línea: {linea.strip()}")

                # Extrae largo_min, largo_max y la lista de peces
                largo_min = int(partes[0])
                largo_max = int(partes[1])
                largo_peces = list(map(int, partes[2].split(',')))

                # Calcula los tamaños válidos para "Jhon"
                resultado = pecera.calcular_tamanios_validos(largo_min, largo_max, largo_peces)

                # Escribe el resultado en el archivo de salida
                salida.write(f"{resultado}\n")

    except FileNotFoundError:
        print("Error: No se encontró el archivo de entrada o salida.")
    except ValueError as e:
        print(f"Error en el formato de entrada: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    procesar_archivo()
