from django.shortcuts import render
from django.http import HttpResponse
from semanticquery.forms import SearchForm
from django.http import HttpResponseRedirect
from SPARQLWrapper import SPARQLWrapper, JSON
import json


# Create your views here.
def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage ]] in the template!
    #context_dict = {'boldmessage': "Cruncy, creamy, cookie, candy, cupcake!"}

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

        sparql = SPARQLWrapper("http://semtech.mty.itesm.mx:3030/Fototeca/sparql")
        sparql.setQuery("""
                    SELECT ?property ?object
                    WHERE {""" +
                        uri + """ ?property ?object  .
                    }
                """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        concepts = []
        qproperties = []
        qobjects = []
        arreglo = [10,20,30,40,50]
        for result in results["results"]["bindings"]:
            #print result["property"]['value'], result["object"]['value']
            qproperties.append(result["property"]['value'])
            qobjects.append(result["object"]['value'])
        context_dict = {'query_properties': json.dumps(qproperties), 'query_objects': json.dumps(qobjects)}

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



#def search_query_results(request):
 #   context_dict = {'name': "Gil"}
  #  return render(request, 'semanticquery/search_query_results.html', context_dict)


