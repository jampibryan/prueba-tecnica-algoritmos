

class MatrixDiagonalDifference:
    def diagonal_difference(self, arr: list) -> int:
        # Suma los elementos de la diagonal principal (de izquierda a derecha)
        diagonal_principal = 0
        for i in range(len(arr)):
            diagonal_principal += arr[i][i]

        # Suma los elementos de la diagonal secundaria (de derecha a izquierda)
        diagonal_secundaria = 0
        for i in range(len(arr)):
            diagonal_secundaria += arr[i][len(arr)-1-i]

        # Retorna la diferencia absoluta entre ambas sumas
        return abs(diagonal_principal - diagonal_secundaria)

def convertir_a_matriz(cadena_matriz: str) -> list:
    # Divide la cadena en filas separadas por ';'
    filas = cadena_matriz.strip().split(';')
    
    # Convierte cada fila en una lista de enteros separados por ','
    matriz = []
    for fila in filas:
        matriz.append(list(map(int, fila.split(','))))
    
    return matriz

def main():
    input_file = "./input/problema_02_input.txt"
    output_file = "./output/problema_02_output.txt"

    # Crea instancia del calculador de diferencias
    calculadora = MatrixDiagonalDifference()

    try:
        # Abre los archivos de entrada y salida
        with open(input_file, 'r') as entrada, open(output_file, 'w') as salida:
            # Lee cada línea del archivo de entrada
            for linea in entrada:
                try:
                    # Convierte la línea en una matriz
                    matriz = convertir_a_matriz(linea)
                    
                    # Calcula la diferencia de diagonales
                    resultado = calculadora.diagonal_difference(matriz)
                    
                    # Escribe el resultado en el archivo de salida
                    salida.write(f"{resultado}\n")
                except Exception:
                    # Salida de -1 en caso de error con una línea específica
                    salida.write("-1\n")
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()