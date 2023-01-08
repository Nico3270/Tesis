# def fibonacciGenerator(n):
#     lista = []
#     for i in range(0,n):
#         if i == 0:
#             lista.append(0)
#         elif i == 1:
#             lista.append(1)
#         else:
#             var1= lista[(len(lista)-1)]
#             var2= lista[(len(lista)-2)]
#             lista.append(var1+var2)
#     return lista

# print(fibonacciGenerator(15))

import HCM_2carriles as mn

datos = mn.hcm2_final_asc(2,9.5,4.1,1.11,"Ascenso",5.4,49.71,520,480,14,15,0.91,15,2,"No",0,25)
print(datos)