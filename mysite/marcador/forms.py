#e form class BookmarkForm is also called a ModelForm because it inherits from django.forms.ModelForm
#ModelForms automatically create form fields for every field in the model to which they belong. 
from django.forms import ModelForm

from .models import Bookmark


class BookmarkForm(ModelForm):
    class Meta:
        model = Bookmark
        exclude = ('date_created', 'date_updated', 'owner')
