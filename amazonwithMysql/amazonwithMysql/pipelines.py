# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class AmazonwithmysqlPipeline:
    def __init__(self):
        self.create_connection()
        self.create_database()

    def create_connection(self):
        self.conn = mysql.connector.connect(host='localhost',user='root',password='',database='amazonscapping')
        self.curr = self.conn.cursor()

    def create_database(self):
        self.curr.execute("""DROP TABLE IF EXISTS amazon""")
        self.curr.execute("""create table amazon (
                    name text,
                    author text ,
                    price text,
                    image text
                    )""")
    def store_db(self,item):
        self.curr.execute("""insert into amazon values (%s,%s,%s,%s)""", (
            item['product_name'][0], item['product_author'][0], item['product_price'][0], item['product_imageLink'][0]
        ))
        self.conn.commit()
    def process_item(self, item, spider):
        self.store_db(item)
        return item
