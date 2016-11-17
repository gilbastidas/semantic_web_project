from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://semtech.mty.itesm.mx:3030/Fototeca/sparql")
sparql.setQuery("""
    SELECT *
    WHERE {
         <http://semtech.mty.itesm.mx:8888/marmotta/resource/fototeca/Aggregation_6951/121105_110744F> ?p ?o .
    } limit 50
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

print ("subject " + " property " + " object")
for result in results["results"]["bindings"]:
    print  result["p"]['value'], result["o"]['value']



