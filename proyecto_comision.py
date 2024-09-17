#Proyecto
nombre_usuario = input("Cual es tu nombre?: ")
venta_total = input("Cual es el monto total($) de tus ventas durante todo este mes?: ")

venta_total = float(venta_total)

comision = venta_total * 13/100
comision = round(comision, 2)

print(f"Ok {nombre_usuario}. este mes ganaste ${comision} en comisiones felicidades.")


