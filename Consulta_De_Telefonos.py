from Consultas import *

class ImplentacionDeAlgoritmosDeBusqueda:

    # Método para el manejo de archivos de texto
    def leerArchivo(self, archivo):
        datos = []
        file = open(archivo, 'r')
        for f in file.readlines():
            linea = f.replace('\n', '')
            elementos = linea.split(',')
            try:
                datos.append([str(elementos[0]), int(elementos[1])])

            except ValueError:
                datos.append(['', 0.0])

        file.close()
        del (file)
        return datos

    # Método encargado de generar los resultados guardandolos en un arreglo y retornandolo
    def generarResultados(self, lista, dato):
        rectangulo = BusquedaSecuencial()
        resultados = []
        for f in range(0, len(lista)):
            area = rectangulo.busqueda(lista, dato)

            resultados.append([area])
        return resultados

    # Método encargado de guardar los resultados guardandolos en un archivo de texto
    def guardarResultados(self, archivo, datos, resultados):
        file = open(archivo, 'w')
        for f in range(0, len(datos)):
            linea = str(resultados[f][0]) + ',' + '\n'
            file.write(linea)

        file.close()
        del (file)


def main():
    file = ImplentacionDeAlgoritmosDeBusqueda()
    datoAencontrar = 7676798567
    arreglo = file.leerArchivo('Datos.txt')
    resultados = file.generarResultados(arreglo, datoAencontrar)
    file.guardarResultados('Resultados_De_La_Busqueda.txt', arreglo, resultados)


if __name__ == '__main__':
    main()