from pages.registration_page import RegistrationPage
import allure

def test_student_registration_form(setup_browser):
    _browser = setup_browser
    registration_page = RegistrationPage(_browser)
    with allure.step("Открываем форму"):
        registration_page.open()

    # WHEN
    with allure.step("Заполняем First Name={first_name}"):
        registration_page.fill_first_name('Anna')
    with allure.step("Заполняем Last Name={last_name}"):
        registration_page.fill_last_name('Kostina')
    with allure.step("Заполняем Email={email}"):
        registration_page.fill_email('111name@example.com')
    with allure.step("Заполняем Gender={gender}"):
        registration_page.select_gender('Female')
    with allure.step("Заполняем Mobile={mobile}"):
        registration_page.mobile_number('8788888888')
    with allure.step("Заполняем Date of Birth={date}"):
        registration_page.select_date_of_birth('18 June 2025')
    with allure.step("Заполняем Subjects={subject}"):
        registration_page.fill_subjects("Computer Science")
    with allure.step("Заполняем Hobbies={hobbies}"):
        registration_page.fill_hobbies('Reading')
    with allure.step("Заполняем Picture={filename}"):
        registration_page.upload_picture('duck.jpg')
    with allure.step("Заполняем Address={address}"):
        registration_page.fill_address('Moscow')
    with allure.step("Выбираем State={state}"):
        registration_page.select_state('Uttar Pradesh')
    with allure.step("Выбираем City={city}"):
        registration_page.select_city('Agra')
    with allure.step("Отправляем форму"):
        registration_page.click_submit()

    # THEN
    with allure.step("Проверяем форму"):
        registration_page.should_registered_user_with('Anna Kostina',
                                               '111name@example.com',
                                               'Female',
                                               '8788888888',
                                               '18 June,2025',
                                               'Computer Science',
                                               'Reading',
                                               'duck.jpg',
                                               'Moscow',
                                               'Uttar Pradesh Agra'
                                               )