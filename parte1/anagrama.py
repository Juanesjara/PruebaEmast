def anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
   
    palabra1_arreglo = list(palabra1)
    palabra2_arreglo = list(palabra2)
  
    palabra1_arreglo.sort()
    palabra2_arreglo.sort()
   
    palabra1_ordenada = "".join(palabra1_arreglo)
    palabra2_ordenada = "".join(palabra2_arreglo)
    # Y finalmente comprobar si son iguales
    return palabra1_ordenada == palabra2_ordenada


def __main__():
    
    palabra1 = input("Escriba la primera palabra a comparar")
    palabra2 = input("Escriba la segunda palabra a comparar")
    es_anagrama = anagrama(palabra1, palabra2)
    if es_anagrama: 
        print(f"{palabra1} es anagrama de {palabra2}")
    else:
        print(f"{palabra1} NO es anagrama de {palabra2}")
        
