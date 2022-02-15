# Selenium-Web-Scraping

You can access the accompanying presentation [here](https://docs.google.com/presentation/d/1xBq8uvsD3wMb_3jCKFcecXZZ1JzsMyMmDE3DOurjL-w/edit?usp=sharing).

## Prerequisites

### Make sure you have python 3 installed! You can verify this:  

### Do this on your own PC at home, this won't work on Uni PCs:

on Windows, open a new Command Prompt, and type `python`, and if you enter python shell `>>>`, you're good to go.  
on Mac/Linux, open a new Terminal window, and type `python` or `python3`.

### Check if pip is installed:

type `pip -V` in your current shell.

### For Uni PCs, we need a Python Virtual Environment:

Create a folder for your project and navigate to it using your terminal.   
Type `virtualenv --python python3.7 venv`, then type `source venv/bin/activate` to activate your virtual environment.


### Next, we need our modules

To install Selenium, type `pip3 install selenium`, to install Pandas, type `pip3 install pandas`. Note `pip3` should be changed to `pip` on windows.

### Let's grab our Web-Driver

Go to [this link](https://chromedriver.chromium.org/downloads), and download the appropriate driver for your current Chrome version.  
You can find this by navigating to Chrome options (triple dot top right), and selecting Help -> About Google Chrome  
Next, place this in an easily accessible directory like your current working dir (*wink wink*)


## Project Set-Up

Test wether your Selenium installation was successfull by creating a new file named `test.py`.  
Add the default import `import selenium` at the top, and put a simple print statement, like `print("Damn, this worked")`.  
Now you can execute this file by opening a new Command Prompt at your current working dir, and calling `python ./test.py`.  
If your installation failed, it will give you an import error, otherwise you get the one-liner print statement in your console.

### Let's set up the Web-Driver

Selenium should now be installed just fine, so create a new file to work in.  
To make your life easier, add a `DRIVER_PATH` variable for your webdriver, such as `DRIVER_PATH = Service("D:\Selenium_LAB\chromedriver.exe")`.  
The import for this is `from selenium.webdriver.chrome.service import Service`, if you use VSCode, you will likely get import suggestions for Selenium modules.

There are some known bugs with a few current chrome versions, just add `options = webdriver.ChromeOptions()` and `options.add_experimental_option('excludeSwitches', ['enable-logging'])`.  

Next, we need to instantiate our webdriver with the pre-defined options, such as `driver = webdriver.Chrome(service=DRIVER_PATH, options=options)`.  
  
From now on, most actions we call in the script will use this driver variable for context, such as `driver.get()` etc...


### Targeting a site to scrape

You can do this using the `driver.get("https://www.link-to-site.com")` method  

In our example, we use NASDAQ's site to find out about stock values. A large part of web-scraping is getting to understand how the website we're scraping works, we need to visit the site and make some observations. Does this site have a "cookie wall"? Is the site behind CloudFlare? What actions we, as users, would have to take to get the information we need without automation?  

For our site, we can see that there is a cookie wall with an accept button. We need to tell Selenium how to get past this.

Using the Developer Console, we can gather info about the element we need to interact with. The accept button has an ID of "onetrust-accept-btn-handler".  
Select this button from the DOM, and click it with `cookie_accept = driver.find_element(By.ID, "onetrust-accept-btn-handler")` and `cookie_accept.click()`.  
  
Give your project a save, then open your Command Prompt at your current directory.
    
You can now run the scripts with: `python ./name_of_file`

Congrats! You just automated a button click on a website.
    
    
