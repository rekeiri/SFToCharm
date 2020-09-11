from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from salesforce.salesforce_api import SalesForceSession
from config import client_id, client_secret, username, password
import asyncio


#driver = webdriver.Firefox()

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_sf_information())
    print('after running')
    #login()
    #navigate_to_patients()
    #add_member()


async def get_sf_information():
    sf_lib = SalesForceSession(client_id, client_secret, username, password)
    await sf_lib.get_token()
    job_id = await sf_lib.create_job("Account", "insert")
    print(job_id)



    await sf_lib.close_session()


def login():
    driver.get('https://ehr2.charmtracker.com/')

    email = driver.find_element_by_id('login_id')
    email.send_keys('kbuckner@bowtiemedical.com')
    
    next_button = driver.find_element_by_id('nextbtn')
    next_button.click()

    password = driver.find_element_by_id('password')
    password.send_keys('Suzanne11')

    #sometimes it is too fast and doesn't click the next_button. Since they reuse the same button.
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID, 'nextbtn')))
    next_button.click()

def navigate_to_patients():
    #sometimes it lags and takes a long time
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'BowTie Medical')))
    bowtie_link = driver.find_element_by_partial_link_text('BowTie Medical')
    bowtie_link.click()

    #at the current time, this is a div belonging to the patients icon.
    patients_icon = driver.find_element_by_id('MEMBER_TAB_ID_1')
    patients_icon.click()

def add_member():

    add_patients_button = driver.find_element_by_xpath('//div[text() = \'Patient\']')
    add_patients_button.click()

    first_name = driver.find_element_by_id('patient_first_name')
    first_name.send_keys('Eric')

    last_name = driver.find_element_by_id('patient_last_name')
    last_name.send_keys('Fu')

    dob = driver.find_element_by_id('patient_dob')
    dob.send_keys('06111998')

    gender_select = driver.find_element_by_id('patient_gender')
    gender_select.click()
    gender_option = driver.find_element_by_xpath('//option[contains(text(), \'Female\')]')
    gender_option.click()

    '''
    cell = driver.find_element_by_id('patient_mobile')
    cell.click()
    cell.send_keys(Keys.HOME)
    cell.send_keys("4403192041")
    '''
    driver.execute_script("document.getElementById('patient_mobile').value='4403192041'")

    email = driver.find_element_by_id('patient_email')
    email.send_keys('eric.fu@bowtiemedical.com')

    #submit = driver.find_element_by_xpath('//button[contains(text(), \'Add\')]')
    #submit.click()


    

    







if __name__ == '__main__':
    main()