import time
from project.Locators.locators import Locators


class AirtimeRechargePage():
    def __init__(self, driver):
        self.driver = driver

        self.buy_airtime_button_xpath = Locators.buy_airtime_button_xpath
        self.phone_number_textbox2_id = Locators.phone_number_textbox2_id
        self.airtime_price_textbox_id = Locators.airtime_price_textbox_id
        self.next_button_id = Locators.next_button_id
        self.wallet_payment_radio_button_xpath = Locators.wallet_payment_radio_button_xpath
        self.confirm_payment_button_id = Locators.confirm_payment_button_id
        self.pay_button_id = Locators.pay_button_id
        self.success_home_button_id = Locators.success_home_button_id
        self.okay_button_id = Locators.okay_button_id

    def click_buy_airtime_button(self):
        self.driver.find_element_by_xpath(Locators.buy_airtime_button_xpath)\
            .click()

    def enter_phone_number(self, phonenumber):
        self.driver.find_element_by_id(Locators.phone_number_textbox2_id)\
            .send_keys(phonenumber)

    def enter_airtime_price(self, price):
        self.driver.find_element_by_id(Locators.airtime_price_textbox_id)\
            .send_keys(price)
        self.driver.find_element_by_id(Locators.next_button_id).click()

    def wallet_payment(self):
        self.driver.find_element_by_xpath(Locators.wallet_payment_radio_button_xpath)\
            .click()
        self.driver.find_element_by_id(Locators.confirm_payment_button_id).click()
        time.sleep(9)
        self.driver.find_element_by_id(Locators.pay_button_id).click()

    def success_payment(self):
        self.driver.find_element_by_id(Locators.success_home_button_id).click()
        time.sleep(3)
        self.driver.find_element_by_id(Locators.okay_button_id).click()










#
# class DesiredCapabilities():
#     def __init__(self, caps):
#         self.driver = caps
#
#         self.platform_name = Locators.platform_name
#         self.platform_version = Locators.platform_version
#         self.new_command_timeout = Locators.new_command_timeout
#         self.disable_window_animation = Locators.disable_window_animation
#         self.no_reset = Locators.no_reset
#         self.device_name = Locators.device_name
#         self.auto_grant_permissions = Locators.auto_grant_permissions
#         self.app_activity = Locators.app_activity
#         self.app_package = Locators.app_package
#
#     def caps(self):
#         self.dr
