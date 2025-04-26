from selenium.webdriver.common.by import By


class Locators:
    REG_BUTTON = (By.LINK_TEXT, "Зарегистрироваться") #кнопка зарегистрироваться в форме логина
    NAME_FIELD = (By.XPATH, "(//input[@class = 'text input__textfield text_type_main-default'])[1]") #поле имя
    EMAIL_FIELD = (By.XPATH, "(//input[@class = 'text input__textfield text_type_main-default'])[2]") #поле email
    PASSWORD_FIELD = (By.XPATH, "(//input[@class = 'text input__textfield text_type_main-default'])[3]") #поле пароль
    CONTINUE_REG_BUTTON = (By.XPATH, "//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") #кнопка зарегистрироваться в форме регистрации
    INVALID_PASSWORD_MESSAGE = (By.XPATH, "//p[text() = 'Некорректный пароль']") #сообщение о некорректном пароле

    LOGIN_MAIN_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']") #кнопка входа на главной
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']") #кнопка Личный Кабинет
    LOGIN = (By.XPATH, "//button[text()='Войти']")#кнопка войти в форме логина
    LOGIN_BUTTON = (By.LINK_TEXT, "Войти") #кнопка войти в форме регистрации
    REMEMBER_PASSWORD_BUTTON = (By.LINK_TEXT, "Восстановить пароль") #кнопка Восстановить пароль
    EMAIL_INPUT = (By.XPATH, "(//input[@class = 'text input__textfield text_type_main-default'])[1]")#поле ввода email
    PASSWORD_INPUT = (By.XPATH, "(//input[@class = 'text input__textfield text_type_main-default'])[2]")#поле ввода пароля

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") #кнопка конструктор
    LOGO_BUTTON = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']/a") #логотип
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()= 'Выход']") #кнопка выход

    BUNS = (By.XPATH, "//span[contains(text(),'Булки')]") #раздел булки
    SAUCES = (By.XPATH, "//span[contains(text(),'Соусы')]") #раздел соусы
    FILLINGS = (By.XPATH, "//span[contains(text(),'Начинки')]") #раздел начинки