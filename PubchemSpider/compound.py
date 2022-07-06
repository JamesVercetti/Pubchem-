import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import utilTools

def getSpecificInfo(seed,browser,file_dir):
    # browser=webdriver.Chrome()
    browser.get(seed)
    #强制等待
    time.sleep(1)
    #隐式等待
    browser.implicitly_wait(5)
    #显式等待
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "main-content")))
    main_content_div=browser.find_element_by_id("main-content")
    # type_div=main_content_div.find_element_by_css_selector(".flex-container.align-vertical-center.width-100")
    # print(type_div.text)
    try:
        page_download_btn=main_content_div.find_element_by_id("page-download-btn")
        page_download_btn.click()
        root_modal_div=browser.find_element_by_id("root-modal")
        modal_body_div=root_modal_div.find_element_by_css_selector(".modal-body.p-l-left.p-l-right")
        ul_div=modal_body_div.find_element_by_css_selector(".unstyled-list.relative")
        download_data_save_a=ul_div.find_elements_by_tag_name("li")[0].find_element_by_tag_name("ul").find_elements_by_tag_name("li")[1].find_element_by_tag_name("a")
        pagedata_save_href = download_data_save_a.get_attribute("href")
        print(pagedata_save_href)
        utilTools.download_file(pagedata_save_href, file_dir, ".xml")
    except:
        #将异常日志信息记录
        utilTools.writeLog("compoundLog.txt", file_dir, pagedata_save_href)
    try:
        twoD_structure_a=ul_div.find_elements_by_css_selector(".p-sm-top.p-sm-bottom")[0].find_element_by_css_selector(".unstyled-list.inline-block").find_elements_by_css_selector(".p-xsm-top.p-xsm-bottom")[0].find_element_by_tag_name("a")
        twoD_structure_href = twoD_structure_a.get_attribute("href")
        print(twoD_structure_href)
        utilTools.download_file(twoD_structure_href, file_dir, ".sdf")
    except:
        # 将异常日志信息记录
        utilTools.writeLog("compoundLog.txt", file_dir, twoD_structure_href)
    try:
        threeD_structure_a=ul_div.find_elements_by_css_selector(".p-sm-top.p-sm-bottom")[1].find_element_by_css_selector(".unstyled-list.inline-block").find_elements_by_css_selector(".p-xsm-top.p-xsm-bottom")[0].find_element_by_tag_name("a")
        threeD_structure_href=threeD_structure_a.get_attribute("href")
        print(threeD_structure_href)
        utilTools.download_file(threeD_structure_href, file_dir, ".sdf")
    except:
        # 将异常日志信息记录
        utilTools.writeLog("compoundLog.txt", file_dir, threeD_structure_href)