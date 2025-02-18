from fastapi import APIRouter, Depends
from typing import Optional
from SPARQLWrapper import SPARQLWrapper, TURTLE
from rdflib import Graph, URIRef
from exceptions import BadInputParsed, NoResultsException
import queue
from typing import List
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')


router = APIRouter(
    prefix='/api/v1',
    tags=['resource']
)

_endpoint_url = config['endpoint']['sparkQL_url']


class Queries:
    '''Konstruktor svog grafa jer nam on takav format RDF treba za BFS search'''
    def __init__(self, url, resource):
        self.url = url
        self.resource = resource
    #   self.category = category

    # current_category_Q = '''
    #                     SELECT ?category
    #                     WHERE {
    #                         <{url}resource/{resource}> dct:subject ?category .
    #                     }
    #

    def parent_category_Q(self):
        return f"""
            CONSTRUCT {{  dbc:{self.resource} skos:broader ?parent . 
                          dbc:{self.resource} skos:narrower ?child . }}
            WHERE {{ 
                    {{ dbc:{self.resource} skos:broader ?parent . }}
            UNION 
                {{ ?child skos:broader dbc:{self.resource} . }}
            }}
        """


def execute_sparql_query(endpoint_url: str, query: str):
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(TURTLE)
    results = sparql.query().convert()

    # print("Row resuls", results)
    return results

def remove_unused_prefixes(self):
        """ Clean up the long list of namespaces rdflib produces."""
        context = dict(self.graph.namespaces())
        used_prefixes = ['rdf', 'rdfs', 'sdo', 'skos', 'xml', 'xsd']
        return {i: j for i, j in context.items() if i in used_prefixes}


@router.get('/categories/{resource}', summary='Retrieve all parent and child categories for a given resource')
def get_slave_and_parent_categories_for_resource(resource: str, page: int = 1, page_size: Optional[int] = None):
        q_instance = Queries(url=config['endpoint']['base_url'], resource=resource)
        query = q_instance.parent_category_Q()
        result = execute_sparql_query(_endpoint_url, query)

        g = Graph()
        graph = g.parse(data=result, format='turtle')
        print("Broj cvorova u grafu:", len(graph))

        visited_categories = set()
        
        # Ako bismo za svaku kategoriju dobijenu na onosvu resursa, 
        # rekruzivno zvali get_slave_and_parent_categories_for_resource f-ju i davali joj novi resurs=dobijena kategorija, imali bi ogroman broj API-ja
        # zato pravimo red cekanja
        lista_cekanja = queue.Queue()

        visited_categories.add(resource)
        lista_cekanja.put(resource)

        layers = []

        while not lista_cekanja.empty():
            category = lista_cekanja.get()  
            categories = []

            for obj in graph.objects(subject=URIRef(category)):
                _cut = str(obj).split("/")[-1]
                if "Category:" in _cut:
                    obj = _cut.replace("Category:", "")
                    categories.append(obj) 

                # dodajemo i resurse jer mora postojati osnovni čvor za iteraciju preko njegovog susednog kada širimo grafikon
                categories.append(resource)

            
                # Trenutno, posto cemo ici po BFS alogirtmu, u prvom searchu po okidanju API-ja u graf dodajemo prvi layer oko resursa, sto nam daje dubinu 1
                layers.extend(expand_the_graph(graph, categories))
                for cat in categories:
                    if cat not in visited_categories: 
                        visited_categories.add(cat)
                        lista_cekanja.put(cat)

                if len(categories) == 0:
                    break
                    # raise NoResultsException 


            # context_used = remove_unused_prefixes()
            # serial_data =  categories.serialize(
            #         format="ttl",
            #         context=context_used,
            #         auto_compact=True
            #     )
        
        return {'categories': layers}




def expand_the_graph(graph: Graph, categories: List[str]) -> List[str]:
    # param: categories je lista  kategorija, tako da je to prakticno root, 

    visited = set(categories)
    stack = queue.Queue(maxsize=5000)

    for category in categories:
        stack.put(category)

    order = []

    while not stack.empty():
        node = stack.get()

        if node not in visited:
            order.append(node)
            visited.add(node)

            for n in graph.objects(subject=URIRef(node)):
                if n not in visited:
                    stack.put(str(n))
    
    return order


# {
#   "categories": "@prefix dbc: <http://dbpedia.org/resource/Category:> .\n@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n\ndbc:Machine_learning skos:broader dbc:Artificial_intelligence,\n        dbc:Learning ;\n    skos:narrower dbc:Applied_machine_learning,\n        dbc:Artificial_intelligence_conferences,\n        dbc:Artificial_neural_networks,\n        dbc:Bayesian_networks,\n        dbc:Blockmodeling,\n        dbc:Classification_algorithms,\n        dbc:Cluster_analysis,\n        dbc:Computational_learning_theory,\n        dbc:Data_mining_and_machine_learning_software,\n        dbc:Datasets_in_machine_learning,\n        dbc:Deep_learning,\n        dbc:Dimension_reduction,\n        dbc:Ensemble_learning,\n        dbc:Evolutionary_algorithms,\n        dbc:Genetic_programming,\n        dbc:Inductive_logic_programming,\n        dbc:Kernel_methods_for_machine_learning,\n        dbc:Latent_variable_models,\n        dbc:Learning_in_computer_vision,\n        dbc:Log-linear_models,\n        dbc:Loss_functions,\n        dbc:Machine_learning_algorithms,\n        dbc:Machine_learning_researchers,\n        dbc:Machine_learning_task,\n        dbc:Markov_models,\n        dbc:Natural_language_processing_researchers,\n        dbc:Ontology_learning_\\(computer_science\\),\n        dbc:Reinforcement_learning,\n        dbc:Semisupervised_learning,\n        dbc:Signal_processing_conferences,\n        dbc:Statistical_natural_language_processing,\n        dbc:Structured_prediction,\n        dbc:Supervised_learning,\n        dbc:Support_vector_machines,\n        dbc:Unsupervised_learning .\n\n"
# }



