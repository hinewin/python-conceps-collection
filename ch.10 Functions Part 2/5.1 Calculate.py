# Write a function called calculate that accepts keyword arguments
# make_float, boolean that returns a float if True, or integer if False
#operation, 'add', 'substract','multiply','divide'
#first = number, second = number, message = string that can be added

#Should return result of running the specified operations
# with first and second keyword arguments
#if make_float = false, first and second = integer. Else = float
#if message is specified, return message keyword argument +
#result of operation . Else return string "the Result is"
#joined with result of operation

def calculate(**kwargs):
    operation_lookup = {
'add': kwargs.get('first,0') + kwargs.get('second',0),
'substract': kwargs.get('first',0) - kwargs.get('second',0),
'divide': kwargs.get('first',0) / kwargs.get('second',0),
'divide': kwargs.get('first',0) * kwargs.get('second',0),}
    is_float = kwargs.get('make_float',False)
    operation_value = operation_lookup[kwargs.get('operation','')]
    
    if is_float:
        final = (f"{kwargs.get('message','The result is')} {float(operation_value)}")
        