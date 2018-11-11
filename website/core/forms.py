from django import forms

class EloUrlToBeShorten(forms.Form):
    elo_url_to_be_shorten = forms.CharField(max_length=1000,label="",widget=forms.TextInput(attrs={'id':'url_parcial_input','type':'text','name':'url_parcial_input','value':'','class':'form-control'}))
    