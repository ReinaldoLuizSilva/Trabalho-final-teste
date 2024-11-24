from selenium import webdriver

class Browser(object):
    #escolher o navegador
    driver = webdriver.Chrome()
    #definir o tempo de espera (configura tempo de timeout)
    driver.set_page_load_timeout(30)
    #maximizar a janela do navegador
    driver.maximize_window()

    #Função pra fechar o navegador
    def browser_quit(self):
        self.driver.quit()

    #Função pra limpar o navegador
    def browser_clear(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script('localStorage.clear();')
        self.driver.execute_script('sessionStorage.clear();')
        self.driver.refresh()
