nombre_curso = "Ultimate Python"
descripcion_curso = """
Ultimate Python: este curso contempla todo lo que necesitas aprender para un trabajo como programador.
"""
print(nombre_curso, descripcion_curso)  # Concatena strings
print(len(nombre_curso))  # Cuenta la cantidad de caracteres
print(nombre_curso[0])  # Posicion 0
print(nombre_curso.rsplit())  # Divide el string de derecha a izquierda
print(nombre_curso[0:5])  # Si no se coloca el valor, Python tomara todo
print(nombre_curso[8:])  # Si no se coloca el valor, Python tomara todo
print(nombre_curso[:6])  # Si no se coloca el valor, Python tomara todo
print(nombre_curso[:])  # Si no se coloca el valor, Python tomara todo
print("Ultimate" in nombre_curso)  # True o False
