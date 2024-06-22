
######################################'''ОТОБРАЖЕНИЕ СТРАНИЦЫ ТОВАРА'''################################################

# import time
# from selenium import webdriver # импортируем webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common import alert
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
#
# driver.implicitly_wait(5)
#
# my_account_btn = driver.find_element_by_id("menu-item-50")
# my_account_btn.click()
#
# username_fld = driver.find_element_by_id("username")
# username_fld.send_keys("ip32142856@gmail.com")
#
# password_login_fld = driver.find_element_by_id("password")
# password_login_fld.send_keys(7894556123)
#
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
#
# shop_btn = driver.find_element_by_id("menu-item-40")
# shop_btn.click()
#
# book_btn = driver.find_element_by_css_selector('[title="Mastering HTML5 Forms"]')
# book_btn.click()
#
# title = driver.find_element_by_class_name("entry-title")
# title_text = title.text
# assert title_text == "HTML5 Forms"
#
#
#
# driver.quit()



############################################'''КОЛИЧЕСТВО ТОВАРОВ В КАТЕГОРИИ'''#######################################
#
#
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common import alert
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
#
# driver.implicitly_wait(5)
#
# my_account_btn = driver.find_element_by_id("menu-item-50")
# my_account_btn.click()
#
# username_fld = driver.find_element_by_id("username")
# username_fld.send_keys("ip32142856@gmail.com")
#
# password_login_fld = driver.find_element_by_id("password")
# password_login_fld.send_keys(7894556123)
#
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
#
# shop_btn = driver.find_element_by_id("menu-item-40")
# shop_btn.click()
#
# html_btn = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/product-category/html/"]')
# html_btn.click()
#
# books_item = driver.find_elements_by_class_name("has-post-title")
# if len(books_item) == 3:
#     print("Количсетво товаров в категории 3")
# else:
#     print("Ошибка. Количество товаров в категории: " + str(len(books_item)))
#
# driver.quit()
#



##############################################'''СОРТИРОВКА ТОВАРА'''##################################################
#
# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver # импортируем webdriver
# from selenium.webdriver.common import alert
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
#
# driver.implicitly_wait(5)
#
# my_account_btn = driver.find_element_by_id("menu-item-50")
# my_account_btn.click()
#
# username_fld = driver.find_element_by_id("username")
# username_fld.send_keys("ip32142856@gmail.com")
#
# password_login_fld = driver.find_element_by_id("password")
# password_login_fld.send_keys(7894556123)
#
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
#
# shop_btn = driver.find_element_by_id("menu-item-40")
# shop_btn.click()
#
# selector = driver.find_element_by_css_selector('option:nth-child(1)')
# selector_text = selector.text
# assert selector_text == "Default sorting"
#
# select_btn = driver.find_element_by_class_name('orderby')
# select_btn.click()
#
# driver.find_element_by_css_selector("option:nth-child(6)").click()
#
# select_btn_two = driver.find_element_by_class_name('orderby')
#
# selector_two = driver.find_element_by_css_selector('option:nth-child(6)')
# selector_two_text = selector_two.text
# assert selector_two_text == "Sort by price: high to low"
#
# driver.quit()
#
#
#
#

############################################'''ОТОБРАЖЕНИЕ СКИДКА ТОВАРА'''############################################

#
# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver # импортируем webdriver
# from selenium.webdriver.common import alert
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
#
# driver.implicitly_wait(5)
#
# my_account_btn = driver.find_element_by_id("menu-item-50")
# my_account_btn.click()
#
# username_fld = driver.find_element_by_id("username")
# username_fld.send_keys("ip32142856@gmail.com")
#
# password_login_fld = driver.find_element_by_id("password")
# password_login_fld.send_keys(7894556123)
#
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
#
# shop_btn = driver.find_element_by_id("menu-item-40")
# shop_btn.click()
#
# book_btn = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]')
# book_btn.click()
#
# old_price = driver.find_element_by_css_selector("del>span")
# old_price_text = old_price.text
# assert old_price_text == "₹600.00"
#
# new_price = driver.find_element_by_css_selector("ins>span")
# new_price_text = new_price.text
# assert new_price_text == "₹450.00"
#
# img_btn = WebDriverWait(driver, 20).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, ".wp-post-image")))
#
# img_btn.click()
#
# close_btn = WebDriverWait(driver,20).until(
# EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
#
# close_btn.click()
#
# driver.quit()


