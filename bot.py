from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time, random

user = ""
password = "" #credenciales cuenta instagram desde las cuales se enviara los mensajes
usuariosAEnviar = [] #lista de usuarios a los cuales se les enviara los mensajes

mensajes = ["Hola!! Perdon por la molestia, estoy buscando personas con cuentas grandes que quieran ayudarme con una encuesta sobre marketing",
            "Son solamente 6 preguntas y demora menos de un minuto!!",
            "No pedimos información personal ni nada por el estilo, es solo información para un análisis universitario, nada con fines de lucro ni nada por el estilo",
            "Gracias y perdon por la molestia posta!!!! https://forms.gle/Eym7JuTJWdFv6VRs6",
            "Gracias nuevamente!"]

# Delay time between messages in sec:
between_messages = 3

browser = webdriver.Chrome('chromedriver')

# Authorization:
def auth(username, password):
	try:
		browser.get('https://instagram.com')
		time.sleep(random.randrange(2,4))

		input_username = browser.find_element_by_name('username')
		input_password = browser.find_element_by_name('password')

		input_username.send_keys(username)
		time.sleep(random.randrange(1,2))
		input_password.send_keys(password)
		time.sleep(random.randrange(1,2))
		input_password.send_keys(Keys.ENTER)

	except Exception as err:
		print(err)
		browser.quit()

# Sending messages:
def send_message(users, messages):
  try:
    browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
    time.sleep(random.randrange(3,4))
    browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
    time.sleep(random.randrange(3,4))
    browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click()
    for user in users:
      time.sleep(random.randrange(3,4))
      browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user)
      time.sleep(random.randrange(3,4))
      pyautogui.click(855,500) #posicion hardcodeada del boton en pantalla, cuidado
      time.sleep(random.randrange(3,4))
      browser.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div/button/div').click()
      time.sleep(random.randrange(3,4))
      text_area = browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
      i=0
      while(True):
        text_area.send_keys(messages[i])
        time.sleep(random.randrange(3,4))
        text_area.send_keys(Keys.ENTER)
        time.sleep(1)
        i+=1
        if(i==5):
          break
      print(f'Message successfully sent to {user}')
      time.sleep(between_messages)
      pyautogui.click(474,306) #posicion hardcodeada del boton en pantalla, cuidado

  except Exception as err:
    print(err)
    browser.quit()


auth(user, password)
time.sleep(random.randrange(2,4))
send_message(usuariosAEnviar, mensajes)