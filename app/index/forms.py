from django import forms

class MovieForm(forms.Form):
    title = forms.CharField(required=True, max_length=100, label="Title")
    year = forms.IntegerField(required=True, min_value=1900, max_value=2100, label="Year of release")
    genres = forms.CharField(required=True, max_length=100, label="Genres")
    duration = forms.IntegerField(required=False, min_value=0, max_value=1000, label="Running time")
    director = forms.CharField(required=False, max_length=100, label="Director")
    writer = forms.CharField(required=False, max_length=100, label="Writer")
    producer = forms.CharField(required=False, max_length=100, label="Producer")
    starring = forms.CharField(required=False, max_length=500, label="Starring")
    sources = forms.CharField(required=False, max_length=1000, label="Additional source links")
