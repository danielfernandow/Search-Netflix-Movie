from selenium.webdriver import Firefox
import time


class Search:
    # construtor do programa.

    def __init__(self, text, user, password, driver):
        self.text = text
        self.user = user
        self.password = password
        self.driver = driver
        self.url = 'https://www.netflix.com/browse'

    # chamar a inicializacao da page
    def chamar(self):
        self.driver.get(self.url)

    # operando
    def operar(self):
        id = self.driver.find_element_by_name('userLoginId')
        id.send_keys(self.user)
        time.sleep(1)
        password = self.driver.find_element_by_name('password')
        password.send_keys(self.password)
        password.submit()
        time.sleep(3)
        person = self.driver.find_element_by_xpath(
            '//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a/span')
        person.click()
        search_bar = self.driver.find_element_by_class_name('searchTab')
        search_bar.click()
        type_search = self.driver.find_element_by_name('searchInput')
        type_search.send_keys(self.text)
        time.sleep(3)
        click_movie = self.driver.find_element_by_id('title-card-0-0')
        click_movie.click()
        play_video = self.driver.find_element_by_class_name('ltr-18i00qw')
        play_video.click()


browser = Firefox()
userr = input('Digite seu user: ' )
passw = input('Digite seu passoword: ')
filme_name = input('Digite o nome do filme: ')

start = Search(filme_name, userr, passw, browser)
start.chamar()
start.operar()
