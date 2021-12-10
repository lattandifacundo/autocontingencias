import os, decouple
import update, scan

RADAR_URL = decouple.config('RADAR_URL')

update.update(RADAR_URL)
if os.path.isfile("sur.png"):
    print("✔ Descarga exitosa")
else:
    print("❌ Error al descargar la imagen")
    exit(1)

scan.scan('sur.png')
os.remove('sur.png')