from selenium import webdriver
import time
import os
import ping3
from selenium.webdriver.common.by import By

fw_path = os.path.abspath("C:\MR50\Firmware.bin")
conf_path = os.path.abspath("C:\MR50\Config.bin")

def main():

    validarPing = ping3.ping('192.168.1.1')
    while validarPing == None:
        validarPing = ping3.ping('192.168.1.1')
        print(validarPing)
        time.sleep(1)
        continue

    driver = webdriver.Chrome()
    driver.get("http://192.168.1.1")
    driver.implicitly_wait(10)

    # Faz o login na pagina, roteador deve estar resetado
    element = driver.find_elements(By.TAG_NAME, "input")
    if len(element) > 3:
        element[0].send_keys("alfa1627")
        element[2].send_keys("alfa1627")
    else:
        element[0].send_keys("alfa1627")
        # element[2].send_keys("alfa1627")
    button = driver.find_element(By.TAG_NAME, "a")
    button.click()
    time.sleep(2)

    driver.get("http://192.168.1.1/#firmware")
    time.sleep(1)
    uploadConf = driver.find_element(By.ID, "manual-upgrade-file").find_element(By.TAG_NAME, "input")
    uploadConf.send_keys(fw_path)
    buttonUpgrade = driver.find_element(By.ID, "local-upgrade-btn").find_element(By.TAG_NAME, "a").click()
    confirmButton = driver.find_element(By.ID, "firmware-upgrade-msg-btn-ok").find_element(By.TAG_NAME, "a").click()

    while validarPing != None:
        print(validarPing)
        validarPing = ping3.ping('192.168.1.1')
        time.sleep(0.5)
        continue
    driver.close()

    while validarPing == None:
        validarPing = ping3.ping('192.168.1.1')
        print(validarPing)
        time.sleep(0.5)
        continue


    pings = [];
    while len(pings) <= 3:
        validarPing = ping3.ping('192.168.1.1')
        if validarPing != None:
            pings.append(str(validarPing))
        time.sleep(1)
        print(pings)
        continue

    driver = webdriver.Chrome()
    driver.get("http://192.168.1.1")
    driver.implicitly_wait(10)
    element = driver.find_elements(By.TAG_NAME, "input")
    element[0].send_keys("alfa1627")
    button = driver.find_element(By.TAG_NAME, "a")
    button.click()
    time.sleep(1)

    driver.get("http://192.168.1.1/#backupRestore")
    uploadConf = driver.find_element(By.ID, "restore-file").find_element(By.TAG_NAME, "input")
    uploadConf.send_keys(conf_path)
    buttonUpgrade = driver.find_element(By.ID, "restore-button").find_element(By.TAG_NAME, "a").click()
    confirmButton = driver.find_element(By.ID, "restore-confirm-msg-btn-ok").find_element(By.TAG_NAME, "a").click()

    while validarPing != None:
        print(validarPing)
        validarPing = ping3.ping('192.168.1.1')
        time.sleep(1)
        continue
    driver.close()
    print("Finalizado com sucesso")

main()


