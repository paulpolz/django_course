from django.shortcuts import render
from django.http import HttpResponse

def advertisement_list (request, *args, **kwargs):
	return render(request, 'advertisements/advertisement_list.html', {})

def advertisement_detail_01 (request, *args, **kwargs):
	return render(request, 'advertisements/advertisement_detail_01.html', {})

def advertisement_detail_02 (request, *args, **kwargs):
	return render(request, 'advertisements/advertisement_detail_02.html', {})

def advertisement_detail_03 (request, *args, **kwargs):
	return render(request, 'advertisements/advertisement_detail_03.html', {})

def advertisement_detail_04 (request, *args, **kwargs):
	return render(request, 'advertisements/advertisement_detail_04.html', {})

def advertisement_detail_05 (request, *args, **kwargs):
	return render(request, 'advertisements/advertisement_detail_05.html', {})