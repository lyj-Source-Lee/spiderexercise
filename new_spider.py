from selenium import webdriver
import time

class SCBSpider(object):
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.url = 'http://www.shichangbu.com'
        self.msg = '期待与您的合作'
        self.i = 1

    # 登录
    def page_log(self):
        self.browser.get(self.url)
        # 点击登录
        self.browser.find_element_by_xpath('/html/body/header/div[1]/div/div/div[2]/div/div/div/a[2]').click()
        # 用户名
        input = self.browser.find_element_by_id('lgp_mobile')
        input.send_keys('用户名')
        # 密码
        input = self.browser.find_element_by_id('lgp_password')
        input.send_keys('密码')
        # 登录按钮
        self.browser.find_element_by_xpath('//*[@id="lgp_btn_login"]').click()
        time.sleep(2)
        # 异业合作
        self.browser.find_element_by_xpath('/html/body/header/div[2]/div/div/menu/ul/li[4]/a').click()
        time.sleep(2)

    # 发送申请
    def send_msg(self):
        count = 0
        for i in range(15):
            if count == 0 or self.i == 1:
                xp = '//*[@id="company_list_data"]/li[{}]/a/div/div[2]/div[1]'.format(i+1)
                self.browser.find_element_by_xpath(xp).click()
                time.sleep(2)
                # 点击申请按钮
                self.browser.find_element_by_xpath('//*[@id="btnApply"]').click()
                time.sleep(0.5)
                # 填入申请信息
                self.browser.find_element_by_xpath('//*[@id="applyTextarea"]').send_keys(self.msg)
                time.sleep(0.5)
                # 点击申请
                self.browser.find_element_by_xpath('//*[@id="btn_ok"]').click()
                time.sleep(1)
                # 返回上一页
                self.browser.back()
                time.sleep(2)
                count += 1
            else:
                for nu in range(self.i):
                    self.browser.find_element_by_class_name('layui-laypage-next').click()
                    time.sleep(1)
                xp = '//*[@id="company_list_data"]/li[{}]/a/div/div[2]/div[1]'.format(i + 1)
                self.browser.find_element_by_xpath(xp).click()
                time.sleep(2)
                # 点击申请按钮
                self.browser.find_element_by_xpath('//*[@id="btnApply"]').click()
                time.sleep(0.5)
                # 填入申请信息
                self.browser.find_element_by_xpath('//*[@id="applyTextarea"]').send_keys(self.msg)
                time.sleep(0.5)
                # 点击申请
                self.browser.find_element_by_xpath('//*[@id="btn_ok"]').click()
                time.sleep(1)
                # 返回上一页
                self.browser.back()
                time.sleep(2)


    def main(self):
        self.page_log()
        x = True
        while x:
            self.send_msg()
            if self.browser.page_source.find('layui-laypage-next layui-disabled') == -1:
                self.browser.find_element_by_class_name('layui-laypage-next').click()
                self.i += 1
            else:
                x = False


if __name__ == '__main__':
    spider = SCBSpider()
    spider.main()














