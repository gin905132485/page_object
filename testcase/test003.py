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

        '测试编辑功能'

        self.a._click(self.a._find_ele('css_selector', '''#dataPanel > 
                tr:nth-child(1) > td:nth-child(7) > label'''))
        sleep(1)
        _id_ = self.a._ele_value(self.a._find_ele('id', 'defectid'))

        _err_msg = '成功啦: 更新数据成功 -> 编号=%s' % _id_
        sleep(1)

        self.a._clear(self.a._find_ele('id', 'headline'))
        _t = str(random.randint(1*10**20,9.9*10**20))
        _r = str(random.randint(1*10**79,9.9*10**79))
        self.a._send_keys(self.a._find_ele('id', 'headline'), _t)
        frame_ele = self.a._find_ele('class_name', 'ke-iframe')
        self.a._frame(frame_ele)
        sleep(1)
        self.a._clear(self.a._find_ele('tag_name', 'body'))
        self.a._send_keys(self.a._find_ele('tag_name', 'body'), _r)
        self.a._frame_parent()
        self.a._click(self.a._find_ele('id', 'edit'))
        sleep(1)

        _err_msg_ = self.a._ele_text(self.a._find_ele('id', 'msg'))

        try:
            self.assertEqual(_err_msg, _err_msg_, msg='提示信息错误')
        except:
            self.a._eimg(Log.fl_path, 'LoginTestCase003_test001.png')
            raise

    def test002(self):

        '测试重置功能'

        _id = ''
        _creator = ''
        _createdtime = ''
        _source = ''
        _status = ''
        _severity = ''
        _priority = ''
        _module = ''
        _platform = ''
        _version = ''
        _headline = ''

        self.a._click(self.a._find_ele('id', 'reset'))
        sleep(1)
        _id_ = self.a._ele_value(self.a._find_ele('id', 'defectid'))
        _creator_ = self.a._ele_value(self.a._find_ele('id', 'creator'))
        _createdtime_ = self.a._ele_value(self.a._find_ele('id', 'createdtime'))
        _source_ = self.a._ele_value(self.a._find_ele('id', 'source'))
        _status_ = self.a._ele_value(self.a._find_ele('id', 'status'))
        _severity_ = self.a._ele_value(self.a._find_ele('id', 'severity'))
        _priority_ = self.a._ele_value(self.a._find_ele('id', 'priority')) 
        _module_ = self.a._ele_value(self.a._find_ele('id', 'module')) 
        _platform_ = self.a._ele_value(self.a._find_ele('id', 'platform')) 
        _version_ = self.a._ele_value(self.a._find_ele('id', 'version')) 
        _headline_ = self.a._ele_value(self.a._find_ele('id', 'headline')) 

        try:
            self.assertEqual(_id, _id_, msg='编号不为空')
            self.assertEqual(_creator, _creator_, msg='创建者不为空')
            self.assertEqual(_createdtime, _createdtime_, msg='创建时间不为空')
            self.assertEqual(_source, _source_, msg='缺陷来源不为空')
            self.assertEqual(_status, _status_, msg='状态不为空')   
            self.assertEqual(_severity, _severity_, msg='严重程度不为空')
            self.assertEqual(_priority, _priority_, msg='优先级不为空')
            self.assertEqual(_module, _module_, msg='所属模块不为空')
            self.assertEqual(_platform, _platform_, msg='测试平台不为空')
            self.assertEqual(_version, _version_, msg='测试版本不为空')
            self.assertEqual(_headline, _headline_, msg='标题不为空') 
        except:
            self.a._eimg(Log.fl_path, 'LoginTestCase003_test002.png')
            raise       

if __name__ == '__main__':
    unittest.main()