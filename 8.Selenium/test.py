from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os


driver = webdriver.Chrome()


def inspect_element(element):
    print("\n==============================")

    print("Element: ", element)  # Selenium WebElement object

    tag = element.tag_name
    print("Tag: ", tag if tag else "Absent")  # HTML tag name

    element_id = element.get_attribute("id")
    print("ID: ", element_id if element_id else "Absent")  # Element's id

    name = element.get_attribute("name")
    print("Name: ", name if name else "Absent")  # Element's name

    class_name = element.get_attribute("class")
    print("Class: ", class_name if class_name else "Absent")  # Element's class

    text = element.text
    print("Text: ", text if text else "Absent")  # Visible text

    inner_html = element.get_attribute("innerHTML")
    print("Inner HTML: ", inner_html if inner_html else "Absent")  # HTML inside

    outer_html = element.get_attribute("outerHTML")
    print("Outer HTML: ", outer_html if outer_html else "Absent")  # Element + HTML

    print("==============================")


try:
    driver.get("http://localhost:5500/8.Selenium/")

    # print(driver.session_id)

    # select the element
    # login_container = driver.find_element(By.ID , "login-container" )
    # inspect_element(login_container)

    # make the element border red
    # driver.execute_script("arguments[0].style.border='5px solid red';",login_container)
    
    # Part 1: All Element Selection
    print("\nPART 1: ELEMENT SELECTION\n")

    # 1. By ID
    fullname = driver.find_element(By.ID , "fullname")
    inspect_element(fullname)

    # 2. By NAME
    email = driver.find_element(By.NAME , "email")
    inspect_element(email)

    # 3. By CLASS_NAME (first matching element)
    first_input = driver.find_element(By.CLASS_NAME , "form-control")
    inspect_element(first_input)  # this is the fullname field (first with that class)

    # 4. By TAG_NAME (first <input>)
    first_input_tag = driver.find_element(By.TAG_NAME , "input")
    inspect_element(first_input_tag)

    # 5. By LINK_TEXT (exact text of a link)
    forgot_link = driver.find_element(By.LINK_TEXT , "Forgot Password?")
    inspect_element(forgot_link)

    # 6. By PARTIAL_LINK_TEXT (partial match)
    forgot_partial = driver.find_element(By.PARTIAL_LINK_TEXT , "Forgot")
    inspect_element(forgot_partial)  # same link

    # 7. By CSS_SELECTOR
    password = driver.find_element(By.CSS_SELECTOR , "input[type='password']")
    inspect_element(password)

    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit'].btn-primary")
    inspect_element(submit_btn)

    #8. By XPATH
    country = driver.find_element(By.XPATH , "//select[@id='country']")
    inspect_element(country)

    female_radio = driver.find_element(By.XPATH , "//label[contains(text(),'Female')]/input")
    inspect_element(female_radio)

    # 9. Wildcard selections (count only, no printing all)
    all_elements = driver.find_elements(By.CSS_SELECTOR , "*")
    print(f"\nWildcard CSS '*' found {len(all_elements)} elements.")

    all_inputs = driver.find_elements(By.TAG_NAME , "input")
    print(f"Total input fields: {len(all_inputs)}")
    for inp in all_inputs:
        print(f"  type={inp.get_attribute('type') or 'unknown'}, id={inp.get_attribute('id')}")

    # Part 2: Interactions (send_keys)
    print("\nPART 2: INTERACTIONS\n")

    # Fill text fields
    driver.find_element(By.ID , "fullname").send_keys("Sandipan Jha")
    driver.find_element(By.NAME , "email").send_keys("sandipanjha3@gmail.com")
    driver.find_element(By.CSS_SELECTOR , "input[type='password']").send_keys("Secret123!")

    # Number
    driver.find_element(By.ID ,"age").send_keys("20")

    # Phone
    driver.find_element(By.ID,"phone").send_keys("+91 1234567890")

    # URL
    driver.find_element(By.ID , "website").send_keys("www.google.com")

    # Date
    driver.find_element(By.ID , "birthdate").send_keys("2003-01-05")

    # Range slider (using JavaScript)
    slider = driver.find_element(By.ID, "rating")
    driver.execute_script("arguments[0].value = 8",slider) # value
    driver.execute_script("arguments[0].dispatchEvent(new Event('input'));",slider) # ui update

    # Radio – select Male
    driver.find_element(By.CSS_SELECTOR,"input[name='gender'][value='male']").click()

    # Checkboxes – check Coding and Gaming
    driver.find_element(By.CSS_SELECTOR,"input[name='interests'][value='coding']").click()
    driver.find_element(By.CSS_SELECTOR,"input[name='interests'][value='gaming']").click()

    # Single select dropdown
    country_select = Select(driver.find_element(By.ID,"country"))
    country_select.select_by_visible_text("India")

    # Multi-select dropdown
    skills_select = Select(driver.find_element(By.ID , "skills"))
    skills_select.select_by_visible_text("Python")
    skills_select.select_by_visible_text("Go")

    # Textarea
    driver.find_element(By.ID ,"bio").send_keys(
        "Hello I am Sandipan Jha. This text is sent from a program. Lets Go!"
    )

    # File upload – create dummy file
    dummy_file = os.path.abspath("8.Selenium/dummy.txt")
    file_input = driver.find_element(By.ID, "resume")
    file_input.send_keys(dummy_file)

    # Click Reset button to clear the form (just to demonstrate click)
    time.sleep(1)
    reset_btn = driver.find_element(By.ID ,"reset-btn").click()
    print("Reset button clicked – form cleared.")

    # Refill a couple of fields after reset to show it works
    time.sleep(1)
    driver.find_element(By.ID, "fullname").send_keys("Neo")
    driver.find_element(By.NAME, "email").send_keys("neo@matrix.com")

    time.sleep(5)


except Exception as e:
    print("An error occured!")
    print(e)

finally:
    driver.quit()