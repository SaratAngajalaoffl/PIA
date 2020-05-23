from selenium import webdriver
import sys
import os
import json
import time


def readdata(path):
    with open(path + "\\userdata.json") as f:
        data = json.load(f)
        Username = data["USERNAME"]
        Password = data["PASSWORD"]
    return Username, Password


def init_browser():
    browser = webdriver.Chrome()
    return browser


def login(browser, path):
    Username, Password = readdata(path)
    browser.get("https://github.com/login")
    Username_input = browser.find_element_by_xpath(
        "/html/body/div[3]/main/div/form/div[4]/input[1]")
    Password_input = browser.find_element_by_xpath(
        "/html/body/div[3]/main/div/form/div[4]/input[2]")
    login_button = browser.find_element_by_xpath(
        "/html/body/div[3]/main/div/form/div[4]/input[9]")
    Username_input.click()
    Username_input.send_keys(Username)
    Password_input.click()
    Password_input.send_keys(Password)
    login_button.click()
    return Username


def create_git_repo(Repo_name, path):
    browser = init_browser()
    Username = login(browser, path)
    browser.get("https://github.com/new")
    Repo_name_input = browser.find_element_by_xpath(
        "/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input")
    Repo_name_input.send_keys(sys.argv[1])
    time.sleep(5)
    Confirm_button = browser.find_element_by_xpath(
        "/html/body/div[4]/main/div/form/div[3]/button")
    Confirm_button.click()
    return browser, Username


def set_github(name, path):
    browser, Username = create_git_repo(name, path)
    os.system("git remote add origin " +
              "https://github.com/"+Username+'/'+name+".git")


if __name__ == "__main__":
    set_github(sys.argv[1], sys.argv[2])
