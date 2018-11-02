from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

class PageBase:

    def __init__(self):
        '创建浏览器对象'
        self.driver = webdriver.Chrome()

    def _open_page(self):
        '打开登录界面'
        self.driver.get('http://localhost/agileone/')

    def _find_ele(self, loc, val):
        '''
        查找元素
        loc = 定位方式
        val = 输入值
        '''
        loc = loc.lower() #转化为小写

        if loc == 'id':
            ele = self.driver.find_element_by_id(val)
        elif loc == "name":
            ele = self.driver.find_element_by_name(val)
        elif loc == "class_name":
            ele = self.driver.find_element_by_class_name(val)
        elif loc == "link_text":
            ele = self.driver.find_element_by_link_text(val)
        elif loc == "partial_link_text":
            ele = self.driver.find_element_by_partial_link_text(val)
        elif loc == "tag_name":
            ele = self.driver.find_element_by_tag_name(val)
        elif loc == "xpath":
            ele = self.driver.find_element_by_xpath(val)
        elif loc == "css_selector":
            ele = self.driver.find_element_by_css_selector(val)
        else:
            raise Exception #若输入其他loc值，报错
        return ele #返回被找到的对象

    def _im_wait(self, time):
        '隐式等待'
        self.driver.implicitly_wait(time)

    def _frame(self, ele):
        '跳转至指定表单'
        self.driver.switch_to.frame(ele)

    def _frame_parent(self):
        '跳转至上一层表单'
        self.driver.switch_to.parent_frame()

    def _send_keys(self, ele, val):
        '''
        发送数据
        ele = 元素
        val = 值
        '''
        ele.send_keys(val)

    def _click(self, ele):
        '鼠标左击'
        ele.click()

    def _url(self):
        '获取当前页面网址'
        url = self.driver.current_url
        return url
    
    def _select_option(self, ele, val):
        '''
        下拉框选择
        ele = 元素
        val = 值
        '''
        so = Select(ele)
        # so.select_by_visible_text(val) 按照文本选择
        so.select_by_index(val) # 按照索引选择
        # so.select_by_value(val) 按照value值选择

    def _ele_value(self, ele):
        '''
        获取value值
        ele = 元素
        '''
        return ele.get_attribute('value')


    def _ele_text(self, ele):
        '''
        获取text文本
        ele = 元素
        '''
        return ele.text


    def _quit(self):
        self.driver.quit()
    
    def _close(self):
        self.driver.close()

    def _clear(self, ele):
        '清除内容'
        ele.send_keys(Keys.CONTROL,'a')
        sleep(1)
        ele.send_keys(Keys.BACK_SPACE)

    def Unicode(self):
        '输入单个汉字'
        val = random.randint(0x4e00, 0x9fbf)
        return chr(val)

    def _eimg(self, fl, img_name):
        '截图'
        _eimg_path = "%s/%s" % (fl, img_name)
        self.driver.get_screenshot_as_file(_eimg_path)