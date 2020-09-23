import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait 
#import org.openqa.selenium.chrome.ChromeDriver;  
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import argparse
import html
import itertools
import re
import sys
import time
 

class MyMain() :  
   
        
    def main_func(self,keyword,prop) :

        item = keyword

        try :
            #items = ["s-300","s-350","s-400","s-500","HQ-9","HQ-16","Pantsir-S1","Grizzly","Howk","Buk","Tor","FD2000","Tunguska","Gaskin"]
            #headers = []
            baseUrl = "https://www.janes.com/"

            #soup = BeautifulSoup(driver.page_source, 'lxml')
            #soup = BeautifulSoup(html.text)
            options = webdriver.ChromeOptions() 
            options.add_argument("start-maximized")
            options.add_argument('disable-infobars')
            options.add_argument('--ignore-ssl-errors=yes')
            options.add_argument('--ignore-certificate-errors')
            options.add_experimental_option("excludeSwitches", ['enable-logging'])
            driver = webdriver.Chrome(chrome_options=options,executable_path= r"C:\Users\hilal.eto\Desktop\chromedriver.exe")
            #driver = webdriver.Chrome(executable_path= r"C:\Users\hilal.eto\Desktop\chromedriver.exe") 
            driver.get(baseUrl)
            driver.implicitly_wait(10)
            main_window = driver.current_window_handle #saving main window
            
            
        except :
                print("Chrome Driver error")

        myclass.login(driver,item,prop)
