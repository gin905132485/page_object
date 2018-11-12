import unittest,random
from page.login import Login
from time import sleep
from common.log import Log

class LoginTestCase002(unittest.TestCase):

    def setUp(self):

        #打开缺陷跟踪页面

        self.a = Login()
        self.a.login('admin', 'admin')
        self.a._click(self.a._find_ele("partial_link_text", '缺陷跟踪'))
        sleep(1)

    def tearDown(self):
        sleep(3)
        self.a._quit()

    def test001(self):

        '填写空标题，填写内容：字符数6，新建失败'

        _err_msg = '出错啦: 缺陷标题不能为空 ...'
        _t = ''
        _r = '445566'

        self.a._send_keys(self.a._find_ele('id', 'headline'), _t)
        frame_ele = self.a._find_ele('class_name', 'ke-iframe')
        self.a._frame(frame_ele)
        self.a._send_keys(self.a._find_ele('tag_name', 'body'), _r)
        self.a._frame_parent()
        self.a._click(self.a._find_ele('id', 'add'))
        sleep(1)

        _err_msg_ = self.a._ele_text(self.a._find_ele('id', 'msg'))

        try:
            self.assertEqual(_err_msg, _err_msg_, msg='填写空标题，填写内容：字符数6，新建成功')
        except:
            self.a._eimg(Log.fl_path, 'LoginTestCase002_test001.png')
            raise

    def test002(self):

        '填写标题:字符数20（该标题未被创建），填写空内容，新建失败'

        _err_msg = '出错啦: 缺陷内容不能为空 ...'
        _t = str(random.randint(1*10**19,9.9*10**19))
        _r = ''

        self.a._send_keys(self.a._find_ele('id', 'headline'), _t)
        frame_ele = self.a._find_ele('class_name', 'ke-iframe')
        self.a._frame(frame_ele)
        self.a._send_keys(self.a._find_ele('tag_name', 'body'), _r)
        self.a._frame_parent()
        self.a._click(self.a._find_ele('id', 'add'))
        sleep(1)

        _err_msg_ = self.a._ele_text(self.a._find_ele('id', 'msg'))

        try:
            self.assertEqual(_err_msg, _err_msg_, msg='''填写标题:字符数20（该标题未被创建），
            填写空内容，新建成功''')
        except:
            self.a._eimg(Log.fl_path, 'LoginTestCase002_test002.png')
            raise

if __name__ == '__main__':
    unittest.main()