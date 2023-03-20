import locale
locale.setlocale(locale.LC_ALL, '')
print("====BIENVENIDO AL FORMULARIO DE DATOS BÁSICOS DEL CURSO DE FUNDAMENTOS DE PROGRAMACIÓN EN PYTHON====")
identificacion= input("Por favor ingresar el número de identificacion: ")
nombres= input("Por favor ingresar el nombre: ")
apellidos= input("Por favor ingresar los apellidos: ")
direccion= input("Por favor ingresar la dirección: ")
telefono= input("Por favor ingresar el número de teléfono: ")
edad= input("Por favor ingresar la edad en años: ")
estado_civil= input("Por favor ingresar el estado civil: ")
numero_hijos= input("Por favor ingresar número de hijos: ")
estatura= input("Por favor ingresar la estatura en centimetros: ")
fecha_contratacion= input("Por favor ingresar la fecha de contratación en el formato: DD/MM/AAAA: ")
sueldo_basico= input("Por favor ingresar el sueldo básico en COP, sin puntuación: ")
dias_laborados= input("Por favor ingresar los días laborados: ")
print("====LOS DATOS INGRESADOS FUERON: =========")
print("Número de identificacion: ", identificacion)
print("Nombre completo: ", nombres, apellidos)
print("Dirección: ", direccion)
print("Teléfono: ", telefono)
print("Edad: ",edad,"años")
print("Estado civil: ", estado_civil)
print("Número de hijos: ", numero_hijos)
print("Estatura: ",estatura,"cm")
print("Fecha de contratación: ", fecha_contratacion)
print("Sueldo básico: ", locale.format_string('%.2f', float(sueldo_basico), grouping=True, monetary=True), "COP")
print("Días laborados: ",dias_laborados)