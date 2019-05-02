from selenium import webdriver
from pages.pages.pageObject import Home

def before_all(context):
	context.driver=webdriver.Remote('http://zalenium:4444/wd/hub')
	context.home_page=Home(context.driver)

def before_feature(context,feature):
	pass

def before_scenario(context,scenario):
	pass

def before_tag(context,tag):
	pass

def after_tag(context,tag):
	pass

def before_step(context,step):
	pass

def after_step(context,step):
	pass

def after_scenario(context,scenario):
	pass

def after_feature(context,feature):
	pass

def after_all(context):
	context.driver.quit()

