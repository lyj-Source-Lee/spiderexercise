这是一个爬取市场部网的程序，采用selenium+Chromedriver技术，
主要获取异业合作里的合作人信息，
由于这个信息要登录且对方同意合作才能进行爬取，
所以由两部分组成。

new_spider.py是登录账号自动向所有合作方发送申请合作。

apply_spider.py是爬取所有已通过申请的合作人信息。
