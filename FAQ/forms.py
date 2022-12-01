from django import forms



class quessionForm(forms.Form):
    name = forms.CharField(required=True,min_length=3, max_length=25, widget = forms.TextInput(attrs={"class" : "form-control mt-3", "name":"name", "placeholder":"Ваше имя"}))
    email = forms.EmailField(required=True,min_length=7,widget = forms.EmailInput(attrs={"class" : "form-control mt-3", "name" : "email", "placeholder" : "Ваш email"}))
    # body_quession = forms.Textarea(widget = forms.Textarea(attrs={"class" : "form-control", "rows" : "7", "placeholder" : "Напишите ваш вопрос",  "name" : "ques"}))
    quession = forms.CharField(required=True,widget=forms.Textarea(attrs={"class" : "form-control mt-3", "rows" : "7", "placeholder" : "Напишите ваш вопрос",  "name" : "ques"}))