##################################################################################################################################
# start to scrape 

    def login(self,driver,item,prop) :
        try :
            print("hi im here !")  
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar-1"]/ul/li[7]/a'))).click()  
            #login_btn = driver.find_element_by_xpath('//*[@id="navbar-1"]/ul/li[7]/a').click()  
            time.sleep(5)
            myclass.search(driver,item,prop)
            
        except NoSuchElementException:
            #driver.get("https://customer.janes.com/janes/home")
            print("couldn't found login button")

        

    # def signin(self,driver) :
    #   try :
    #        myclass.search(driver,item)
    #    except NoSuchElementException :
    #       WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="customerLoginForm"]/div[4]/div/p[2]/small/a'))).click()
    #       time.sleep(5)    


    def search(self,driver,item,prop) :

            print("ok now here")
            search_item = item
            print(search_item)
            key_item = "[title("+search_item+")]"
            print(key_item)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="banner-search-bar"]/div[1]/span/button')))
            entry = driver.find_element_by_xpath('//*[@id="siteSearch"]')
            entry.send_keys(Keys.CONTROL,"a") #clear the box
            entry.send_keys(key_item)  #searching keyword from titles
            entry.send_keys(Keys.RETURN)
            #enter item in entrybox 
            #time.sleep(3)
            #search_btn = driver.find_element_by_xpath('//*[@id="banner-search-bar"]/div[1]/span/button').click() #search it
            time.sleep(5)
            #myclass.filter_results(driver)
            #myclass.get_link(driver)
            print("im done searching")
            myclass.filter_results(driver)
            myclass.get_link(driver,prop)
            if  driver.find_elements_by_class_name("noResultsCtrl") :  
                #if element is not found,resu#look for the element that is present when there are no resultslts are exist
                print("There's nothing here ! ")
    
                    
                
    def get_link(self,driver,prop) : 

        #while(True) : #if there is next page 
                
        print("hi")
        time.sleep(5)
        all_links = driver.find_elements_by_css_selector("a[href*='/Janes/Display/']")

        flag =0

        for link in all_links :  
            #scroll()
            print("hey")
            driver.execute_script("arguments[0].click();", link)
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(10)
            myclass.get_info(driver,prop) 
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            flag=flag+1

        #if flag !=0 and flag%6==0 :   #in  the end of the screen,it scrolled

            #if flag !=0 and flag%30 == 0 :  #in  the end of the screen,go to next page 

                #if driver.find_element_by_class("paginate_button next") :
                    #driver.find_element_by_class("paginate_button next").click() #go to next page
                    #all_links.clear()   #clear the link list for the next page
                    #time.sleep(5) 

            #else :

                #scroll(driver)



    def get_info(self,driver,prop) :

        soup = BeautifulSoup(driver.page_source, 'lxml')
        

        try :    
            #in case there is no table in link 
            tables = driver.find_elements_by_xpath("//table")
            #tables = soup.findChildren('table')
                
        except NoSuchElementException :
            print("No tables found in link !")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(5)  
            #closes new tab and swtich to the first tab

        data_list = {} #this is a nested dictionary object

            # eg list 
            # {
            # "length" : {"s50gk" : "12", "s460" : "20"}
            # "width" : {"360y" : "12", "300n" : "20"}
            # }
        temp = {}
        for pro in prop :
            head_text = []
            
                   
            for table in tables:

                    #row_found = driver.find_element_by_xpath('//div[@class="table table-bordered"]//table//tr[td[last()][text()="%s"]]/td[1]/a' % prop)
                        
                #HEADER SIDE
                        
               
                if  driver.find_elements_by_xpath("//th") :  
                    #if header exists 

                    head = driver.find_elements_by_xpath("//*[@id='mainContent']/div/div/div/table/thead/tr") 
                    #it takes all header columns to the list
                    print(head)        
                    if driver.find_elements_by_class_name("inlineLinkContainer"): 
                        #if header is clickable 

                        headers = list(set(head)) 
                        #removes duplicates from list
                        print(headers)
                        
                    
                    elif "(" in head :  
                        #remove regular expressions
                                
                        if("(A)" in head) :
                            lis = [s.strip() for s in head.split("(A)")]
                        if("(B)" in head) :
                            lis = [s.strip() for s in head.split("(B)")]
                        if("(C)" in head) :
                            lis = [s.strip() for s in head.split("(C)")]

                        head_text.append(lis)
                        print(head_text)

                                
                    

                    elif "," in head :
                            temp = head.split(",")
                            head_text.append(lis)
                            print(head_text)

                                
                        
                    elif "/" in head :
                            temp_data = head.split("/")
                            head_text.append(lis)
                            print(head_text)


                    elif driver.find_element_by_xpath("//td[contains(text(),'Variant')]/input") : 
                        row = driver.find_elements_by_xpath("//*[@id='mainContent']/div[10]/div[3]/div/div/table/tbody/tr[1]/td")
                        for col in row :
                                head_text.append(col.text)
                        print(head_text)
                            

                    elif driver.find_elements_by_class("sr-only") :

                        if(driver.find_element_by_class("sr-only").text == "Specifications") :
                            #dont get the value if td is "specifications" 
                            head_text.append(pro)
                            print(head_text)

                        else :
                            head_text.append(pro)
                            print(head_text)
                else :
                    head_text.append(prop)
                    print(head_text)


                #for key in head_text:
                    #tree_dict = {key: tree_dict} 

                #VALUE SIDE 
                

                if driver.find_elements_by_xpath("//td[text()="+pro+"]") :
                    # if the property exists in table
                    prop_found = driver.find_elements_by_xpath("//div[@class='table table-bordered']//[contains(text(),'%s')]" % pro)
                    next_element = prop_found.find_elements_by_xpath('./following-sibling::td') 
                    #get next element that shows value of the prop
                        
                    while not next_element.text : 
                         # in case sibling cell is empty
                        next_element = next_element.find_elements_by_xpath('./following-sibling::td')

                    while not  "overall" in next_element.text  : 
                        #in case sibling cell contains "overall" text
                        next_element = next_element.find_elements_by_xpath('./following-sibling::td')
                        

                    val_list=[]
                    for i in next_element :  
                        #find the cell that is not empty
                        

                        myVal = next_element[i]
                        k = 0
                        if "(A)" in myVal :
                            value = myVal.split("(A)") 
                            val_list.append(value[k])
                            k = k + 1

                        if "(B)" in myVal :
                            value = myVal.split("(B)")
                            val_list.append(value[k])
                            k = k + 1 

                        if "(A/B)" in myVal :
                            value = myVal.split("(A/B)")
                            val_list.append(value[k])
                            k = k + 1

                        if "(C)" in myVal :    
                            value = myVal.split("(C)")
                            val_list.append(value[k])
                            k = k + 1

                        if "(A/C)" in myVal :
                            value = myVal.split("(A/C)")
                            val_list.append(value[k])
                            k = k + 1

                        if "(B/C)" in myVal :
                            value = myVal.split("(B/C)")                                        
                            val_list.append(value[k])
                            k = k + 1
                        
                        

                        if "(1)" in myVal :
                            value_A = myVal.split("(1)")
                            val_list.append(value_A[0])

                        if "(2)" in myVal :
                            value_A = myVal.split("(2)")
                            val_list.append(value_A[1])

                        elif "," in myVal :
                            value_A = myVal.split(",")
                            val_list.append(value_A)



                #for val in val_list :
                    #temp_dict ={key : prop , value : val}

                #for head in head_text :

                #    head_dict = {key : head_text , value : temp_dict}

                #add_dict = dict(zip(head_text,temp_dict))  

                #dict_prop = dict()
                #for line in list:
                    #if line[0] in dict_prop:
                     # append the new number to the existing array at this slot
                        #dict_prop[line[0]].append(line[1])
                    #else: # create a new array in this slot
                        #dict_prop[line[0]] = [line[1]]
                         

            # all prop all headers in one table all values for 1 prop in one table found 

            #temp = dict(zip(head_text)
            #tmp = dict(zip(prop,val))
            #data_list.update(temp)
                                     
        print("searching for ", pro ,"is finished !")
        #return data_list
        

    def scroll(self,driver, timeout):
        
        scroll_pause_time = timeout

    # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
        # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page 
            time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height :
            # If heights are the same it will exit the function
                break
            last_height = new_height
            

    def filter_results(self,driver) : #news document type will be filtered
        scr1 = driver.find_element_by_xpath('//*[@id="left-panel"]')
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
        time.sleep(2)

        doc_type = driver.find_element_by_xpath('//*[@id="myTabContent"]/div/div[5]/div[2]/h5/button[1]').click()
        panel = driver.find_elements_by_xpath('//*[@id="myTabContent"]/div/div[5]/div[2]/ul')
        #checkboxes = driver.find_elements_by_xpath("//input[@name='DOCUMENTTYPESTAXONOMY[]']")

        #for checkbox in checkboxes:
                #if not checkbox.get_attribute('value') == "News" :#filter all document types except "News"
                    #checkbox.click()
        profile = driver.find_element_by_xpath('//*[@id="myTabContent"]/div/div[5]/div[2]/ul/li[2]/label').click()
        analysis = driver.find_element_by_xpath('//*[@id="myTabContent"]/div/div[5]/div[2]/ul/li[3]/label').click()
        print("i am filtering")

        apply = driver.find_element_by_xpath('//*[@id="btnApplyFacets"]')
        #driver.execute_script('document.getElementById("left-panel").scrollTop += 100')
        driver.execute_script("arguments[0].scrollIntoView(true);", apply)
        apply.click()
        #driver.execute_script("scrollBy(0,-200);",scr1)
        time.sleep(2)
      
        

    def to_json(self,df) :

        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = timestr + self.item
        df.to_json(r"C:\Users\hilal.eto\Desktop\" +%s+ ",filename)

        


myclass = MyMain()