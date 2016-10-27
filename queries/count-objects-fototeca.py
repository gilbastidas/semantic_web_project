from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://semtech.mty.itesm.mx:3030/Fototeca/sparql")
sparql.setQuery("""
    SELECT ?property1 ?property2 ?property3 ?property4 (count(?object) as ?relations)
    WHERE {
         <http://semtech.mty.itesm.mx:8888/marmotta/resource/fototeca/2454/120621_105237F> ?property1 ?object1  .
         ?object1 ?property3 ?object .
         ?foto2 ?property2 ?object2 .
         ?object2 ?property4 ?object .
    }
    group by ?property1 ?property2 ?property3 ?property4
    order by ?property1 ?property2 ?property3 ?property4
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

print ("subject " + " property " + " object")
for result in results["results"]["bindings"]:
    print result["property1"]['value'], result["property2"]['value'], result["property3"]['value'], result["property4"]['value']



