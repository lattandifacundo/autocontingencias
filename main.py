import os
import dotenv

dotenv.load_dotenv()

RADAR_URL = os.getenv('RADAR_URL')

import update, scan

# update.update(RADAR_URL)
if os.path.isfile("sur.png"):
    print("Download succesfull")
scan.scan()
from PIL import Image; Image.open("sur.png").show()
os.remove("sur.png")