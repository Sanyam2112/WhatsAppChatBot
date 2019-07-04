import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:\ChromeDriver\chromedriver.exe')
driver.get('https://web.whatsapp.com/')

input("Press enter")

def replymsg(v):
    f = open('info27.txt', 'r')
    fcont = f.read()
    line = fcont.split("\n\n")
    for each in line:
        wordies = each.split(" ")
        for wordy in wordies:
            if (wordy == v):
                msg_box = driver.find_element_by_class_name('_3u328')
                msg_box.send_keys(each)
                msg_box.send_keys(Keys.ENTER)

    f.close()




def InputOutput (unread, recipient):
    names = [recipient]
    for name in names:
        #find = name
        person = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        person.click()

        for i in range(1, 4):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        msg_got = driver.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
        msg = [message.text for message in msg_got]

        for i in range(-unread, 0):
         print(msg[i])
         replymsg(msg[i])

for i in range(1, 15):
    try:
        c = "//*[@id=\"pane-side\"]/div[1]/div/div/div[" + str(i) + "]/div/div/div[2]/div[2]/div[2]/span[1]/div"
        d = driver.find_element_by_xpath(c)
        x = d.text

        try:
            a = "//*[@id=\"pane-side\"]/div[1]/div/div/div[" + str(i) + "]/div/div/div[2]/div[1]/div[1]/span/span"
            b = driver.find_element_by_xpath(a)
            y = b.text
            print(y)
            print(x)
            InputOutput(int(x), y)

        except Exception as e1:
            print("")
            continue

    except Exception as e:
        print("")
        continue

print("chat bot ended")
