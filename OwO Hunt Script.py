import pyautogui, keyboard, time, requests, os, json, sys
from PIL import Image

currentpath = os.path.dirname(sys.argv[0])

with open(f"{currentpath}\config.json") as config:
    cfg = json.load(config)

userid = cfg['userid']

while True:
    try:
        if keyboard.is_pressed(cfg['startbutton']):
            while True:
                url = cfg['webhook']
                screenshot = pyautogui.screenshot()

                screenshot.save(path)
                time.sleep(1)

                img = Image.open(path)
                colors = img.getpixel((35,115))

                if colors == (70, 178, 239):
                    data = {
                    "content" : f"<@{dcid}> Achtung Captcha!"
                    }

                    result = requests.post(url, json = data)
                    try:
                        result.raise_for_status()
                    except requests.exceptions.HTTPError as err:
                        print(Error)
                    time.sleep(30)

                else:
                    url = cfg['webhook']
                    screenshot = pyautogui.screenshot()

                    screenshot.save((path))
                    time.sleep(1)

                    img = Image.open(path)
                    colors = img.getpixel((485,850))

                    if colors == (255, 204, 77):
                        data = {
                        "content" : f"<@{dcid}> Attention Captcha!"
                        }

                        result = requests.post(url, json = data)
                        try:
                            result.raise_for_status()
                        except requests.exceptions.HTTPError as err:
                            print(Error)
                        time.sleep(30)

                    else:
                        pyautogui.write('owo hunt')
                        pyautogui.press('enter')
                        time.sleep(1)
                        pyautogui.write(f"owo {cfg['mode']} all")
                        pyautogui.press('enter')
                        time.sleep(14)

    except:
        break
