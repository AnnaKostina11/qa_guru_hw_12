import os

from selene import have, command, be

class RegistrationPage:
    def __init__(self, browser):
        self.browser = browser

    def open(self):
         self.browser.open('https://demoqa.com/automation-practice-form')
         self.browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
           have.size_greater_than_or_equal(3)
            )
         self.browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
         return self


    def fill_first_name(self, value):
        self.browser.element("#firstName").type(value)
        return self

    def fill_last_name(self, value):
        self.browser.element("#lastName").type(value)
        return self

    def fill_email(self, value):
        self.browser.element("#userEmail").type(value)
        return self

    def select_gender(self, value):
        gender_options = {
            'Male': '[for="gender-radio-1"]',
            'Female': '[for="gender-radio-2"]',
            'Other': '[for="gender-radio-3"]'
        }
        self.browser.element(gender_options[value]).click()
        return self

    def mobile_number(self, value):
        self.browser.element("#userNumber").type(value)
        return self

    def select_date_of_birth(self, value):
        day, month, year = value.replace(',', ' ').split()

        self.browser.element('#dateOfBirthInput').click()
        self.browser.element('.react-datepicker__month-select').type(month)
        self.browser.element('.react-datepicker__year-select').type(year)
        self.browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subjects(self, value):
        self.browser.element("#subjectsInput").type(value).press_enter()
        return self

    def fill_hobbies(self, hobby_name: str):
        hobby_map = {'Sports': '1', 'Reading': '2', 'Music': '3'}
        if hobby_name not in hobby_map:
            raise ValueError(f"Unknown hobby: {hobby_name}. Use one of: {list(hobby_map.keys())}")

        selector = f'label[for="hobbies-checkbox-{hobby_map[hobby_name]}"]'
        element = self.browser.element(selector)
        element.perform(command.js.scroll_into_view)
        element.perform(command.js.click)
        return self

    def upload_picture(self, file_path):
        self.browser.element("#uploadPicture").set_value(
            os.path.abspath(f"tests/resources/{file_path}"))
        return self

    def fill_address(self, value):
        self.browser.element("#currentAddress").type(value)
        return self

    def select_state(self, value):
        self.browser.element('#state').click()
        self.browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def select_city(self, value):
        self.browser.element('#city').click()
        self.browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def click_submit(self):
        self.browser.element('#submit').click()
        return self

    def should_registered_user_with(self, full_name, email, gender, mobile_number, date_of_birth, subjects, hobbies, upload_picture, address, state_and_city):
        self.browser.element('.table').all('td').even.should(
            have.exact_texts(
            full_name,
            email,
            gender,
            mobile_number,
            date_of_birth,
            subjects,
            hobbies,
            upload_picture,
            address,
            state_and_city
            )
        )
        return self