---
title: Python安裝Oracle
date: 2017-10-18 11:35:42
tags: [python,oracle]
categories: 工作問題
---

安裝oracle并使用 Navicat 鏈接oracle
<!-- more -->
# 安裝oracle客戶端
## 下載及解壓
下載三個安裝包，解壓到E://Oracle/instantclient_12_1中(貌似直接解壓到Oracle就可以了，Oracle目錄需要新建)
instantclient-basic-windows.x64-12.1.0.2.0.zip
instantclient-sdk-windows.x64-12.1.0.2.0.zip
instantclient-sqlplus-windows.x64-12.1.0.2.0.zip
## 添加環境變量及配置文件
選擇在上方目錄基礎下新建E://Oracle/network/admin
### 設置環境變量
新增系統環境變量
NLS_LANG = AMERICAN_AMERICA.ZHS16GBK
TNS_ADMIN = E:\Oracle\network\admin
LD_LIBRARY_PATH = E:\Oracle\instantclient_12_1
SQLPATH = E:\Oracle\instantclient_12_1
追加系統環境變量
Path变量结尾加上E:\Oracle\instantclient_12_1
### 配置文件編寫
在admin 目錄下新建一個 tnsnames.ora 的文件編譯文件,按下方格式添加數據庫連接信息（按格式追加就行）
``` ora
NSD01 =  #連接名
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = 10.132.48.70)(PORT = 1903))  
    )
    (CONNECT_DATA =
      (SERVICE_NAME = nsd01)
    )
  )
```
## python 安裝oracle
windows + R  cmd 直接pip install  cx-Oracle就好了 不會請百度
pip list 查看是否安裝
``` 
C:\Users\Administrator>pip list
cassandra-driver (3.11.0)
certifi (2017.7.27.1)
chardet (3.0.4)
cx-Oracle (6.0.2)
```
測試是否有用cmd 命令下 python 
```
C:\Users\Administrator>python
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (In
tel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import cx_oracle
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'cx_oracle'
>>> import cx_Oracle
>>> db = cx_Oracle.connect('ipcbuuser/ipcbutest@10.142.149.5:1903/SEBUODB')
>>> print (db.version)
>>>
```

## Navicat連接oracle
安裝完成后直接填寫好數據庫信息點擊連接測試,正常情況下應該是連接成功
![Alt text](/images/oracle.PNG)
出現上方問題是應為oci文件不版本不符，根據網上的解決方案是去安裝oracle的文件夾下找到oci文件替換
![Alt text](/images/oracle2.PNG)
然後就出現這個問題，貌似是這個軟件不支持 64位的oracle  oci文件 ，所以要去官網下載一個該版本的32位的 
instantclient-basic-nt-12.1.0.2.0.zip解壓到任意位置將 軟件的oci文件讀取指向該文件夾就好了
![Alt text](/images/oracle3.PNG)

