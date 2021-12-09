from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import random
from selenium.webdriver.common.keys import Keys

class paybot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.ysense.com/offer-wall/?wall=offertoro")
        sleep(30)
        self.driver.switch_to_window(self.driver.window_handles[1])
        for u in range(50):
            for i in range(83):
                #Generacion de numeros aleatorios.--------------------
                n = random.randrange(1,3,1)
                slip = random.randrange(1,30,1)
                alt = random.randrange(1,30,1)
                old = random.randrange(1,19,1)
                altr = random.randrange(1,20,1)
                dumb = random.randrange(1,15,1)
                also = random.randrange(1,40,1)
                elfo = random.randrange(1,30,1)
                anti = random.randrange(1,40,1)
                sofa = random.randrange(1,40,1)
                prada = random.randrange(1,40,1)
                nike = random.randrange(1,49,1)
                sofal = random.randrange(1,23,1)
                partial = random.randrange(1,43,1)
                last = random.randrange(2,29,1)
                #Cierre de numeros aleatorios.------------------------
                sleep(30)
                if n == 1:
                    self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/form/fieldset/div/div[1]/label/div/div")\
                        .click()
                    sleep(slip)
                elif n == 2:
                    self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/form/fieldset/div/div[3]/label/div/div")\
                        .click()
                    sleep(alt)
                sleep(old)
                #Scroll down
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(altr)
                sleep(dumb)
                #Next primero
                sleep(20)
                try:
                    self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/form/div[4]/div/div[4]/button")\
                        .click()
                except:
                    self.driver.find_element_by_id("nextButton")
                sleep(also)
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(elfo)
                sleep(20)
                #Next button
                try:
                    self.driver.find_element_by_xpath("//*[@id='nextButton']")\
                        .click()
                    sleep(anti)
                except:
                    try:
                        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[4]/div/div[2]/button")
                    except:
                        try:
                            self.driver.find_elements_by_id("nextButton")
                        except:
                            sleep(10)
                            i+=1
                sleep(anti)
            sleep(sofa)
            #Cargar anuncio
            self.driver.find_element_by_xpath("/html/body/div[1]/nav/div/div/ul[1]/li[2]/a")
            el = self.driver.find_element_by_xpath("/html/body/div[1]/nav/div/div/ul[1]/li[2]/a")
            action = webdriver.common.action_chains.ActionChains(self.driver)
            action.move_to_element_with_offset(el, 250, 100)
            action.click()
            action.perform()
            sleep(prada)
            self.driver.switch_to_window(self.driver.window_handles[2])
            sleep(nike)
            self.driver.close()
            sleep(sofal)
            self.driver.switch_to_window(self.driver.window_handles[1])
            sleep(partial)
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div/a")
            sleep(last)
            sleep(10)
            u+=1
    
paybot()


