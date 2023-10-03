from bs4 import BeautifulSoup
import os
import math
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
from cropper import crop

def download(mediatype, elem):
  if mediatype == 'image':
    r1, r2 = '.webp', '.jpg'
  elif mediatype == 'video':
    r1, r2 = '.mp4', '.mp4'
  
  src = elem.get_attribute('src')
  
  src = src.replace(r1, r2)
  src_no_extension = src.replace(r1, '')
  
  if mediatype == 'picture':
    src_no_extension = src_no_extension.replace(f'https://img.ifunny.co/{mediatype}s/', '')
  else:
    src_no_extension = src_no_extension.replace(f'https://img.ifunny.co/{mediatype}s/', '')

  response = requests.get(src)
  
  if response.status_code == 200:
    image_content = response.content

    with open(os.path.join('output', f'{src_no_extension}{r2}'), 'wb') as f:
      if r2 == '.mp4':
        f.write(response.content)
      else:
        img = crop(image_content)
        f.write(img)
    print(f'Content saved')
  else:
    print(f'Failed to save image. Status code: {response.status_code}')
    

def main():
  try:
    browser = webdriver.Firefox()
    # url = 'https://ifunny.co/video/JMlvnugrA'
    url = 'https://ifunny.co/picture/cocaine-ma-beer-apple-fritters-vFIpBQgrA'
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    mediatype = None

    if not url.find('https://ifunny.co/video/'):
      elem = browser.find_element(By.TAG_NAME, 'video')
      mediatype = 'video'


    if not url.find('https://ifunny.co/picture/'):
      elem = browser.find_element(By.XPATH, '//*[contains(@class, "f+2d")]')
      # elem = soup.find(class_='f+2d')
      if elem:
        pass
      else:
        pass
      mediatype = 'image'

    if mediatype == None:
      browser.close()
      print('error, no media type found')
      SystemExit

    if mediatype == 'image':  
      download(mediatype, elem)

    if mediatype == 'video':
      download(mediatype, elem)

    browser.close()


  except Exception as e:
    print(e)
    browser.close()
if __name__ == "__main__":
  main()
  