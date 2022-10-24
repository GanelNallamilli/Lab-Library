import sympy as sy
class errorpropy:
    sy.init_printing(wrap_line=False, no_global=True)


    def error_prop(expression,variables,vari_values,error_values):
        expression = sy.parse_expr(expression)
        symbol_array = [sy.symbols(x) for x in variables]
        complete_expression = sy.sqrt((sum((sy.diff(expression,x)*sy.symbols('sigma_'+variables[i]))**2 for i,x in enumerate(symbol_array))).simplify())
        symbol_tuple = tuple(x for x in symbol_array) + tuple(sy.symbols('sigma_'+variables[i]) for i in range(len(symbol_array))) 
        value_tuple = tuple(x for x in vari_values) + tuple(x for x in error_values)
        lambda_expression = sy.lambdify(symbol_tuple,complete_expression)
        value = lambda_expression(*value_tuple)
        return complete_expression,value



