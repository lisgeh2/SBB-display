import io, time, requests
from PIL import Image
from luma.core.interface.serial import spi
from luma.oled.device import ssd1322

device = ssd1322(spi(port=0, device=0, gpio_DC=24, gpio_RST=25))
URL = "http://your-server:8000/board.png?token=my-secret"

while True:
    img = Image.open(io.BytesIO(requests.get(URL).content))
    device.display(img.convert(device.mode))
    time.sleep(10)