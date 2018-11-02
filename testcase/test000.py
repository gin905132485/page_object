import unittest
from page.login import Login
from time import sleep
from common.log import Log

class LoginTestCase000(unittest.TestCase):

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

        '检查默认填写元素'

        _id = ''
        _creator = 'admin'
        _createdtime = ''
        _source = ''
        _status = 'New'
        _severity = 'Major'
        _priority = 'Medium'
        _module = ''
        _platform = ''
        _version = ''
        _headline = ''

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
            self.assertEqual(_creator, _creator_, msg='默认创建者错误')
            self.assertEqual(_createdtime, _createdtime_, msg='默认创建时间不为空')
            self.assertEqual(_source, _source_, msg='默认缺陷来源错误')
            self.assertEqual(_status, _status_, msg='默认状态错误')   
            self.assertEqual(_severity, _severity_, msg='默认严重程度错误')
            self.assertEqual(_priority, _priority_, msg='默认优先级错误')
            self.assertEqual(_module, _module_, msg='默认所属模块不为空')
            self.assertEqual(_platform, _platform_, msg='默认测试平台不为空')
            self.assertEqual(_version, _version_, msg='默认测试版本不为空')
            self.assertEqual(_headline, _headline_, msg='默认标题不为空')
        except:
            self.a._eimg(Log.fl_path, 'LoginTestCase000_test001.png')
            raise

        
    def test002(self):

        '填写已经创建过的标题，再次创建时报错'
        
        _err_msg = '出错啦: 缺陷标题已经存在 ...'

        self.a._send_keys(self.a._find_ele('id', 'headline'), '112233')
        frame_ele = self.a._find_ele('class_name', 'ke-iframe')
        self.a._frame(frame_ele)
        self.a._send_keys(self.a._find_ele('tag_name', 'body'), '445566')
        self.a._frame_parent()
        self.a._click(self.a._find_ele('id', 'add'))
        sleep(1)

        _err_msg_ = self.a._ele_text(self.a._find_ele('id', 'msg'))

        try:
            self.assertEqual(_err_msg, _err_msg_, msg='填写已经创建过的标题,再次创建时成功')
        except:
            self.a._eimg(Log.fl_path, 'LoginTestCase000_test002.png')
            raise

if __name__ == '__main__':
    unittest.main()