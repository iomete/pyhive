import unittest
from sqlalchemy import create_engine


class TestHiveHttp(unittest.TestCase):
    def test_create_connection(self):
        engine = create_engine('hive://admin:Admin_123@localhost:10000/ios?auth=CUSTOM;transport_mode=http')
        print(engine.execute("show databases").fetchall())
