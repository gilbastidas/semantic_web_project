from rdflib import Graph

g = Graph()
g.parse("version3-A.ttl", format="turtle")

for row in g.query(
            'select * where { ?s ?p ?o .}LIMIT 10'):
        print row.s
