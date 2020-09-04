from pruebaPrimos.models import Primos
from pruebaPrimos.serializers import PrimosSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


def calcular_numeros_primos(n):
    """
    Metodo que permite retornar los primeros n numeros primos
    :param n: n numeros primos como parametro
    :return: Lista con los primeros n numeros primos
    """
    list_numeros_primos = []
    list_numeros_no_primos = []
    num = int(n)
    for j in range(1, 200):
        if j <= 1:
            list_numeros_no_primos.append(j)
        elif j == 2:
            list_numeros_primos.append(j)
        else:
            cache = []
            for i in range(1, j + 1):
                mod = j % i
                if mod == 0:
                    cache.append(mod)
            if len(cache) == 2:
                list_numeros_primos.append(j)
        if (len(list_numeros_primos) == num):
            return list_numeros_primos

def calcular_numeros_primos_gemelos(n):
    """
    Metodo que permite retornar los primeros n numeros primos gemelos
    :param n: n numeros primos como parametro
    :return: Lista con los n primeros numeros primos gemelos
    """
    list_numeros_primos = []
    list_numeros_no_primos = []
    list_numeros_primos_pares = []
    num = int(n)
    for j in range(1, 200):
        if j <= 1:
            list_numeros_no_primos.append(j)
        elif j == 2:
            list_numeros_primos.append(j)
        else:
            cache = []
            for i in range(1, j+1):
                mod = j % i
                if mod == 0:
                    cache.append(mod)
            if len(cache) == 2:
                list_numeros_primos.append(j)
                if len(list_numeros_primos) > 1:
                    ultimo_valor = list_numeros_primos[len(list_numeros_primos) - 1]
                    penultimo_valor = list_numeros_primos[len(list_numeros_primos) - 2]
                    if ultimo_valor - penultimo_valor == 2:
                        list_numeros_primos_pares.append((penultimo_valor, ultimo_valor))
                        if len(list_numeros_primos_pares) == num:
                            return list_numeros_primos_pares

@api_view(['GET', 'PUT', 'DELETE'])
def numeros_primos(request, pk):
    """
    Metodo que permite devolver por api los primeros n numeros primos al usuario
    :param request: metodo GET, PUT o DELETE-
    :param pk: Parametro que indica los n primeros numeros primos que el usuario desee visualizar
    :return: Respuesta Json, que indica la cantidad de numeros primos a visualizar y una lista con los n primeros numeros
    """
    if request.method == 'GET':
        primps = Primos(numero=pk, numeros_primos=calcular_numeros_primos(pk))
        primosSerializer = PrimosSerializer(primps)
        return Response(primosSerializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def numeros_primos_gemelos(request, pk):
    """
        Metodo que permite devolver por api los primeros n numeros primos gemelos al usuario
        :param request: metodo GET, PUT o DELETE-
        :param pk: Parametro que indica la cantidad de n primeros numeros primos que el usuario desee visualizar
        :return: Respuesta Json, que indica la cantidad de numeros primos a visualizar y una lista con los n primeros numeros
        """
    if request.method == 'GET':
        primps = Primos(numero=pk, numeros_primos=calcular_numeros_primos_gemelos(pk))
        primosSerializer = PrimosSerializer(primps)
        return Response(primosSerializer.data)