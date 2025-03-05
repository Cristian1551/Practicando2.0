''' 
   Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura seré el numero de factura y el valor el costo de la factura. 

   El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existen o terminar. 

   Si desea pagar una factura se preguntara por el numero de factura y se eliminara del diccionario. Despues de cada operacion el rpograma debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

''' 
facturas = {}
cobrado = 0
pendiente = 0
mas = ''


while more != 'T':
    if more == 'A':
        clave = input('Introduce el número de la factura: ')
        coste = float(input('Introduce el costo de la factura: '))
        facturas[clave] = coste
        pendiente += coste


    if more == 'P':
        clave = input('Introduce el número de la factura a pagar: ')
        coste = facturas.pop(clave, 0)
        cobrado += coste
        pendiente -= coste


    print('Cobrado:', cobrado)
    print('Pendiente de cobro: ', pendiente)

    more = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')