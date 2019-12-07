#Write a Python program that simulates a system that supports the functions of an e-book reader. You should 
# include methods for users of your system to “buy” new books, view their list of purchased books, and read 
# their purchased books. Your system should use actual books, which have expired copyrights and are available 
# on the Internet, to populate your set of available books for users of your system to “purchase” and read.

import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
