import fibonacci 
import palindromo
import fizzbuzz
import anagrama

def __main__():
    menu = input("¿Que funcion deseas correr? \n 1. Fibonacci \n 2. Palindromo \n 3. FizzBuzz \n 4. Anagrama \n")
    match int(menu):
        case 1:
            numero = input("¿Hasta que numero quieres la sucesion de fibonacci?\n")
            print("Esta es la secuencia hasta el numero ", numero)
            for x in range(int(numero)):
                print(fibonacci.fib(x))
        case 2:
            palabra = input('Escriba una palabra: \n').lower()  
            res = palindromo.esPalindromo(palabra)
            if res:
                print('La palabra ',palabra,' es palindromo')
            else:
                print('La palabra ',palabra,' no es palindromo')
        case 3:
            numero = input('Escriba hasta que numero desea hacer la secuencia de FizzBuzz \n')
            fizzbuzz.fizzBuzz(numero)
        case 4:
            palabra1 = input("Escriba la primera palabra a comparar \n")
            palabra2 = input("Escriba la segunda palabra a comparar \n")
            es_anagrama = anagrama.anagrama(palabra1, palabra2)
            if es_anagrama: 
                print(f"{palabra1} es anagrama de {palabra2}")
            else:
                print(f"{palabra1} NO es anagrama de {palabra2}")
        case default:
            print("Esa opcion no esta disponible vuelve a elegir otra \n")
            __main__()
                
            
            
            
            
    
__main__()