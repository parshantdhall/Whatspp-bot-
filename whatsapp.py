from selenium import webdriver
import time

# Getting All the info
# Enter the name of the user or gurp to send the msg
uname = input("Enter the name of the grup or User to send the message -: \n")
# Message to send
msg = input("Enter the message to send -: \n")
# Count
cnt = input("Count times message to send -: \n")

# Selenium web driver setup and fire up the browser
browser = webdriver.Chrome(
    '/home/parshantdhall/Desktop/song_downloader/chromedriver')

browser.get('https://web.whatsapp.com/')

# Ensure the barcode is scanned
input("Press enter after scanning the barcode")
# Searching into the search box

search_box = browser.find_element_by_xpath(
    f'//input[@title="Search or start new chat"]')
search_box.click()
search_box.send_keys(uname)
# wait
while True:
    print('.....Waiting....')
    time.sleep(1.2)
    print('.....Waiting Complete....')
    break

# Finding the person
# person_to_send_msg = browser.find_element_by_xpath(
#     f'//span[starts-with(@title,{uname})]')
person_to_send_msg = browser.find_element_by_xpath(f'//span[@title="{uname}"]')
person_to_send_msg.click()
# Clicking the input box
input_box = browser.find_element_by_class_name('_13mgZ')
input_box.click()
# Sending the flood of message
for i in range(int(cnt)):
    input_box.send_keys(str(msg))
    browser.find_element_by_xpath(f"//span[@data-icon='send']").click()

print('..................Done.................')
