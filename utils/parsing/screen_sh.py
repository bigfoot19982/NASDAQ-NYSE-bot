from selenium import webdriver
from PIL import Image
from io import BytesIO

fox = webdriver.Firefox()
fox.get('http://stackoverflow.com/')

# now that we have the preliminary stuff out of the way time to get that image :D
element = fox.find_element("60629")  # find part of the page you want image of
location = element.location
size = element.size
png = fox.get_screenshot_as_png()  # saves screenshot of entire page
fox.quit()

im = Image.open(BytesIO())  # uses PIL library to open image in memory

left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']

im = im.crop((left, top, right, bottom))  # defines crop points
im.save('screenshot.png')  # saves new cropped image


# https://overcoder.net/q/88587/%D0%BA%D0%B0%D0%BA-%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C-%D1%87%D0%B0%D1%81%D1%82%D0%B8%D1%87%D0%BD%D1%8B%D0%B9-%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82-%D1%81-selenium-webdriver-%D0%B2-python