

sparql = SPARQLWrapper("http://semtech.mty.itesm.mx:3030/Fototeca/sparql")
sparql.setQuery("""
    SELECT *
    WHERE {
         ?s ?p ?o .
    } limit 50
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

print ("subject " + " property " + " object")
for result in results["results"]["bindings"]:
    print result["s"]['value'], result["p"]['value'], result["o"]['value']



