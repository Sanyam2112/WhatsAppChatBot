import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:\ChromeDriver\chromedriver.exe')
driver.get('https://web.whatsapp.com/')

input("Press enter")

def replymsg(v):
    v.lower()
    if "schemes" in v:
        reply = "These are the following schemes available"
    elif "card" in v:
        reply = "Do you want to make a card"
    elif "hello" in v:
        reply = "Hey, how can i help you"
    elif "yes" in v:
        reply = "Okay here's the link to make your new Kissan card"
    elif "crop" in v:
        reply = "Here's information about crops"
    elif "quit" in v:
        reply = "Thank you for using the chatbot"
    else:
        reply = "I'm sorry, I do not understand"

    msg_box = driver.find_element_by_class_name('_3u328')
    msg_box.send_keys(reply)
    msg_box.send_keys(Keys.ENTER)

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

def loop():
    count = 0
    for i in range(1, 16):
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
                time.sleep(2)

            except Exception as e1:
                print('error')
                continue
        except Exception as e:
            print('error')
            count = count + 1
            continue
    return count

for a in range(100):
    if loop() == 15:
        driver.refresh()
        time.sleep(15)

print("chat bot ended")