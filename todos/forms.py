from django import forms
from .models import Todo


class CreateTodoForm(forms.ModelForm):
    """ create todo form definition """

    class Meta:
        model = Todo
        fields = ('title', 'description', 'category',)


class UpdateTodoForm(forms.ModelForm):
    """ update todo form definition """

    class Meta:
        model = Todo
        fields = ('title', 'description', 'category',)

