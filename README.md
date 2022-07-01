# stepik_test_final_project
**Eng**.

Repository for the final project for the Stepik course "**Test Automation with Selenium and Python**".

**For the work were used**:
* Linux OS
* Python 3.10.5
* Google Chrome 103.0.5060.53
* Firefox 102.0

**Additional in the code**:
* So that when adding a product to basket tests can handle links with and without "?promo=": In the "ProductPage" class, in the "add_product_button_click" function, added a check for the presence of "?promo=" in the address. If "?promo=" is present, the "solve_quiz_and_get_code" function from the base class is started.
* Changed code for setting options in Firefox in the file "conftest.py". Since the new version of Selenium, using obsolete methods (which are given as an example in the course lessons) leads to a warning about the need to use new methods.  

        from selenium.webdriver.firefox.options import Options # for new selenium version
        options = Options() # for new selenium version
        options.set_preference('intl.accept_languages', user_language) # for new selenium version
        browser = webdriver.Firefox(options=options) # for new selenium version


**Рус**.

Хранилище для итогового проекта по курсу Stepik "**Автоматизация тестирования с помощью Selenium и Python**".

**Для работы использовались**:
* ОС Linux
* Python 3.10.5
* Google Chrome 103.0.5060.53
* Firefox 102.0

**Дополнительное в коде**:
* Чтобы при добавлении продукта в корзину, тесты могли работать с сылками с "?promo=" и без: в классе "ProductPage", в функции "add_product_button_click", добавлена проверка на наличие "?promo=" в адрессе. Если "?promo=" присутствует, то запускается функция "solve_quiz_and_get_code" из базового класса.
* Изменен код для установки опций в Firefox в файле "conftest.py". Так как в новой версии Selenium, использование устаревших методах (которые приведены в пример в уроках курса) приводит к появлению предупреждения о необходимости использовать новые методы.  

        from selenium.webdriver.firefox.options import Options # for new selenium version
        options = Options() # for new selenium version
        options.set_preference('intl.accept_languages', user_language) # for new selenium version
        browser = webdriver.Firefox(options=options) # for new selenium version
