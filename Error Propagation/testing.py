from errorpropy import errorpropy as

formula,value = ep.error_prop("x+y",["x","y"],[2,5],[6,3])
print(formula)
print(value)