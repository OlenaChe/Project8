from django.core.management.base import BaseCommand, CommandError
import requests

from sub.models import Category, Product
from sub.constants import CATEGORY_LIST, NUM_PRODUCTS 

class Command(BaseCommand):
    help = 'Insert data in the table Category, Product'

    def handle(self, *arg, **options):
        for cat_name in CATEGORY_LIST:
            p = {"search_terms": cat_name, "json": 1, "page_size": 100}
            r = requests.get("https://fr.openfoodfacts.org/cgi/search.pl",
                             params=p)
            obj, created = Category.objects.update_or_create(name=cat_name)
            i = 0
            for i in range(100):
                if i < NUM_PRODUCTS:
                    product = {"name": "", "description": "", "url": "",
                               "score": "", "category": "", "store": ""}
                    try:
                        if (len(r.json()["products"][i]["product_name_fr"]) > 2
                            and
                            len(r.json()["products"][i]["generic_name_fr"]) > 2
                            and
                            len(r.json()["products"][i]["url"]) > 2
                            and
                            (len(r.json()["products"][i]["nutrition_grade_fr"]) >= 1) 
                            and
                            len(r.json()["products"][i]["stores"]) > 2):
                                name = (r.json()["products"][i]["product_name_fr"])
                                description = r.json()["products"][i]["generic_name_fr"]
                                url = r.json()["products"][i]["url"]
                                store = r.json()['products'][i]['stores']
                                score = (r.json()["products"][i]["nutrition_grade_fr"])
                                img = (r.json()["products"][i]["image_small_url"])
                                obj1, created = Product.objects.update_or_create(name = name, description = description, url = url, store = store, score = score, img = img, category = obj)
                    except (TypeError):
                        pass
                    except (KeyError):
                        pass        
            