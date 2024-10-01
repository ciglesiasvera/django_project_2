# book/views.py
from django.shortcuts import render, redirect
from .forms import BookForm

def input_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('inputbook')  
    else:
        form = BookForm()

    return render(request, 'book/input_book.html', {'form': form})
