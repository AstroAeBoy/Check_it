from django.shortcuts import render
from . import models
from django.http import HttpResponse
from collections import OrderedDict
# Create your views here.


def index(request):
    return render(request, 'index.html',)

# def Data_to_index():
#     TNJ=models.Tour(1,'Thanjavur','Situated in TN', 1000,"custom/thanjavur.jpg")
#     BOM=models.Tour(2,'Bombay','Situated in Maharastra', 3000,"custom/thanjavur.jpg")
#     DEL = models.Tour(3, 'DELHI', 'Situated in Delhi', 200,"custom/thanjavur.jpg")
#     TNJ_2 = models.Tour(1, 'Thanjavur', 'Situated in TN', 1000, "custom/thanjavur.jpg")
#     BOM_2 = models.Tour(2, 'Bombay', 'Situated in Maharastra', 3000, "custom/thanjavur.jpg")
#     DEL_2 = models.Tour(3, 'DELHI', 'Situated in Delhi', 200, "custom/thanjavur.jpg")
#     return [TNJ,BOM,DEL,TNJ_2,BOM_2,DEL_2]
#
# def index(request):
#     """
#     The index page with dynamic content
#     :param request: From Client
#     :return:
#     """
#     if request.method=='GET':
#         data=Data_to_index()
#         # final_dict=OrderedDict()
#         # i=1
#         # for each in data:
#         #     key='data_'+str(i)
#         #     final_dict[key]=each
#         #     i+=1
#         # print(final_dict)
#         # return render(request,'index.html',final_dict)  final_dict={'dict_1':TNJ}
#         return render(request, 'index.html', {'data':data})
#


