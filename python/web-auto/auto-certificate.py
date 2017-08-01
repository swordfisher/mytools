# coding=utf-8

import unittest
from splinter import Browser
import time
import random

chrome = Browser('chrome')
def main():
    global chrome

    # 登录规则引擎
    chrome.visit('xxx')
    time.sleep(1)
    chrome.fill('user', '')
    chrome.fill('passwd', 'xxx')
    # 验证码需要在后台注释,这里才可以运行
    chrome.find_by_xpath('//*[@id="loginForm"]/div/div[4]').first.click()
    chrome.find_by_xpath('//*[@id="loginTypeOpt"]/p[3]').first.click()
    chrome.find_by_id('loginButton').first.click()
    chrome.find_by_xpath('//*[@id="admin-navbar-collapse"]/ul[1]/li[3]').first.click()
    chrome.find_by_xpath('//*[@id="admin-navbar-collapse"]/ul[1]/li[3]/ul/li[1]').first.click()
    chrome.find_by_xpath('/html/body/div/ul[1]/li[2]').first.click()
    chrome.find_by_xpath('//*[@id="s2id_app"]').first.click()
    chrome.find_by_xpath('//*[@id="select2-results-1"]/li[23]').first.click()

    chrome.fill('version', '')
    chrome.fill('pre_version', '')
    chrome.select('type', '')
    chrome.fill('changelog', '\n')
    chrome.fill('pub_person', '')
    #release_time
    chrome.find_by_xpath('/html/body/div[1]/form/div[5]/div').first.click()
    chrome.find_by_xpath('/html/body/div[2]/div[3]/div/button[1]').first.click()
    chrome.attach_file('path', '')
    chrome.find_by_xpath('/html/body/div[1]/form/div[13]/div/input[1]').first.click()

if __name__ == '__main__':
    main()
