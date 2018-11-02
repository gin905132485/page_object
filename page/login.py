from page_base import PageBase
import time

class Login(PageBase):

    '登录'

    def login(self, usr, pw):
        user_ele = ('id', 'username')
        pw_ele = ('id', 'password')
        save_ele = ('id', 'savelogin')
        login_ele = ('id', 'login')
        self._im_wait(3)
        self._open_page() #打开页面
        self._send_keys(self._find_ele(user_ele[0],user_ele[1]), usr) #输入用户名
        self._send_keys(self._find_ele(pw_ele[0], pw_ele[1]), pw) #输入密码
        self._click(self._find_ele(save_ele[0], save_ele[1])) #取消保存用户信息
        self._click(self._find_ele(login_ele[0], login_ele[1])) #点击登录按钮
        
if __name__ == '__main__':
    a = Login()
    a.login('admin', 'admin')


