import os

from neo4j.v1 import GraphDatabase, basic_auth

driver = None

def run(query, param={}):
    return get_session().run(query, param)

def get_session():
    global driver
    if driver is None:
        user = os.environ.get('NEO4J_USER')
        password = os.environ.get('NEO4J_PASS')
        driver = GraphDatabase.driver("bolt://db:7687", auth=basic_auth(user, password))
    return driver.session()
