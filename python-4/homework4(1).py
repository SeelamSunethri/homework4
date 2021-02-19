def temp_converter(Tf):
    celscius= (5/9)*(Tf-32)
    return celscius
Tf = float(input('temperature in Fahrenheit')) 
print(temp_converter(Tf))