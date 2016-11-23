from django.shortcuts import render
from django.http import HttpResponse
from semanticquery.forms import SearchForm
from django.http import HttpResponseRedirect
from SPARQLWrapper import SPARQLWrapper, JSON
from django.utils.safestring import mark_safe
import json


# Create your views here.
def index(request):
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that te first parameter is the template we wish to use.
    #return render(request, 'semanticquery/index.html', context=context_dict)
    form = SearchForm(request.GET or None)
    context = {
        "form": form
    }
    if form.is_valid():
        # print form.cleaned_data
        sparql_endpoint = form.data['sparql_endpoint']
        uri = form.data['uri']
        prefix = form.data['prefix']
        varproperty = form.data['varProperty']

        results = query(prefix, uri, varproperty, sparql_endpoint)
        concepts = []
        qobjects = []
        qrelations = []
        qpicurl = []

        for result in results["results"]["bindings"]:
            #print result["property1"]['value'], result["relations"]['value']
            qobjects.append(result["foto2"]['value'])
            qrelations.append(result["relations"]['value'])
            qpicurl.append(result["picurl"]['value'])
            query2 = query(prefix, result["foto2"]['value'], varproperty, sparql_endpoint)

            for result2 in query2["results"]["bindings"]:
                print result2["relations"]['value'], result2["picurl"]['value']

        context_dict = { 'query_objects': json.dumps(qobjects), 'query_relations': json.dumps(qrelations), 'query_picurl': json.dumps(qpicurl), 'uri_view': uri, 'resultados': json.dumps(results["results"]["bindings"])}
        # return HttpResponseRedirect('/semanticquery/search_query_results/')
        return render(request, 'semanticquery/search_query_results.html', context_dict)

    return render(request, 'semanticquery/index.html', context)

def about(request):
    #return HttpResponse("Rango says here is the about page <a href='/semanticquery'>Home</a> ")
    context_dict = {'name': "Gil"}
    return render(request, 'semanticquery/about.html', context=context_dict)

def search_query(request):
    form = SearchForm(request.GET or None)
    context = {
        "form": form
    }
    if form.is_valid():
        # print form.cleaned_data
        sparql_endpoint = form.data['sparql_endpoint']
        uri = form.data['uri']
        context_dict = {'sparql_endpoint': sparql_endpoint}
        #return HttpResponseRedirect('/semanticquery/search_query_results/')
        return render(request, 'semanticquery/search_query_results.html', context_dict)
    return render(request, 'semanticquery/search_query.html', context)


def query(prefix, uri, varproperty, sparqlendpoint):
    sparql = SPARQLWrapper(sparqlendpoint)
    sparql.setQuery("""
                        PREFIX """ + prefix + """
                        SELECT ?picurl (count(?object) as ?relations) ?foto2
                        WHERE { <""" + uri + """>
                            ?property1 ?object  .
                            OPTIONAL { ?foto2 """ + varproperty + """ ?picurl }.
                            ?foto2 ?property2 ?object .
                            filter(?property1 = ?property2)
                            ?foto2 a <http://semtech.mty.itesm.mx:8888/marmotta/resource/fototeca/Picture> .
                            filter(?property1 != <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>)
                            filter(?foto2 != <""" + uri + """>)
                        }
                        group by ?foto2 ?picurl
                        ORDER BY DESC(?relations)
                        LIMIT 10
                    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

#def search_query_results(request):
 #   context_dict = {'name': "Gil"}
  #  return render(request, 'semanticquery/search_query_results.html', context_dict)