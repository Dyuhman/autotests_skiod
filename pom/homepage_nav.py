from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '#menu>.menu-link>a'
        self.NAV_LINK_TEXT = 'РЕЕСТР НАБОРОВ ДАННЫХ,МЕТА-КАРТА ДАННЫХ,РЕЕСТР НСИ,ВЕБ-СЕРВИСЫ,НОВОСТИ'

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return ",".join(nav_links_text)
