from django.shortcuts import render,get_object_or_404,HttpResponse,redirect,reverse
from django.views import View
from django.views.generic import UpdateView,CreateView,DeleteView,ListView,DetailView
from .models import createtodo
from .forms import todoform
from django.views.generic.edit import FormView
import os


from django import forms
# Create your views here.
class ValidationMixin:
	def getform(self,formname):
		form=formname
		return form

class CreateTodo(CreateView):
	template_name='createtodo.html'
	context_object_name='form'
	success_url='../'
	form_class=todoform
	def form_valid(self,form):
		return super().form_valid(form)
		

		
class UpdateTodo(View):
	template_name='updatetodo.html'
	context_object_name='form'
	form_class=todoform
	success_url='../'
	pk_url_kwarg='id'
	def get(self,request,id):
		queryset=get_object_or_404(createtodo,id=id)
		form=self.form_class(instance=queryset)
		return render(request,self.template_name,context={self.context_object_name:form})
	def post(self,request,id):
		queryset=get_object_or_404(createtodo,id=id)
		form=self.form_class(request.POST,instance=queryset)
		if form.is_valid():
			form.save()
			return redirect(self.success_url)
		return render(request,self.template_name,context={self.context_object_name:form})
	

class UpdateTodoSearch(UpdateView):
	template_name='updatetodosearch.html'
	context_object_name='form'
	form_class=todoform
	pk_url_kwarg='id'
	def get(self,request,id):
		queryset=get_object_or_404(createtodo,id=id)
		form=self.form_class(instance=queryset)
		return render(request,self.template_name,context={self.context_object_name:form})
	def post(self,request,id):
		queryset=get_object_or_404(createtodo,id=id)
		form=self.form_class(request.POST,instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('../')
		return render(request,self.template_name,context={self.context_object_name:form})
	


class ListTodo(ListView):
	
	template_name='listtodo.html'
	context_object_name='form'
	queryset=createtodo.objects.all()

class DetailTodo(ListView):
	template_name='detailtodo.html'
	context_object_name='form'
	queryset=createtodo.objects.all()

class SearchTodoDetail(DetailView):
	template_name='searchtodo.html'
	context_object_name='form'
	def get(self,request):
		
		data=request.GET.get('q')
		length=len(data) if data else 0
		detail=[]
		for i in createtodo.objects.all():
			if i.Name.upper()[0:length] == data.upper():
				collected={'id':i.id,'Name':i.Name,'Date':i.Date,
			'Time':i.Time,'Description':i.Description}
				detail.append(collected)
				print(i.Name,'is matched!')
			else:pass
		print(detail)
		context={
		self.context_object_name:detail,
		}
		return render(request,self.template_name,context)
		
class SearchTodoList(DetailView):
	template_name='searchtodolist.html'
	context_object_name='form'
	def get(self,request):
		
		data=request.GET.get('q')
		print(f"received : {data}")
		length=len(data) if data else 0
		data = "" if not data else data

		detail=[]
		for i in createtodo.objects.all():
			if i.Name.upper()[0:length] == data.upper():
				collected={'id':i.id,'Name':i.Name,'Date':i.Date,
				'Time':i.Time,'Description':i.Description}
				detail.append(collected)
				print(i.Name,'is matched!')
			else:pass
		print(detail)
		context={
		self.context_object_name:detail,
		}
		return render(request,self.template_name,context)

class DeleteTodoSearch(DeleteView):
	model=createtodo
	queryset=createtodo.objects.all()
	success_url='.././'
	def get(self,request,id):
		for i in self.queryset:
			if i.id == id:
				i.delete()
		return redirect(self.success_url)

class DeleteTodo(DeleteTodoSearch):
	success_url='../'


def home(request):
	user=request.user
	context={
	'user':user,
	}
	return render(request,'index.html',context)