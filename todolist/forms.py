from .models import createtodo
from django import forms

class todoform(forms.ModelForm):
	class Meta():
		model=createtodo
		fields=[
		'Name','Date','Time','Description']
	def clean_Name(self):
		name=self.cleaned_data.get('Name')
		date=self.cleaned_data.get('Date')
		time=self.cleaned_data.get('Time')
		description=self.cleaned_data.get('Description')
		for i in createtodo.objects.all():
			if name.upper()==i.Name.upper() and i.Date == date and i.Time == time and i.Description == description:
				print('matched!')
				raise forms.ValidationError('To Do already exists!')
		return name
