import math
from robocorp.tasks import task
import instructions

#======================================================================================
#CALCULATE THE FUNCTION F(X)
#======================================================================================

def calculate_function(function_str, x) -> float:
    try:
        result = eval(function_str, {'x': x, 'math': math, 'sin': math.sin, 'cos': math.cos, 
                                     'tan': math.tan, 'log': math.log, 'log10': math.log10, 
                                     'sqrt': math.sqrt, 'abs': abs})
        return result
    except Exception as error:
        return (f"Erro ao calcular a função: {error}")

#======================================================================================
#RUN THE ITERACTION METHOD
#======================================================================================

def iteraction(function_str, a, b, e) -> str:
    expected_error = eval(e)
    xi = 0
    total_iteraction = 0

    while True:
        fa = calculate_function(function_str, a)
        fb = calculate_function(function_str, b)

        if fa == 0:
            xi = a
            break
        if fb == 0:
            xi = b
            break

        if(fa*fb) > 0:
            return (f'Não há uma raiz entre {a} e {b}')

        xi = (a+b)/2
        fxi = calculate_function(function_str, xi)

        if (fa * fxi) < 0:
            b = xi
        else:
            a = xi

        total_iteraction += 1

        if expected_error > abs(b-a):
            break
    
    if total_iteraction == 1:  
        return (f'A raíz é {xi}. Foi necessária {total_iteraction} iteração.')
    
    return (f'A raíz é {xi}. Foram necessárias {total_iteraction} iterações.')


#======================================================================================
#DISPLAY THE INPUTS AND OUTPUTS FOR THE USER
#======================================================================================

@task
def inputs() -> None:
    instructions.show_instructions()
    function_str = input("Entre com a função f(x): ")
    a = float(input("Entre com o valor de a: "))
    b = float(input("Entre com o valor de b: "))
    e = input("Entre com o valor de euler(erro): ")

    final_result = iteraction(function_str, a, b, e)

    print(final_result)
