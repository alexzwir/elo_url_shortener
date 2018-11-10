from django.shortcuts import render
from django.http import HttpResponse

from .forms import EloUrlToBeShorten
from pyshorteners import Shortener

# Create your views here.

def home(request):
    form_elo_url_to_be_shorten = EloUrlToBeShorten()
    return render(request,'index.html',{"form_elo_url_to_be_shorten":form_elo_url_to_be_shorten})


def elo_url_shortener(request):
    form_url_to_be_shorten_raw = EloUrlToBeShorten(request.POST)
    if form_url_to_be_shorten_raw.is_valid():
        url_raw = form_url_to_be_shorten_raw.cleaned_data['elo_url_to_be_shorten']
        s = Shortener(api_key='94d77dc93cb4db2ef89ce7dfc23dbd80168af1a2')
        final_elo_shorten_bitly_url = s.bitly.short(url_raw)
        print(final_elo_shorten_bitly_url)
    else:
        url_raw="Não deu certo!"
        print(url_raw)
    return HttpResponse(final_elo_shorten_bitly_url)
    


    # s = Shortener()
    # url_to_be_shorten = s.tinyurl.short('https://use.elo.com.br/')
    # url_to_be_shorten_bily = s.bitly.short('https://use.elo.com.br/')
    # print(url_to_be_shorten)
    # print(url_to_be_shorten_bily)

    # s = pyshorteners.Shortener(api_key='YOUR_KEY')
