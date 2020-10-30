# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from filecomparision import file_comparision
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,JsonResponse
from . import forms
from filesetting import settings
import json

file_path = settings.MEDIA_ROOT

@csrf_exempt
def comp_file(request):

    if request.method == 'POST':

        try:

            myfile_1 = request.FILES['file_1']

        except:

            pass

        try:

            myfile_2 = request.FILES['file_2']

        except:

            pass


        fs = FileSystemStorage()

        try:

            file_1_name = fs.save(myfile_1.name,myfile_1)

        except:

            pass

        try:

            file_2_name = fs.save(myfile_2.name, myfile_2)

        except:

            pass

        try:
            first_file = file_path + '/' + file_1_name
        except:
            pass
        try:
            second_file = file_path + '/' + file_2_name
        except:
            pass

        try:
            result = file_comparision.filecomparision(first_file, second_file)
        except:
            pass

        # print(file_1_name)
        # with open(file_path+'/'+'file_similar.txt', 'w') as fs:
        #     fs.writelines(result['similar_sentences'])
        #     fs.close()
        try:
            rreturn={'similar_sent':result['similar_sentences'],
                                 'data1_minus_data2':result['data1_minus_data2'],
                                 'data2_minus_data1':result['data2_minus_data1'],
                     'freq_file_1':result['freq_file_1'].items(),
                     'freq_file_2': result['freq_file_2'].items(),
                     'similar_sent_length':result['similar_sentences_length'],
                     'data1_minus_data2_length':result['data1_minus_data2_length'],'data2_minus_data1_length':result['data2_minus_data1_length'],
                     'file_1_name':file_1_name,'file_2_name':file_2_name,

                     }

        except:
            rreturn={"text":'error'}


        return render(request,'balancesheet.html',rreturn)  #jreturn

    uploaded_form = forms.File_Upload_Form()


    return render(request,'balancesheet.html',{'form':uploaded_form})

