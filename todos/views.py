from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.messages.views import SuccessMessageMixin
from .models import Todo, Category
from .forms import CreateTodoForm, UpdateTodoForm


class TodoHomeView(ListView):
    """ Todo home view definition """
    model = Todo
    paginate_by = 4
    page_kwarg = 'page'
    context_object_name = 'todos'
    template_name = 'todos/home.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(TodoHomeView, self).get_context_data()
        context['category_menu'] = category_menu
        return context


class TodoCreateView(SuccessMessageMixin, CreateView):
    """ Todo create view definition """
    model = Todo
    form_class = CreateTodoForm
    template_name = 'todos/create_todo.html'
    success_url = reverse_lazy('todos:home')
    success_message = 'todo added !!'


class TodoUpdateView(SuccessMessageMixin, UpdateView):
    """ Todo update view definition """
    model = Todo
    form_class = UpdateTodoForm
    template_name = 'todos/update_todo.html'
    success_url = reverse_lazy('todos:home')
    success_message = 'Value updated !'


class TodoDeleteView(SuccessMessageMixin, DeleteView):
    """ Todo delete view definition """
    model = Todo
    template_name = 'todos/confirm_delete.html'
    success_url = reverse_lazy('todos:home')
    success_message = 'Value deleted !'


class CategoryFilterView(View):
    """ Category filter view definition """

    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        print(category)
        todos_by_category = Todo.objects.filter(category=category)
        context = {
            'category': category,
            'todos_by_category': todos_by_category
        }
        return render(request, 'todos/category_wise_todo.html', context)
