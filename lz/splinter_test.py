# -*- coding: UTF-8 -*-
from splinter import Browser

'''
参考文档：https://blog.csdn.net/qq471011042/article/details/79514908
1.解压取出geckodriver.exe（以64x为例）；
2.将geckodriver.exe放到Firefox的安装目录下，如：（D:\火狐\Mozilla Firefox）；
3.将火狐安装目录（D:\火狐\Mozilla Firefox）添加到环境变量path中
4.（最终要的一步）重启pycharm，不要像我一样傻逼的装了好几次火狐就不重启一次pycharm


'''
def main():
    browser = Browser()
    browser.visit("http://www.baidu.com")
    browser.fill('wd','python')
    button = browser.find_by_id('su')
    button.click()
    if browser.is_text_present('splinter.cobrateam.info'):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... We need to improve our SEO techniques")

if __name__ == '__main__':
    main()
