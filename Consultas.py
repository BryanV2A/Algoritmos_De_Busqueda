# Clase BusquedaSecuencial
class BusquedaSecuencial:

    # Método para realizar una busqueda de manera secuencial en un arreglo
    def busqueda(self, lista, clave):
        encontrado = False
        for f in range(0, len(lista)):
            for c in range(0, len(lista[f])):
                if lista[f][c] == clave:
                    encontrado = True
                    break
        return encontrado

def main():
    A = [['aaron', 7676798563], ['abel', 7676798564], ['abelardo', 7676798565], ['abigail', 7676798566], ['abraham', 7676798567]]
    b = BusquedaSecuencial()
    print(b.busqueda(A, 7676798563))

if __name__ == "__main__":
    main()