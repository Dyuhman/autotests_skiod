from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class RegistryNSI(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.NAME_MODULE_TEXT: str = 'РЕЕСТР НСИ'
        self.__header_table: str = '.n3__fixedtable__head>tr>th>div'
        self.HEADER_TABLE_TEXT: str = 'Наименование документа,Номер документа,Дата документа,Наименование набора данных,Поставщик,Краткое описание содержимого документа'
        self.__search_input: str = '.search-input__input'
        self.__filters_button: str = '.n3__filters__button'
        self.__filter_from_date_input: str = ''
        self.__filter_to_date_input: str = ''
        self.__submit_filters_button: str = 'n3__filters__submit-button'
        self.__reset_filters_button: str = 'n3__filters__reset-button'
        self.__export_button: str = '.nsi-export'

    def get_header_table(self) -> List[WebElement]:
        return self.are_visible('css', self.__header_table, 'Заголовки таблицы Реестра НСИ')

    def get_header_table_text(self) -> str:
        headers_table = self.get_header_table()
        headers_table_text = self.get_text_from_webelements(headers_table)
        return ",".join(headers_table_text)

    def get_search_input(self) -> WebElement:
        return self.is_visible('css', self.__search_input, 'Поисковая строка')

    def get_filters_button(self) -> WebElement:
        return self.is_visible('css', self.__filters_button, 'Кнопка фильтров')

    def get_filter_from_date_input(self) -> WebElement:
        return self.is_visible('css', self.__filter_from_date_input, 'Поле фильтра по дате С')

    def get_filter_to_date_input(self) -> WebElement:
        return self.is_visible('css', self.__filter_to_date_input, 'Поле фильтра по дате ПО')

    def get_submit_filters_button(self) -> WebElement:
        return self.is_visible('css', self.__submit_filters_button, 'Кнопка поиска по фильтрам')

    def get_reset_filters_button(self) -> WebElement:
        return self.is_visible('css', self.__reset_filters_button, 'Кнопка сброса фильтров')

    def get_export_button(self) -> WebElement:
        return self.is_visible('css', self.__export_button, 'Кнопка экспорта Реестра НСИ')
