from selenium import webdriver

chrome_path = "D:/Supraja_Work/python/chromedriver.exe" # change path as needed
driver = webdriver.Chrome(chrome_path)

wb = open('companylist.txt')
data = wb.read().split('\n')

companysign = []
companyname = []
revenuedate = []
totalrevenue = []

for i in range(737) :
    url = 'https://www.set.or.th/set/factsheet.do?symbol='+data[i]+'&ssoPageId=3&language=en&country=US'
    driver.get(url)
    ele1 = driver.find_element_by_xpath("""/html/body/table/tbody/tr[3]/td/table[1]/tbody/tr/td[1]""")
    ele2 = driver.find_element_by_xpath("""/html/body/table/tbody/tr[3]/td/table[1]/tbody/tr/td[2]""")
    ele3 = driver.find_element_by_xpath("""/html/body/table/tbody/tr[3]/td/table[2]/tbody/tr[9]/td/table/tbody/tr[1]/td[2]""")
    ele4 = driver.find_element_by_xpath("""/html/body/table/tbody/tr[3]/td/table[2]/tbody/tr[9]/td/table/tbody/tr[4]/td[2]""")
    companysign.append(ele1.text)
    companyname.append(ele2.text)
    revenuedate.append(ele3.text)
    totalrevenue.append(ele4.text)
import pandas as pd
df=pd.DataFrame(companysign,columns=['Companysign'])
df['companyname'] = companyname
df['RevenueDate'] = revenuedate
df['TotalRevenue'] = totalrevenue   

writer = pd.ExcelWriter('thailand_company_info.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='Sheet1')
writer.save()   