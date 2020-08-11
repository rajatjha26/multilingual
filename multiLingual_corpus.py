# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import sys
import getopt
import inspect
import pandas as pd
import pyperclip

def PrintLog(message="Here....."):
    callerframerecord = inspect.stack()[1]    # 0 represents this line
                                                # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    # print ("LOG: %s:, %s:, %s:, %s" %(info.filename, info.function, info.lineno, message))

def autoTrans(srcData,outputDS,source,target,translEngine,fileName):
    data=[]
    segData=""
    mainData=""
    out=open(fileName,"w")
    for line in srcData:
        if(re.search(r"\#SEG",line)):
            if(len(segData)+len(mainData)>4500):
                # here the segments are written in data array whose length is less than 5000.
                data.append(mainData)       
                mainData=segData
                segData=""
                continue

            if(mainData==""):
                mainData=segData
            else:
                mainData=mainData+"\n"+segData
            segData=""
        else:
            # print(line)
            if(segData==""):
                segData=line
            else:
                segData=segData+"\n"+line
    data.append(mainData)
    data.append(segData)
    output=[]
    driver = webdriver.Firefox()
    if(translEngine=="gmt"):
        driver.get("https://translate.google.co.in/")
        time.sleep(1)
        driver.find_element_by_xpath('//div[@class="notification-header"]//div[@class="tlid-dismiss-button dismiss-button button"]').click()
        time.sleep(1)
        selectSrc = driver.find_element_by_xpath('//div[@class="sl-wrap"]//div[@class="sl-more tlid-open-source-language-list"]')
        selectSrc.click()
        time.sleep(1)
        if(source=="eng"):
            sour=driver.find_element_by_xpath('//div[@class="language_list_section"]//div[@class="language_list_item_wrapper language_list_item_wrapper-en"]')
            sour.click()
            time.sleep(1)
        else:
            sour=driver.find_element_by_xpath('//div[@class="language_list_section"]//div[@class="language_list_item_wrapper language_list_item_wrapper-hi"]')
            sour.click()
            time.sleep(1)
        
        selectTar = driver.find_element_by_xpath('//div[@class="tl-wrap"]//div[@class="tl-more tlid-open-target-language-list"]')
        selectTar.click()
        time.sleep(1)
        if(target=="eng"):
            out.write("English")
            out.write("\n")
            driver.find_element(By.CSS_SELECTOR, ".language_list_item_wrapper-en:nth-child(23) > .language_list_item").click()
            time.sleep(1)
        elif(target=="hin"):
            out.write("Hindi")
            out.write("\n")
            driver.find_element(By.CSS_SELECTOR, ".language_list_item_wrapper-hi:nth-child(39) > .language_list_item").click()
            time.sleep(1)
        elif(target=="ban"):
            out.write("Bangla")
            out.write("\n")
            driver.find_element(By.CSS_SELECTOR, ".language_list_section:nth-child(2) > .language_list_item_wrapper-bn > .language_list_item").click()
            time.sleep(1)
        elif(target=="tel"):
            out.write("Telugu")
            out.write("\n")
            driver.find_element(By.CSS_SELECTOR, ".language_list_item_wrapper-te:nth-child(97) > .language_list_item").click()
            time.sleep(1)
        elif(target=="tam"):
            out.write("Tamil")
            out.write("\n")
            driver.find_element(By.CSS_SELECTOR, ".language_list_item_wrapper-ta:nth-child(95) > .language_list_item").click()
            time.sleep(1)
        elif(target=="mar"):
            out.write("Marathi")
            out.write("\n")
            driver.find_element(By.CSS_SELECTOR, ".language_list_item_wrapper-mr:nth-child(67)").click()
            time.sleep(1)
        elif(target=="kan"):
            out.write("Kannada")
            out.write("\n")
            driver.find_element(By.CSS_SELECTOR, ".language_list_item_wrapper-kn:nth-child(49)").click()
            time.sleep(1)
        else:
            PrintLog("Please Select a valid Target Language.")
            driver.close()
            sys.exit(1)

        inpBox= driver.find_element(By.ID, "source")
        for data1 in data:
            pyperclip.copy(data1)
            time.sleep(1)
            inpBox.send_keys(Keys.CONTROL, 'v')
            time.sleep(1)
            pyperclip.copy("")
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".tlid-copy-translation-button"))).click()
            time.sleep(1)
            alltext=pyperclip.paste()
            time.sleep(1)
            output.append(alltext)
            pyperclip.copy("")
            time.sleep(1)
            inpBox.clear()
        driver.quit()
    
    elif(translEngine=="bmt"):
        driver.get("https://www.bing.com/translator")
        time.sleep(1)
        inpBox= driver.find_element_by_id("tta_input_ta")
        if(target=="eng"):
            out.write("English")
            out.write("\n")
            select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "tta_tgtsl"))))
            select.select_by_visible_text("English")
        elif(target=="hin"):
            out.write("Hindi")
            out.write("\n")
            select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "tta_tgtsl"))))
            select.select_by_visible_text("Hindi")
        elif(target=="ban"):
            out.write("Bangla")
            out.write("\n")
            select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "tta_tgtsl"))))
            select.select_by_visible_text("Bangla")
        elif(target=="tel"):
            out.write("Telugu")
            out.write("\n")
            select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "tta_tgtsl"))))
            select.select_by_visible_text("Telugu")
        elif(target=="tam"):
            out.write("Tamil")
            out.write("\n")
            select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "tta_tgtsl"))))
            select.select_by_visible_text("Tamil")
        elif(target=="mar"):
            out.write("Marathi")
            out.write("\n")
            select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "tta_tgtsl"))))
            select.select_by_visible_text("Marathi")
        elif(target=="kan"):
            out.write("Kannada")
            out.write("\n")
            select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "tta_tgtsl"))))
            select.select_by_visible_text("Kannada")
        else:
            PrintLog("Please Select a valid Target Language.")
            driver.close()
            sys.exit(1)
        for data1 in data:
            pyperclip.copy(data1)
            time.sleep(1)
            inpBox.send_keys(Keys.CONTROL, 'v')
            time.sleep(2)
            pyperclip.copy("")
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="tta_copyIcon"]').click()
            time.sleep(1)
            alltext=pyperclip.paste()
            time.sleep(1)
            output.append(alltext)
            pyperclip.copy("")
            time.sleep(1)
            inpBox.clear()
        driver.quit()
    elif(translEngine=="wmt"):
        driver.get("https://www.ibm.com/demos/live/watson-language-translator/self-service/home")
    
    else:
        PrintLog("Please Select among gmt,bmt and wmt translation engines.")

    segInd={}
    for paraid in outputDS:
        if(re.search(r"\#SEG",paraid)):
            segInd.update({outputDS.index(paraid):'"'+paraid+'"'})
    i=0
    outData=[]
    for seg in output:
        segLine=seg.split("\n")
        for lines in segLine:
            if(i in segInd.keys()):
                outData.append(segInd[i])
                i=i+1
            outData.append(lines)
            i=i+1
    
    for data in outData:
        out.write(data)
        out.write("\n")

