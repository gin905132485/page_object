import unittest,random
from page.login import Login
from time import sleep,strftime
from common.log import Log

class LoginTestCase001(unittest.TestCase):

    def setUp(self):

        #打开缺陷跟踪页面

        self.a = Login()
        self.a.login('admin', 'admin')
        self.a._click(self.a._find_ele("partial_link_text", '缺陷跟踪'))
        sleep(1)
        self.b = Log()

    def tearDown(self):
        sleep(3)
        self.a._quit()

    def test001(self):

        '填写标题：字符数20（该标题未被创建），填写内容：字符数10，新建成功'
        #dataPanel > tr:nth-child(1) > td:nth-child(2)   新创建的报告元素定位

        _t = str(random.randint(1*10**19,9.9*10**19))
        _r = '4455667788'
        self.a._send_keys(self.a._find_ele('id', 'headline'), _t)
        frame_ele = self.a._find_ele('class_name', 'ke-iframe')
        self.a._frame(frame_ele)
        self.a._send_keys(self.a._find_ele('tag_name', 'body'), _r)
        self.a._frame_parent()
        self.a._click(self.a._find_ele('id', 'add'))
        sleep(2)

        _t_ = self.a._ele_text(self.a._find_ele('css_selector', '''#dataPanel
        > tr:nth-child(1) > td:nth-child(2)'''))
        try:
            self.assertEqual(_t, _t_, msg='填写标题：字符数20（该标题未被创建），填写内容：字符数10，新建失败')
        except:
            self.a._eimg(Log.fl_path, 'LoginTestCase001_test001.png')
            raise

    def test002(self):

        '填写标题：字符数80（该标题未被创建），填写内容：字符数10，新建成功'
        #dataPanel > tr:nth-child(1) > td:nth-child(2)   新创建的报告元素定位

        _t = str(random.randint(1*10**79,9.9*10**79))
        _r = '4455667788'
        self.a._send_keys(self.a._find_ele('id', 'headline'), _t)
        frame_ele = self.a._find_ele('class_name', 'ke-iframe')
        self.a._frame(frame_ele)
        self.a._send_keys(self.a._find_ele('tag_name', 'body'), _r)
        self.a._frame_parent()
        self.a._click(self.a._find_ele('id', 'add'))
        sleep(2)

        _t_ = self.a._ele_text(self.a._find_ele('css_selector', '''#dataPanel
        > tr:nth-child(1) > td:nth-child(2)'''))
        try:
            self.assertEqual(_t, _t_, msg='填写标题：字符数80（该标题未被创建），填写内容：字符数10，新建失败')
        except:
            self.a._eimg(Log.fl_path, 'LoginTestCase001_test002.png')
            raise

    def test003(self):

        '填写标题：字符数81，填写内容：字符数10，新建失败'
        #dataPanel > tr:nth-child(1) > td:nth-child(2)   新创建的报告元素定位
        _t = str(random.randint(1*10**80,9.9*10**80))
        _r = '4455667788'

        self.a._send_keys(self.a._find_ele('id', 'headline'), _t)
        frame_ele = self.a._find_ele('class_name', 'ke-iframe')
        self.a._frame(frame_ele)
        self.a._send_keys(self.a._find_ele('tag_name', 'body'), _r)
        self.a._frame_parent()
        self.a._click(self.a._find_ele('id', 'add'))
        sleep(2)

        _t_ = self.a._ele_text(self.a._find_ele('css_selector', '''#dataPanel
        > tr:nth-child(1) > td:nth-child(2)'''))

        try:
            self.assertNotEqual(_t, _t_, msg='字符数超过80，但创建成功')
        except:
            self.a._eimg(Log.fl_path, 'LoginTestCase001_test003.png')
            raise

    def test004(self):

        '填写标题：字符数1（该标题未被创建），填写内容：字符数10，新建成功'
        #dataPanel > tr:nth-child(1) > td:nth-child(2)   新创建的报告元素定位

        _t = str(self.a.Unicode())
        _r = '4455667788'

        self.a._send_keys(self.a._find_ele('id', 'headline'), _t)
        frame_ele = self.a._find_ele('class_name', 'ke-iframe')
        self.a._frame(frame_ele)
        self.a._send_keys(self.a._find_ele('tag_name', 'body'), _r)
        self.a._frame_parent()
        self.a._click(self.a._find_ele('id', 'add'))
        sleep(2)

        _t_ = self.a._ele_text(self.a._find_ele('css_selector', '''#dataPanel
        > tr:nth-child(1) > td:nth-child(2)'''))
        try:
            self.assertEqual(_t, _t_, msg='填写标题：字符数1（该标题未被创建），填写内容：字符数10，新建失败')
        except:
            self.a._eimg(Log.fl_path, 'LoginTestCase001_test004.png')
            raise

if __name__ == '__main__':
    unittest.main()