# stepik-test-final-project
**Eng**.

Repository for the final project for the Stepik course "**Test Automation with Selenium and Python**".

**For the work were used**:
* Linux OS
* Python 3.10.5
* Google Chrome 103.0.5060.53

**Additional in the code**:
So that when adding a product to basket tests can handle links with and without "?promo=":
In the "ProductPage" class, in the "add_product_button_click" function,
added a check for the presence of "?promo=" in the address. If "?promo=" is present, 
the "solve_quiz_and_get_code" function from the base class is started.

**Рус**.

Хранилище для итогового проекта по курсу Stepik "**Автоматизация тестирования с помощью Selenium и Python**".

**Для работы использовались**:
* ОС Linux
* Python 3.10.5
* Google Chrome 103.0.5060.53

**Дополнительное в коде**:
Чтобы при добавлении продукта в корзину, тесты могли работать с сылками с "?promo=" и без:
в классе "ProductPage", в функции "add_product_button_click",
добавлена проверка на наличие "?promo=" в адрессе. Если "?promo=" присутствует, 
то запускается функция "solve_quiz_and_get_code" из базового класса.
