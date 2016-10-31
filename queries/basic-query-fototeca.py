from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://semtech.mty.itesm.mx:3030/Fototeca/sparql")
uri = "<http://semtech.mty.itesm.mx:8888/marmotta/resource/fototeca/2454/120621_105237F>"
sparql.setQuery("""
    SELECT ?property ?object
    WHERE {""" +
         uri + """ ?property ?object  .
    }
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print result["property"]['value'], result["object"]['value']