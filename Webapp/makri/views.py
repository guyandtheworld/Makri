# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.encoding import smart_bytes, smart_str
from makri.forms import UploadFileForm

from rest_framework.response import Response
from .serializer import MakriClassifier

import os, json
import Classifier.new as n

from rest_framework import views


def corpus(request):

    #os.chdir('RDRPOSTagger/pSCRDRtagger')

    form = UploadFileForm()

    if request.method == 'GET':
        query =request.GET.get('q')
        if query is not None:
            query = smart_str(query, )
            result = (n.out(query))
            #result = json.dumps({'Tagged':result})
            return HttpResponse(result)
        else:
            args = {'stat':False, 'form':form}
            return render(request, 'makri/index.html', args)


    if request.method == 'POST':
        if request.POST['data'] != '' :
            data = (request.POST['data'])
            data = smart_bytes(data,encoding='utf-8')
            args = {'stat':True, 'form':form, 'output':n.out(data)}
            return render(request, 'makri/index.html', args)
        else:
            form = UploadFileForm(request.POST, request.FILES)
            f = open('result.txt', 'w+')
            result = n.out(request.FILES['file'].read())


            response = HttpResponse(f,content_type='application/txt')
            response['Content-Disposition'] = 'attachment; filename="%s"'%os.path.basename('/mysite/'+request.FILES['file'].name)
            response.write(result)
            f.close()
            return response
            args = {'stat':True, 'form':form, 'output':n.file_process(request.FILES['file']),  }

            return render(request,'makri/index.html', args)
    else:
        args = {'stat':False, 'form':form}
        return render(request, 'makri/index.html', args)

class Api(views.APIView):

    def get(self,request):
        data = request.GET.get('q','')
        result = n.out(data)
        return Response(result)
