import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:\ChromeDriver\chromedriver.exe')
driver.get('https://web.whatsapp.com/')





e = " "
input("Press enter")
while(e != "end"):
    #input("Press enter")
    #time.sleep(5)

    names = ["Kenan Pcce"]
    for name in names:
        find = name
        person = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        person.click()


        for i in range(1, 4):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

        msg_got = driver.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")

        msg = [message.text for message in msg_got]

        print(msg[-1])

    # if msg[-1] == "Tell me the schemes available":
    # reply = "These are the following schemes available "

    v = msg[-1]

    reply = " "

    if "schemes" in v:
        reply = "These are the following schemes available "
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
        e = "end"
    else:
        reply = "I'm sorry, I do not understand, try another message or message quit if you are done"


    msg_box = driver.find_element_by_class_name('_3u328')
    msg_box.send_keys(reply)
    msg_box.send_keys(Keys.ENTER)
    time.sleep(10)

print("chat bot ended")
