from django import forms

class SearchForm(forms.Form):
    sparql_endpoint = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}), initial="http://semtech.mty.itesm.mx:3030/Fototeca/sparql")
    uri = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}), initial="http://semtech.mty.itesm.mx:8888/marmotta/resource/fototeca/2454/120621_105237F" )
    prefix = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}), initial="edm: <http://purl.org/dc/elements/1.1/>" )
    varProperty = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}), initial="edm:identifier")




