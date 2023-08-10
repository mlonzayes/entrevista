from django import forms



class MyTaskForm(forms.Form):
     title=forms.CharField(label='title',max_length=200,required=True)
     description=forms.CharField(label='description',max_length=200,required=True)
     expire=forms.DateField(label='expire date',required=True)
     finish=forms.BooleanField(label='finish?',required=True)
