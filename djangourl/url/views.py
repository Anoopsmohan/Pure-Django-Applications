# Create your views here.
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import django
from django import http
from django import shortcuts
import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import random
from url.models import ShortUrl

def main(request):
    return render_to_response('index.html')


def handle_error(request,template, msg, params=None):

    if params is None:
        params={}
    params['error']=msg
    return shortcuts.render_to_response(template, params)


@csrf_exempt
def posted(request):
    try:
	s=1
	z=0
	count=[]
	ourl = request.POST['url']
	code=request.POST['slug']
 	char_array = "abcdefgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_"
	count=ShortUrl.objects.filter(ourl=ourl)
	cnt=ShortUrl.objects.filter(code=code)	
 	z=len(count)
	y=len(cnt)
	if z > 0:
	    surl=count[0].surl
 	if code:
	    if y >0:
	        raise SlugException("""
                The customized url you specified (%s) has already been taken
                Try using a different url or leave it blank for a default.
                """ % code)
	    elif y==0:
	        surl="http://127.0.0.1:8000/"+code
		#surl="http://dj-url.appspot.com/"+code
		g=ShortUrl(
				ourl=ourl,
				code=code,
				surl=surl)
		g.save();		
        elif z==0:
	    while s>0:
	        word = "".join(random.choice(char_array) for i in range(4))
		x=ShortUrl.objects.filter(code=code)
                s = len(x)   		
	    #surl="http://dj-url.appspot.com/"+word
	    surl="http://127.0.0.1:8000/"+word
	    g=ShortUrl(
				ourl=ourl,
				code=word,
				surl=surl)
	    g.save();
	params={}
	params['ref']=ourl
	params['ShortUrl']=ourl
	params['short_url']= surl.replace("www.", "")      
	return shortcuts.render_to_response("index.html", params)
   
    except SlugException, slug_error:
        return handle_error(request,"index.html",str(slug_error),{})
    except Exception, ex:
        msg = """The URL you submitted (%s) does not appear to be a valid one !
         <br/>%s.
         """ % (request.POST['url'], str(ex))
        return handle_error(request,"index.html",msg,{})


class SlugException(Exception):
    def __init__(self, value = ''):
        self.value = value
    def __str__(self):
        return self.value
	
	
def forwardurl(request,path):
    try:
	code = request.path
	print code
        count=ShortUrl.objects.filter(code=path)
	y=len(count)
        if y==1:
            ourl = count[0].ourl
	    return http.HttpResponseRedirect(ourl)
	else:
	    raise SlugException("""
                The code you specified (%s) does not exists in the database !
                """ % code)
    except SlugException, slug_error:
        return handle_error(request,"index.html",str(slug_error),{})



	
	