from selenium import webdriver
import time

class SCBSpider(object):
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.url = 'http://www.shichangbu.com'

    # 登录
    def page_log(self):
        self.browser.get(self.url)
        # 点击登录
        self.browser.find_element_by_xpath('/html/body/header/div[1]/div/div/div[2]/div/div/div/a[2]').click()
        # 用户名
        self.browser.find_element_by_id('lgp_mobile').send_keys('账号')
        # 密码
        self.browser.find_element_by_id('lgp_password').send_keys('密码')
        # 登录按钮
        self.browser.find_element_by_xpath('//*[@id="lgp_btn_login"]').click()
        time.sleep(2)
        # 点击头像进入个人
        self.browser.find_element_by_xpath('/html/body/header/div[1]/div/div/div[2]/div/div/div/div/a/img').click()
        time.sleep(1)
        # 点击我的申请
        self.browser.find_element_by_xpath('/html/body/main/div[2]/div/div[1]/div/ul[1]/li[3]/a').click()
        time.sleep(1)

    # 解析一级界面信息
    def one_page(self):
        tr_list = self.browser.find_elements_by_xpath('//*[@id="company_list_data"]')
        for tl in tr_list:
            # 返回一个列表，text化后分割后得到一个列表
            # print(tl)
            info = tl.text.split('\n')
            # print(info)
            for i in info:
                # 取倒数第三个字
                # print(i)
                # print(i[-3])
                if i[-3] == '已':
                    xp = '//tr[{}]/td[2]/a'.format(i+1)
                    tl.find_element_by_xpath(xp).click()
                    time.sleep(1)
                    self.two_page()
                    self.browser.back()
                    time.sleep(1)

    # 解析二级界面信息
    def two_page(self):
        msg_list = self.browser.find_elements_by_xpath('/html/body/main/div[2]/div/div[1]/div[4]/div[2]/div')
        for ml in msg_list:
            info = ml.text.split('\n')
            print(info)

    def main(self):
        self.page_log()
        x = True
        while x:
            self.one_page()
            if self.browser.page_source.find('layui-laypage-next layui-disabled') == -1:
                self.browser.find_element_by_class_name('layui-laypage-next').click()
            else:
                x = False


if __name__ == '__main__':
    spider = SCBSpider()
    spider.main()



