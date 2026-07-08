# TODO 1: crea un diccionario product con name="lapiz", price=2.5 y stock=30.
# Luego revisa el valor de product para ver el diccionario creado.
product =

# TODO 2: crea un diccionario vacio llamado sales_by_day.
# Luego revisa el valor de sales_by_day para ver que empieza vacio.
sales_by_day =

# TODO 3: crea un diccionario supplier usando dict() con una lista de pares.
# Usa brand="Faber" y country="Peru".
# Luego revisa el valor de supplier para ver el diccionario creado desde pares.
supplier =

# TODO 4: obtiene el nombre del producto usando la clave "name".
# Luego revisa el valor de product_name para ver el acceso por clave.
product_name =

# TODO 5: obtiene la categoria usando get() con el valor por defecto "sin categoria".
# Luego revisa el valor de product_category para ver el resultado de get().
product_category =

# TODO 6: agrega la clave "category" con el valor "utiles" a product.
# Luego revisa el valor de product para ver la nueva clave.


# TODO 7: actualiza product con price=3.0 y stock=25 usando update().
# Luego revisa el valor de product para ver los cambios.


# TODO 8: elimina "category" usando pop() y guarda el valor en removed_category.
# Luego revisa el valor de removed_category y product.
removed_category =

# TODO 9: crea discontinued_product con old_code="A1" y old_price=1.0.
# Luego revisa el valor de discontinued_product para ver el diccionario inicial.
discontinued_product =

# TODO 10: elimina la clave "old_price" usando del.
# Luego revisa el valor de discontinued_product para ver el cambio.


# TODO 11: elimina el ultimo par de discontinued_product usando popitem().
# Luego revisa el valor de removed_pair y discontinued_product.
removed_pair =

# TODO 12: crea draft_product con note="borrar" y ready=False.
# Luego revisa el valor de draft_product para ver el diccionario inicial.
draft_product =

# TODO 13: vacia draft_product usando clear().
# Luego revisa el valor de draft_product para ver que quedo vacio.


# TODO 14: comprueba si "stock" existe en product.
# Luego revisa el valor de has_stock para ver el resultado de usar in.
has_stock =

# TODO 15: obtiene las claves de product como una lista.
# Luego revisa el valor de product_keys para ver el resultado de keys().
product_keys =

# TODO 16: obtiene los valores de product como una lista.
# Luego revisa el valor de product_values para ver el resultado de values().
product_values =

# TODO 17: obtiene los pares clave-valor de product como una lista.
# Luego revisa el valor de product_items para ver el resultado de items().
product_items =

# TODO 18: crea una lista vacia llamada formatted_fields.
# Luego revisa el valor de formatted_fields para ver que empieza vacia.
formatted_fields =

# TODO 19: recorre product.items() desempaquetando key y value.
# Dentro del for, crea field_summary con textos como "name: lapiz".
# Agrega field_summary a formatted_fields.
# Luego revisa el valor de field_summary en cada vuelta y formatted_fields al final.


# TODO 20: crea una copia de product usando copy().
# Luego revisa el valor de product_copy para ver la copia.
product_copy =

# TODO 21: agrega "status" con el valor "activo" a product_copy.
# Luego revisa el valor de product_copy y product para ver que son diccionarios distintos.


# TODO 22: crea un diccionario prices con lapiz=2.5, cuaderno=8.0 y regla=3.0.
# Luego revisa el valor de prices para ver los precios base.
prices =

# TODO 23: crea prices_with_tax usando dict comprehension y round(price * 1.18, 2).
# Luego revisa el valor de prices_with_tax para ver los precios con impuesto.
prices_with_tax =

# TODO 24: crea affordable_prices con los productos de prices que cuestan menos de 5.
# Luego revisa el valor de affordable_prices para ver el diccionario filtrado.
affordable_prices =

# TODO 25: crea un diccionario anidado store con inventory y branches.
# inventory debe tener lapiz con stock=30 y price=2.5, y cuaderno con stock=12 y price=8.0.
# branches debe tener centro="Lima" y norte="Trujillo".
# Luego revisa el valor de store para ver el diccionario anidado.
store =

# TODO 26: obtiene el stock de lapiz desde store.
# Luego revisa el valor de lapiz_stock para ver el acceso anidado.
lapiz_stock =

# TODO 27: cambia el stock de lapiz a 40 dentro de store.
# Luego revisa el valor de updated_lapiz_stock y store para ver el cambio anidado.
updated_lapiz_stock =

# TODO 28: crea base_product y product_details.
# base_product debe tener name="cuaderno" y price=8.0.
# product_details debe tener stock=12 y category="papeleria".
# Luego revisa el valor de base_product y product_details.
base_product =
product_details =

# TODO 29: crea merged_product combinando base_product y product_details con **.
# Luego revisa el valor de merged_product para ver el diccionario combinado.
merged_product =

# TODO 30: crea un diccionario codes con LPZ="lapiz" y CDR="cuaderno".
# Luego revisa el valor de codes para ver los codigos.
codes =

# TODO 31: invierte codes usando dict comprehension.
# Luego revisa el valor de inverted_codes para ver claves y valores invertidos.
inverted_codes =

# TODO 32: crea keys y values para formar un producto con zip().
# keys debe tener "name", "price" y "stock".
# values debe tener "mochila", 45.0 y 5.
# Luego revisa el valor de keys y values.
keys =
values =

# TODO 33: crea product_from_zip usando dict(zip(keys, values)).
# Luego revisa el valor de product_from_zip para ver el diccionario creado.
product_from_zip =

# TODO 34: crea una funcion calculate_inventory_value que reciba price y stock.
# Debe retornar price * stock.
# Luego usa la funcion en el siguiente TODO.
def calculate_inventory_value(price, stock):
    return


# TODO 35: crea value_data con price y stock desde product.
# Luego llama calculate_inventory_value desempaquetando value_data con **.
# Revisa el valor de value_data y inventory_value.
value_data =
inventory_value =
