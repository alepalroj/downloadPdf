#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: alepalroj
@file: downloadPdf.py
@time: 11/03/22 10:30 PM
"""

import argparse

DOWNLOAD_FOLDER_ARGUMENT_NAME = 'downloadPath'
SELENIUM_DRIVER_FOLDER_ARGUMENT_NAME = 'driverPath'
URL_ARGUMENT_NAME = 'url'
KEYWORD_ARGUMENT_NAME = 'keyword'
DOWNLOAD_ARGUMENT_NAME = '--down'
CONVERT_ARGUMENT_ACTION = 'store_true'

PROCESS_DESCRIPTION = 'Process of downloading pdf files with Selenium searching for keywords in the link.'
DOWNLOAD_FOLDER_ARGUMENT_HELP_DESCRIPTION = 'a download folder name where the pdf files will be stored'
DRIVER_FOLDER_ARGUMENT_HELP_DESCRIPTION = 'a folder name where the selenium driver will be stored'
PDF_URL_ARGUMENT_HELP_DESCRIPTION = 'an url where the document is hosted'
KEYWORD_ARGUMENT_HELP_DESCRIPTION = 'a keyword present in the pdf download link'
DOWNLOAD_ARGUMENT_HELP_DESCRIPTION = 'download pdf document from a keyword in the download link'

def download_pdf_with_keyword_from_link(downloadPath, driverPath, url, keyword):
    from selenium import webdriver
    firefoxProfile = webdriver.FirefoxProfile()
    firefoxProfile.set_preference("browser.download.panel.shown", False)
    firefoxProfile.set_preference("browser.helperApps.neverAsk.openFile","application/pdf")
    firefoxProfile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    firefoxProfile.set_preference("browser.download.manager.showWhenStarting", False)
    firefoxProfile.set_preference("browser.download.manager.alertOnEXEOpen", False)
    firefoxProfile.set_preference("browser.download.manager.focusWhenStarting", False)
    firefoxProfile.set_preference("browser.download.folderList", 2)
    firefoxProfile.set_preference("browser.download.useDownloadDir", True)
    firefoxProfile.set_preference("browser.helperApps.alwaysAsk.force", False)
    firefoxProfile.set_preference("browser.download.manager.alertOnEXEOpen", False)
    firefoxProfile.set_preference("browser.download.manager.closeWhenDone", True)
    firefoxProfile.set_preference("browser.download.manager.showAlertOnComplete", False)
    firefoxProfile.set_preference("browser.download.manager.useWindow", False)
    firefoxProfile.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False)
    firefoxProfile.set_preference("pdfjs.disabled", True)
    firefoxProfile.set_preference("browser.download.dir", downloadPath)
    driver = webdriver.Firefox(firefox_profile=firefoxProfile,executable_path=driverPath)
    driver.get(url)
    link = driver.find_element_by_xpath("(//a[contains(text(),"+keyword+")])")
    link.click()
    driver.refresh()
    driver.close()

parser = argparse.ArgumentParser(description=PROCESS_DESCRIPTION)
parser.add_argument(DOWNLOAD_FOLDER_ARGUMENT_NAME, type=str, help=DOWNLOAD_FOLDER_ARGUMENT_HELP_DESCRIPTION)
parser.add_argument(SELENIUM_DRIVER_FOLDER_ARGUMENT_NAME, type=str, help=DRIVER_FOLDER_ARGUMENT_HELP_DESCRIPTION)
parser.add_argument(URL_ARGUMENT_NAME, type=str, help=PDF_URL_ARGUMENT_HELP_DESCRIPTION)
parser.add_argument(KEYWORD_ARGUMENT_NAME, type=str, help=PDF_URL_ARGUMENT_HELP_DESCRIPTION)
parser.add_argument(DOWNLOAD_ARGUMENT_NAME, action=CONVERT_ARGUMENT_ACTION , help=DOWNLOAD_ARGUMENT_HELP_DESCRIPTION)

args = parser.parse_args()

if args.down:        
        download_pdf_with_keyword_from_link(args.downloadPath, args.driverPath, args.url, args.keyword)
