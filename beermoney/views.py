from cornicesqla.crud import crud
from cornicesqla.views import DBView
from pyramid.view import view_config
from models import Product, DBSession

import json


@crud(path='/products/{id}', collection_path='/products', mapping=Product,
        session=DBSession)
class ProductView(DBView):
    pass
