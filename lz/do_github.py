# -*- coding: UTF-8 -*-
#模拟登陆github网站
#登陆地址：https://github.com/login

from splinter import Browser

def main():
    browser = Browser()
    browser.visit("https://github.com/login")
    browser.fill('wd','python')
    button = browser.find_by_name('login')
    button.click()
    if browser.is_text_present('splinter.cobrateam.info'):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... We need to improve our SEO techniques")

if __name__ == '__main__':
    main()