def start():
    inputCsv=""
    source=""
    target=""
    translEngine=""
    try:
        options, remainder = getopt.getopt(sys.argv[1:], 'hi:s:t:m:',['ifile=','source=', 'target=','machTrans=', 'help'])
    except getopt.GetoptError:
        print ('multiLingual_corpus.py -i <inputCsv> -s <sourceLang> -t <targetLang> -m <Translation_Engine> <[gmt,wmt,bmt]>')
        sys.exit(2)
    for opt, arg in options:
        if opt in ('-h', '--help'):
            print("Usage: \
                \n -i --input csv, \
                \n -s, --source lang, \
                \n -t, --target lang, \
                \n -m, --transEngine <[gmt,wmt,bmt]>, \
                \n -h, --help")
            print('command: \
            \n multiLingual_corpus.py -i <inputCsv> -s <sourceLang> -t <targetLang> -m <Translation_Engine> <[gmt,wmt,bmt]>"')
            sys.exit(1)
        elif opt in ('-i', '--ifile'):
            inputCsv = arg
            PrintLog('input file=%s'%arg)
        elif opt in ('-s', '--src'):
            source = arg
            PrintLog('source=%s'%arg)        
        elif opt in ('-t', '--tar'):
            target = arg
            PrintLog('target=%s'%arg)
        elif opt in ('-m', '--tran'):
            translEngine = arg
            PrintLog('NMT=%s'%arg)
    srcName="English" if(source=="eng") else "Hindi"
    df = pd.read_csv (inputCsv,sep="|",index_col=[0],na_filter=False)
    fileName=inputCsv.replace(".csv","")+"_"+source+"2"+target+"_"+translEngine+".txt"
    autoTrans(df[srcName],df.index.tolist(),source,target,translEngine,fileName)

start()