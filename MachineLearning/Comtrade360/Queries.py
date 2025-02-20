from SPARQLWrapper import SPARQLWrapper, TURTLE, JSON
from exceptions import NoResultsException
import asyncio
import time

class Queries:

    '''SparQL konstruktor grafa jer nam on takav format RDF treba za BFS search'''
    def __init__(self, url, resource):
        self.url = url
        self.resource = resource
        self.sparql = SPARQLWrapper(endpoint=None)
    
    def document_scrapper(self):
        '''Svaki Resurs ima odredjeni entitet u vidu dokumenta koji mozemo scrape-ovati kako bismo dobili opsirni text o objektu za dublju vektorsku analizu'''
        return f"""SELECT ?object WHERE {{ 
                    dbr:{self.resource} dbo:abstract ?object .
                    FILTER (lang(?object) = "en")
                    }}
                """


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
                    VALUES (?r) {{ (<http://dbpedia.org/resource/{resource_obj}>) }}
                        {{ ?r ?p ?o }}
                        UNION
                        {{ ?s ?r ?o }}
                        
                }}
                """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        self.sparql.setTimeout(20)

        for i in range(3):  # Pokušaj do 3 puta
            try:
                result = self.sparql.query().convert()
                print(f"SPARQL result for {resource_obj}: {result}")
                if result.get('boolean') is True:
                    return True
                return False
            except Exception as e:
                print(f"SPARQL error on attempt {i+1} for {resource_obj}: {e}")
                time.sleep(2)  # Sačekaj 2 sekunde i probaj opet
        
        raise NoResultsException

            

    async def execute_sparql_query(self, endpoint_url: str, query: str, format : SPARQLWrapper):
        '''Izvršava asinhroni SPARQL upit.'''
        self.sparql.endpoint = endpoint_url
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(format)

        loop = asyncio.get_event_loop()  
        try:
            results = await loop.run_in_executor(None, self.sparql.query().convert)  
            return results
        except Exception as e:
            raise  {str(e)}

 