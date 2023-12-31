## Описание

Задание 2:
Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам. 

Дополнительно к работоспособности оценим:
* Юнит-тесты
* Легкость добавления других фигур
* Вычисление площади фигуры без знания типа фигуры в compile-time
* Проверку на то, является ли треугольник прямоугольным

Задание 3:
В датафреймах (pyspark.sql.DataFrame) заданы продукты, категории и связь между ними. Одному продукту может соответствовать много категорий, в одной категории может быть много продуктов. Напишите метод с помощью PySpark, который вернет все продукты с их категориями (датафрейм с набором всех пар «Имя продукта – Имя категории»). В результирующем датафрейме должны также присутствовать продукты, у которых нет категорий.

## Как запустить проект локально:

Клонировать репозиторий и перейти в него в командной строке (в папку calculating_figures_area):

``` git@github.com:VictorTsyganov/test_task_mindbox.git ``` 

Задание 2

``` cd test_task_mindbox/calculating_figures_area/ ``` 

Для запуска калькулятора введите команду:

```
python area_calculator.py

```
Для запуска тестов проверки кода калькулятора введите команду:

```
python test_calculator.py

```

Задание 3

Для запуска и проверки задания № 3 необходимо вернуться директорию test_task_mindbox/ и развернуть виртуальное окружение. Для создания виртуального окружения введите команды:

```
python -m venv venv

```
* Если у вас Linux/macOS:
    ``` source venv/bin/activate ``` 

* Если у вас Windows:
    ``` source venv/Scripts/activate ```
    
``` python -m pip install --upgrade pip ``` 

Установить зависимости из файла requirements:

``` pip install -r requirements.txt ```

Для запуска и проверки задания введите команду:

``` spark-submit products_pyspark.py ```
