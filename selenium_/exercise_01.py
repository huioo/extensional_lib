import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.51job.com")
elem_login = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/p/a[1]")
elem_login.click()

elem_account = driver.find_element_by_id("loginname")
elem_account.send_keys('*****')

elem_password = driver.find_element_by_id("password")
elem_password.send_keys('******')

elem_login_btn = driver.find_element_by_id("login_btn")
elem_login_btn.click()

elem_work_position = driver.find_element_by_id("work_position_input")
elem_work_position.click()
for elem_css_id in ['work_position_click_center_right_list_category_000000_080200',
                    'work_position_click_center_right_list_category_000000_090200',
                    'work_position_click_center_right_list_category_000000_030200']:
    elem = driver.find_element_by_id(elem_css_id)
    elem.click()


while True:
    elem_work_position_selected_l = driver.find_elements_by_css_selector(
        'html body div#work_position_layer.layer_class '
        'div#work_position_click_init.panel_lnp.panel_py.panel_ct.con_m '
        'div#work_position_click_multiple.panel_tags.mk '
        'div#work_position_click_multiple_selected.tin '
        'span')
    # print(elem_work_position_selected_l)
    if elem_work_position_selected_l:
        elem_work_position_selected_l[0].click()
    else:
        break


elem_work_position = driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200")
elem_work_position.click()


elem_work_position_save = driver.find_element_by_id("work_position_click_bottom_save")
elem_work_position_save.click()

elem_kwd = driver.find_element_by_id("kwdselectid")
elem_kwd.send_keys('python')
elem_kwd.send_keys(Keys.RETURN)

driver.implicitly_wait(10)   # seconds
# driver.get("http://somedomain/url_that_delays_loading")
# myDynamicElement = driver.find_element_by_id("myDynamicElement")

elem_result_l = driver.find_elements_by_css_selector(
    "html body div.dw_wp div#resultList.dw_table div.el")
# print(elem_result_l)
for elem in elem_result_l:
    # print(elem)
    a_l = elem.find_elements_by_tag_name('a')
    span_l = elem.find_elements_by_tag_name('span')

    print(*[item.text for item in a_l+span_l], sep=' | ')

# elem_search_btn.click()
# print(driver.page_source)
# driver.close()

