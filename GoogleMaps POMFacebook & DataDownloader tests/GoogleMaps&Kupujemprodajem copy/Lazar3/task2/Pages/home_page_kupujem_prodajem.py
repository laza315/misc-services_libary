from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import re
from Lazar3.task2.Pages.base_page import BasePage
from Lazar3.task2.config.config import KupujemprodjameURL


class HomePage(BasePage):

    input_field = '//input[@id="keywords"]'
    displayed_items = By.XPATH, '//*[@class="AdItem_adOuterHolder__Z29Nf"]'
    get_prices = '//*[@class="AdItem_adOuterHolder__Z29Nf"]//*[@class="AdItem_price__k0rQn"]'

    def __init__(self, driver):
        super().__init__(driver)

    def open_url(self):
        self.driver.get(KupujemprodjameURL)

    def insert_what_you_searh_for(self, enter):
        self.driver.find_element(By.XPATH, self.input_field).click()
        self.driver.find_element(By.XPATH, self.input_field).send_keys(enter)
        action = ActionChains(self.driver)
        action.send_keys(Keys.ENTER).perform()

    def verify_displayed_items(self):
        self.is_visible(self.displayed_items)
        list_of_offers = self.driver.find_elements(By.XPATH, self.get_prices)
        print(len(list_of_offers))
        print(type(list_of_offers))
        all_prices = list(map(lambda x: x.text.strip(' din'), list_of_offers))
        all_prices = list(filter(lambda x: x != "Dogovor", all_prices))
        all_prices = list(map(lambda x: x.replace('.', ''), all_prices))
        print(list(all_prices))
        casted_prices = []
        for element in all_prices:
            if '€' in element:
                element = float(element.replace('€', '').replace(',', '.')) *100
            element = float(element)
            casted_prices.append(element)
        print(casted_prices)
        average_price = (sum(casted_prices) / len(casted_prices))
        print(average_price)






        #   all_prices = (''.join(e for e in string if e.isalnum()), all_prices)

        # if string in all_prices:
        #     ''.join(e for e in string if e.isalnum())
        #      print(list(all_prices).append())
        # for element in list_of_offers:
        #     all_prices = element.text
        #     cena = all_prices.strip(" din")
        #     print(cena)
        # for element in list_of_offers:
        #     all_prices = element.text
        #     dogovor = all_prices.strip("Dogovor")
        #     print(dogovor)

        # y = 'Dogovor'
        # new_list = [list_of_offers]
        # if y in list_of_offers:
        #     list_of_offers.remove("Dogovor")
        #     print(new_list)


        # for dogovor in cene:
        #     all_prices = dogovor.text
        #     dogovor = all_prices.strip("Dogovor")
        # new_list = []
        # new_list.extend(cena)
        # for el in dogovor:
        #     if el not in new_list:
        #         new_list.append(el)
        # print("Union of the lists is:", new_list)


        # y = 'Dogovor'
        # new_list = [all_prices]
        # if y in all_prices:
        #     new_list.remove(y)
        #     print(new_list)
            # zameni = 'din'
            # if zameni in all_prices:
            #     mylst = ([s.strip(' din') for s in all_prices])
            #     for i in range(0, len(mylst)):
            #         mylst[i] = int(mylst[i])
            #         print(mylst)


                #my_float = float(mylst.replace(',', '').replace('%', ''))

                # for i in range(0, len(mylst)):
                #     mylst[i] = int(mylst[i])
            # y = 'Dogovor'
            # new_list = [all_prices]
            # if y in all_prices:
            #     new_list.remove(y)
            #     print(new_list)




            #      empty_string = list.replace("[A-z/€]", "")
            # list.__add__(empty_string)

        #
        # for element in cene:
        #     all_prices = element.text
        #     nova_lista = [all_prices]
        #     k = 'Dogovor'
        #     if k in nova_lista:
        #         nova_lista.remove(k)
        #     # print(nova_lista)
        #     res = [float(ele) for ele in nova_lista]
        #     print(res)
        # lista = [all_prices]
        # total = 0
        # for element in lista:
        #     if isinstance(element, int) or element.isdigit():
        #         total += int(element)
        # print(lista)


        # broj = float(x) for x in nova_lista






                #  = sum(filter(lambda i: isinstance(i, int), nova_lista))
                # print(res)


            # napravi int listu
                                      # if statemant koji ce da prodje kroz listu
                                      # ako ima
            #
            # def average():
            #     saberi = sum(val for val in range(prevedi)
            #            if isinstance(val, (int, float)))
            #     print(dir(saberi))
            #     zbir = sum(prevedi)
            #     print(zbir)
            # average()

        # result = sum(filter(lambda i: isinstance(i, int), brojke))
        # print(result)

        # def average():
        #     nestp =  sum(val for val in all_prices
        #                if isinstance(val, (int)))
        #     print(nestp)

