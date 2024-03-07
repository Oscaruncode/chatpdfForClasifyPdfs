import subprocess

path="./pdfs/"

# Ejecutar un comando de Bash
resultado = subprocess.run(["ls"], capture_output=True, text=True, cwd="./pdfs")

if resultado.returncode == 0:
    print("Salida del comando:")
    print(resultado.stdout.split('\n'))
else:# Verificar si la ejecución fue exitosa
    print("Error al ejecutar el comando:")
    print(resultado.stderr)

lines=resultado.stdout.split('\n')
paths = list(map(lambda x: path + x, lines))
print(paths)

for path in paths[:-1]:
    print(path)



