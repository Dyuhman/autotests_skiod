import time

import pytest

from pom.homepage_nav import HomepageNav
from pom.registrynsi import RegistryNSI


@pytest.mark.usefixtures('setup')
class TestRegistryNSI:
    def test_nav_link_registrynsi(self):
        actual_result = HomepageNav(self.driver).get_nav_links()[2].text
        expected_result = RegistryNSI(self.driver).NAME_MODULE_TEXT
        assert actual_result == expected_result, 'Валидация названия раздела Реестра НСИ на главной странице'

    def test_headers_table_text(self):
        HomepageNav(self.driver).get_nav_links()[2].click()  # Нажать на Реестр НСИ
        headers_table = RegistryNSI(self.driver)
        actual_result = headers_table.get_header_table_text()
        expected_result = headers_table.HEADER_TABLE_TEXT
        assert actual_result == expected_result, 'Валидация названий колонок таблицы Реестра НСИ'

    # def test_export_registry(self):
    #     HomepageNav(self.driver).get_nav_links()[2].click()  # Нажать на Реестр НСИ
    #     RegistryNSI(self.driver).get_export_button().click()
    #     # Здесь должно быть: Корректность выгружаемого файла
    #     # Здесь должно быть: Удаление файла
    #     time.sleep(3)

    def test_search_namedoc(self):
        HomepageNav(self.driver).get_nav_links()[2].click()  # Нажать на Реестр НСИ
        