##########################################'''ПРОВЕРКА ЦЕНЫ В КОРЗИНЕ'''#################################################
#
#
# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver # импортируем webdriver
# from selenium.webdriver.common import alert
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
#
# driver.implicitly_wait(10)
#
# shop_btn = driver.find_element_by_id("menu-item-40")
# shop_btn.click()
#
# add_basket = driver.find_element_by_css_selector("div>ul>li:nth-child(4)>a:nth-child(2)")
# add_basket.click()
#
# cart_item = driver.find_element_by_class_name("cartcontents")
# cart_item_text = cart_item.text
# assert cart_item_text == "1 item"
#
# price_item = driver.find_element_by_css_selector("nav>ul>li:nth-child(6)>a>.amount")
# price_item_text = price_item.text
# assert price_item_text == "₹180.00"
#
# basket_btn = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0")
# basket_btn.click()
#
# time.sleep(3)
#
# price_amount = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element(By.CSS_SELECTOR("tr.cart-subtotal>td>span"), "₹180.00"))
#
# price_total = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element(By.CSS_SELECTOR("tr.order-total>td>strong>span"), "₹183.60")
#
# driver.quit()


###############################################'''РАБОТА В КОРЗИНЕ'''###################################################

#
# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver # импортируем webdriver
# from selenium.webdriver.common import alert
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
#
# driver.implicitly_wait(10)
#
# shop_btn = driver.find_element_by_id("menu-item-40")
# shop_btn.click()
#
# driver.execute_script("window.scrollBy(0, 400);")
#
# book_btn = driver.find_element_by_css_selector('[data-product_id="182"]')
# book_btn.click()
#
# time.sleep(3)
#
# driver.execute_script("window.scrollBy(0, 200);")
#
# book_btn_two = driver.find_element_by_css_selector('[data-product_id="180"]')
# book_btn_two.click()
#
# basket_btn = driver.find_element_by_class_name("wpmenucart-contents")
# basket_btn.click()
#
# time.sleep(3)
#
# delete_btn = driver.find_element_by_css_selector('[data-product_id="182"]')
# delete_btn.click()
#
# undo_btn = driver.find_element_by_css_selector('div.woocommerce-message>a')
# undo_btn.click()
#
# quantity_fld = driver.find_element_by_css_selector('[name="cart[4c5bde74a8f110656874902f07378009][qty]"]')
# quantity_fld.clear()
# quantity_fld.send_keys(3)
#
# update_btn = driver.find_element_by_name("update_cart")
# update_btn.click()
#
# quantity_fld_value = quantity_fld.get_attribute("value")
# assert quantity_fld_value == "3"
#
# time.sleep(3)
#
# coupon_btn = driver.find_element_by_css_selector("tr>td>div.coupon>input:nth-child(3)")
# coupon_btn.click()
#
# coupon_enter = driver.find_element_by_css_selector("div>ul.woocommerce-error>li")
# coupon_enter_text = coupon_enter.text
# assert coupon_enter_text == "Please enter a coupon code."
#
# driver.quit()
#


###############################################'''ПОКУПКА ТОВАРА'''####################################################



import time
from selenium.webdriver.support.select import Select
from selenium import webdriver # импортируем webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

driver.implicitly_wait(5)

shop_btn = driver.find_element_by_id("menu-item-40")
shop_btn.click()

driver.execute_script("window.scrollBy(0, 300);")

book_btn = driver.find_element_by_css_selector('[data-product_id="182"]')
book_btn.click()

basket_btn = driver.find_element_by_class_name("wpmenucart-contents")
basket_btn.click()

time.sleep(3)

proceed_btn = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button.alt.wc-forward")))
#proceed_btn = driver.find_element_by_css_selector(".button.alt.wc-forward")
proceed_btn.click()

first_name_fld = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name_fld.send_keys("Visual")

last_name_fld = driver.find_element_by_id("billing_last_name")
last_name_fld.send_keys("Memorial")

mail_fld = driver.find_element_by_id("billing_email_field")
mail_fld.send_keys("ip32142856@gmail.com")

phone_fld = driver.find_element_by_id("billing_phone")
phone_fld.send_keys("7984561237")

selector_btn = driver.find_element_by_css_selector("p>div>a")
selector_btn.click()

select_fld = driver.find_element_by_id("s2id_autogen1_search")
select_fld.send_keys("Russia")

country_btn = driver.find_element_by_class_name("select2-match")
country_btn.click()

street_address_fld = driver.find_element_by_id("billing_address_1")
street_address_fld.send_keys("Volga")

town_fld = driver.find_element_by_id("billing_city")
town_fld.send_keys("Moscow")

state_fld = driver.find_element_by_id("billing_state")
state_fld.send_keys("Russia")

postcode_fld = driver.find_element_by_id("billing_postcode")
postcode_fld.send_keys("789456")

driver.execute_script("window.scrollBy(0, 600);")

time.sleep(3)

radio_btn = driver.find_element_by_id("payment_method_cheque")
radio_btn.click()

place_order_btn = driver.find_element_by_id("place_order")
place_order_btn.click()

element_thx = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(By.CLASS_NAME("woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

time.sleep(3)

payment_method = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(By.CSS_SELECTOR("tfoot>tr:nth-child(3)>td"), "Check Payments"))

driver.quit()


















