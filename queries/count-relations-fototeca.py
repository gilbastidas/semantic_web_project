from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://semtech.mty.itesm.mx:3030/Fototeca/sparql")
sparql.setQuery("""
    SELECT ?property1 ?property2 (count(?object) as ?relations) ?foto2
    WHERE {
      <http://semtech.mty.itesm.mx:8888/marmotta/resource/fototeca/2454/120621_105237F> ?property1 ?object  .
      ?foto2 ?property2 ?object .
      filter(?property1 = ?property2)
      ?foto2 a <http://semtech.mty.itesm.mx:8888/marmotta/resource/fototeca/Picture> .
      filter(?property1 != <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>)
      filter(?foto2 != <http://semtech.mty.itesm.mx:8888/marmotta/resource/fototeca/2454/120621_105237F>)
    }
    group by ?property1 ?property2 ?foto2
    ORDER BY DESC(?relations)
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print result["relations"]['value'],result["foto2"]['value'],



