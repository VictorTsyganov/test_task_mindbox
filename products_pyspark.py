# В датафреймах (pyspark.sql.DataFrame) заданы продукты, категории и связь между ними.
# Одному продукту может соответствовать много категорий, в одной категории может быть много продуктов.
# Напишите метод с помощью PySpark, который вернет все продукты с
# их категориями (датафрейм с набором всех пар «Имя продукта – Имя категории»).
# В результирующем датафрейме должны также присутствовать продукты, у которых нет категорий.
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

data_products = [
    (1, 'prod_1'),
    (2, 'prod_2'),
    (3, 'prod_3'),
    (4, 'prod_4'),
    (5, 'prod_5'),
    (6, 'prod_6'),
    (7, 'prod_7'),
    (8, 'prod_8'),
    (9, 'prod_9'),
    (10, 'prod_10'),
]

products_columns = ['id', 'prod_name',]

data_categories = [
    (1, 'cat_1'),
    (2, 'cat_2'),
    (3, 'cat_3'),
    (4, 'cat_4'),
    (5, 'cat_5'),
    (6, 'cat_6'),
    (7, 'cat_7'),
    (8, 'cat_8'),
    (9, 'cat_9'),
    (10, 'cat_10'),
]

categories_columns = ['id', 'cat_name',]

products_categories_data = [
    (1, 1),
    (1, 4),
    (1, 5),
    (2, 4),
    (2, 1),
    (2, 3),
    (3, 7),
    (3, 4),
    (9, 4),
    (4, 9),
    (5, 10),
    (6, 10),
    (6, 8),
    (4, 2),
    (1, 7),
    (7, 1),
    (4, 7),
    (1, 8),
    (8, 8),
]

products_categories_columns = ['product_id', 'category_id', ]

products_table = spark.createDataFrame(
    data=data_products, schema=products_columns)

categories_table = spark.createDataFrame(
    data=data_categories, schema=categories_columns)

products_categories_table = spark.createDataFrame(
    data=products_categories_data, schema=products_categories_columns)


result_data = (products_table.join(products_categories_table,
                                   products_table.id == products_categories_table.product_id, 'left')
               .join(categories_table,
                     products_categories_table.category_id == categories_table.id, 'left')
               .select(['prod_name', 'cat_name', ])
               )

result_data.orderBy('product_id', 'category_id', ).show()
