from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")  # Ссылка «Личный кабинет» в шапке
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")  # Ссылка «Конструктор» в шапке
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")  # Логотип Stellar Burgers
    MAKE_BURGER_HEADING = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок «Соберите бургер»
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка «Оформить заказ» (видна после входа)

    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")  # Вкладка «Булки»
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")  # Вкладка «Соусы»
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")  # Вкладка «Начинки»
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")  # Активная вкладка конструктора
    ACTIVE_TAB_CLASS = "tab_tab_type_current"  # Часть класса активной вкладки


class LoginPageLocators:
    HEADING = (By.XPATH, "//h2[text()='Вход']")  # Заголовок «Вход»
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле Email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле «Пароль»
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка «Войти»
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Ссылка «Зарегистрироваться»
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # Ссылка «Восстановить пароль»


class RegistrationPageLocators:
    HEADING = (By.XPATH, "//h2[text()='Регистрация']")  # Заголовок «Регистрация»
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле «Имя»
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле Email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле «Пароль»
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка «Зарегистрироваться»
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка «Войти» в форме регистрации
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")  # Ошибка «Некорректный пароль»


class ForgotPasswordPageLocators:
    HEADING = (By.XPATH, "//h2[text()='Восстановление пароля']")  # Заголовок «Восстановление пароля»
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка «Войти» в форме восстановления пароля


class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")  # Вкладка «Профиль» в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка «Выход»
