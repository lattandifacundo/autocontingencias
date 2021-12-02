import os
import dotenv

dotenv.load_dotenv()

RADAR_URL = os.getenv('RADAR_URL')

import util, image, scan

image.update(RADAR_URL)
scan.scan()
util.show()


