from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import hill_cipher
from . import blowfish_cipher

# Create your views here.

def index(request):
    return render(request, "cipher/index.html")

obj1= hill_cipher.HillCipher()

def hill_encryption(request):
    if request.method == "POST": 
        text = request.POST['text']
        if True:
            e_text = obj1.encrypt(text, [[3, 3], [2, 5]])
            return render(request, "cipher/hill_encryption.html",{
                "text": text,
                "e_text": e_text
            })
        else:
            return HttpResponseRedirect(reverse("cipher:hill_encryption"))
    else:
        return render(request, "cipher/hill_encryption.html")

def hill_decryption(request):
    if request.method == "POST": 
        d_text = request.POST['text']
        if True:
            text = obj1.decrypt(d_text, [[3, 3], [2, 5]])
            return render(request, "cipher/hill_decryption.html",{
                "text": text,
                "d_text": d_text
            })
        else:
            return HttpResponseRedirect(reverse("cipher:hill_decryption"))
    else:
        return render(request, "cipher/hill_decryption.html")

obj2 = blowfish_cipher.BlowfishCipher()

def blowfish_encryption(request):
    if request.method == "POST": 
        text = request.POST['text']
        if text.isdigit():
            text = int(text)
            if True:
                e_text = obj2.encrypt(text)
                return render(request, "cipher/blowfish_encryption.html",{
                    "text": text,
                    "e_text": e_text
                })
            else:
                return HttpResponseRedirect(reverse("cipher:blowfish_encryption"))
        elif text is "":
            return HttpResponseRedirect(reverse("cipher:blowfish_encryption"))
            
        else:
            return render(request, "cipher/error.html")
            
    else:
        return render(request, "cipher/blowfish_encryption.html")

def blowfish_decryption(request):
    if request.method == "POST": 
        d_text = request.POST['text']
        if d_text.isdigit():
            d_text = int(d_text)
            if True:
                text = obj2.decrypt(d_text)
                return render(request, "cipher/blowfish_decryption.html",{
                    "text": text,
                    "d_text": d_text
                })
            else:
                return HttpResponseRedirect(reverse("cipher:blowfish_decryption"))
        elif d_text is "":
            return HttpResponseRedirect(reverse("cipher:blowfish_decryption"))
            
        else:
            return render(request, "cipher/error.html")
            
    else:
        return render(request, "cipher/blowfish_decryption.html")
    
    # Software Engineer Joseph 20202273
    
    
    