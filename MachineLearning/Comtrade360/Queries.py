from SPARQLWrapper import SPARQLWrapper, TURTLE, JSON
from exceptions import TimeOutException, NoResultsException

class Queries:

    '''SparQL konstruktor grafa jer nam on takav format RDF treba za BFS search'''
    def __init__(self, url, resource):
        self.url = url
        self.resource = resource
        self.sparql = SPARQLWrapper(endpoint=None)


    def parent_category_Q(self):
            '''Resurs ima svog nadredjenog i podredjenog, CONSTRUCT pravimo svoj graf od pretrage po parentu(broader predikat) i pretrage po childu(narrower predikat) za odredjeni resurs(objekat). '''
            return f"""
                CONSTRUCT {{ 
                    <http://dbpedia.org/resource/Category:{self.resource}> skos:broader ?parent . 
                    <http://dbpedia.org/resource/Category:{self.resource}> skos:narrower ?child . 
                }}
                WHERE {{ 
                    {{ <http://dbpedia.org/resource/Category:{self.resource}> skos:broader ?parent . }}
                    UNION 
                    {{ ?child skos:broader <http://dbpedia.org/resource/Category:{self.resource}> . }}
                }}
            """
    def dbpedia_uri_validator(self, resource_obj) -> bool:
         
            query = f"""ASK {{
                        VALUES (?r) {{ (dbr:{resource_obj}) }}
                            {{ ?r ?p ?o }}
                            UNION
                            {{ ?s ?r ?o }}
                            UNION
                            {{ ?s ?p ?r }}
                    }}
                     """
            self.sparql.setQuery(query)
            self.sparql.setReturnFormat(JSON)
            self.sparql.setTimeout(20)

            try:
                result = self.sparql.query().convert()
                if result:
                    return True
            except Exception as e:
                raise NoResultsException
            

    async def execute_sparql_query(self,endpoint_url: str, query: str):
        '''SparQL wrapper predstavlja konzolu sa podesenim query-jem, stdout formatom i raw podacima.'''
        self.sparql(endpoint_url)
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(TURTLE)
        self.sparql.setTimeout(360)

        try:
            results = self.sparql.query().convert()
            return results
        except Exception as e:
             raise TimeOutException

        # print("Row resuls", results)
 