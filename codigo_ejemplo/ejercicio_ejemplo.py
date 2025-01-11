def calcular_lote(arr_cajas):
    # Se suman las cantidades de cada caja
    return sum(arr_cajas)

def main():
    # Ruta de archivo de entrada
    input_file = "../input/input.txt"

    # Ruta de archivo de salida
    output_file = "../output/output.txt"

    # Se valida el archivo de entrada
    try:
        with open(input_file, 'r') as br:
            # Se crea el archivo de salida
            with open(output_file, 'w') as fw:
                # Se iteran todas las líneas del archivo de entrada
                for line in br:
                    # Se convierten las cantidades de String a Int
                    numbers = list(map(int, line.strip().split(',')))
                    # Llamar a la función de cálculo
                    suma = calcular_lote(numbers)
                    # Se escribe la respuesta en el archivo de salida con un salto de línea para separar la respuesta de cada línea
                    fw.write(f"{suma}\n")
    except FileNotFoundError as e:
        print(f"Archivo no encontrado: {e}")
    except IOError as e:
        print(f"Error de E/S: {e}")

if __name__ == "__main__":
    main()