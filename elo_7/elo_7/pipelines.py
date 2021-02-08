# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3


class Elo7Pipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.connect = sqlite3.connect('products.db')
        self.cursor = self.connect.cursor()

    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS products""")

        sql = """
			CREATE TABLE products(
				name TEXT,
				price REAL,
				details TEXT,
				category TEXT,
                subcategory TEXT,
				url TEXT UNIQUE
			)
		"""
        self.cursor.execute(sql)

    def db_insert(self, item):
        self.cursor.execute(
            """
			INSERT INTO products(name, price, details, category, subcategory, url)
				VALUES('{}', '{}', '{}', '{}', '{}', '{}')
			""".format(
                item['name'],
                item['price'],
                item['details'],
                item['category'],
                item['subcategory'],
                item['url'],
            )
        )
        self.connect.commit()

    def process_item(self, item, spider):
        self.db_insert(item)
        return item
