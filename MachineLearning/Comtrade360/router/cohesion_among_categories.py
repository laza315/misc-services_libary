from fastapi import APIRouter, Depends
from typing import Optional
from rdflib import Graph, URIRef
from exceptions import BadInputParsed, NoResultsException
from fastapi_cache.decorator import cache
from Queries import Queries
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache import FastAPICache
from exceptions import MissingInput
from logging import getLogger


logger = getLogger(__name__)


router = APIRouter(
    prefix='/api/v1',
    tags=['resource']
)

_endpoint_url = "https://dbpedia.org/sparql"


cacher = InMemoryBackend()
FastAPICache.init(cacher)



@router.get('/concepts/{resource}', summary='Analysis of words converted to nodes in vector space')
@cache(expire=2000)
async def concept_analizer(resource: str, page: int = 1, page_size: Optional[int] = None):
    if not resource:
        raise MissingInput
    q_instance = Queries(url="http://dbpedia.org/", resource=resource)
    is_uri_valid = q_instance.dbpedia_uri_validator(resource_obj=resource)
    if is_uri_valid:
        logger.info('message from resource module')
        query = q_instance.parent_category_Q()
        result = await Queries.execute_sparql_query(_endpoint_url, query)

        g = Graph()
        g.parse(data=result, format='turtle')

        print("Broj cvorova u grafu:", len(g))
        categories = []
        for obj in g.objects():
            _cut = str(obj).split("/")[-1]
            if "Category:" in _cut:
                obj = _cut.replace("Category:", "")
            categories.append(obj)

        return {'categories': categories}
    else:
        return {'error': "Resource not found on DBPedia!"}

# class Tensor:

#     import io
#     import re
#     import string
#     import tqdm

#     import numpy as np

#     import tensorflow as tf
#     from keras import layers