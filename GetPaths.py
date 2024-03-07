#On linux
import subprocess
from Consts import folderPath

def getPaths():
    # Run bash ls on paths
    filenames = subprocess.run(["ls"], capture_output=True, text=True, cwd=folderPath)

    if filenames.returncode == 0:
        lines = filenames.stdout.split('\n')
        if lines[-1] == '': lines.pop() #Delete last element because is a void quotes
        paths = list(map(lambda x: folderPath + x, lines))
        return paths
    else:
      print("Error al ejecutar el comando:")
      print(filenames.stderr)

