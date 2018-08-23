# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 17:25:15 2018

@author: lihang
"""

# 动态网站数据爬取

from selenium import webdriver
import pandas as pd

url = "http://www.sse.com.cn/assortment/stock/list/info/profit/index.shtml?COMPANY_CODE=600660"


def parse_Equity_registers(aObj):
    # parse len
    objlen = len(aObj)
    if objlen > 2:
        str1 = [] # 股权登记日
        str2 = [] # 股权登记日总股本(万股)
        str3 = [] # 除息交易日
        str4 = [] # 除息前日收盘价
        str5 = [] # 除息报价
        str6 = [] # 每股红利  含税
        str7 = [] # 每股红利 除税
        for i in range(2,objlen):
            line = aObj[i].text.split("\n")
            str1.append(line[0])
            str2.append(line[1])
            str3.append(line[2])
            str4.append(line[3])     
            str5.append(line[4])
            str6.append(line[5])
            str7.append(line[6])
        Equity_registers = pd.DataFrame({"股权登记日":str1,
                                         "股权登记日总股本(万股)":str2,
                                         "除息交易日":str3,
                                         "除息前日收盘价":str4,
                                         "除息报价":str5,
                                         "每股红利含税":str6,
                                         "每股红利除税":str7},columns = ["股权登记日","股权登记日总股本(万股)","除息交易日","除息前日收盘价","除息报价","每股红利含税","每股红利除税"])
        return Equity_registers
    


obj = webdriver.PhantomJS(executable_path="D:\phantomjs\phantomjs.exe")

try:
    #obj.set_page_load_timeout(5)
    obj.get(url)
    obj.implicitly_wait(10)
    print(obj.title)
    a = obj.find_elements_by_xpath('//*[@id="tableData_one"]/div[2]/table/tbody/tr')
    adf = parse_Equity_registers(a)
    print(adf)
    adf.to_csv("test.csv")
    obj.quit() 
except Exception as e:
    print(e)