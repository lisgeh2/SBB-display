from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

import requests, time
CURRENT_STATION = "Zürich, Waldgarten"
IMG_NAME = "board.png"


def get_station_info(current_station=CURRENT_STATION):
    r = requests.get("https://transport.opendata.ch/v1/stationboard",
                    params={"station": current_station, "limit": 7})
    lines = []
    # print(r.json()["stationboard"])
    for d in r.json()["stationboard"]:
        mins = int((d["stop"]["departureTimestamp"] - time.time()) // 60)
        if mins>0:
            lines.append((d["number"], d["to"], f"{mins}'"))
        
    return lines


def write_board_image(lines = None):
    if lines is None:
        lines = get_station_info()

    img = Image.new("L", (256, 64), 0)          # "L" = grayscale, 0 = black
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arialbd.ttf", 13)   # Arial Bold

    for i, (line, dest, mins) in enumerate(lines):
        y = i * 16
        draw.text((0, y), line, fill=255, font=font)     # 255 = full brightness
        draw.text((26, y), dest, fill=180, font=font)    # a bit dimmer
        draw.text((230, y), mins, fill=255, font=font)

    here = Path(__file__).parent
    img.save(here / IMG_NAME)



if __name__ == "__main__":
    print(get_station_info())
    write_board_image()