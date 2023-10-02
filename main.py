# import bs4 as bs
import os
import math
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
from cropper import crop
def main():
  browser = webdriver.Firefox()

  browser.get('https://ifunny.co/picture/thayla-carvalho-february-16-his-is-the-cat-of-love-PappoShrA')

  elem = browser.find_element(By.XPATH, '//*[contains(@class, "f+2d")]')

  src = elem.get_attribute('src')
  src = src.replace('.webp', '.jpg')
  src_no_extension = src.replace('.webp', '')
  src_no_extension = src_no_extension.replace('https://img.ifunny.co/images/', '')
  print(src_no_extension)

  response = requests.get(src)
  if response.status_code == 200:
    image_content = response.content
    with open(os.path.join('output', f'{src_no_extension}.jpg'), 'wb')as f:
      img = crop(image_content)
      f.write(img)
    print(f'Image saved')
  else:
    print(f'Failed to save image. Status code: {response.status_code}')
  browser.close()

if __name__ == "__main__":
  main()

  