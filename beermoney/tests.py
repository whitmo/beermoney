import unittest
import transaction

from pyramid import testing

from .models import DBSession


class TestProductView(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from .models import (
            Base,
            Product,
            )
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            model = Product(name='one',price=55)
            DBSession.add(model)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_it(self):
        from .views import ProductView
        request = testing.DummyRequest()
        info = ProductView(request)
        self.assertEqual(info['one'].name, 'one')
        self.assertEqual(info['project'], 'beermoney')
