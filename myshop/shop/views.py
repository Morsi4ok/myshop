from django.shortcuts import render

from shop.forms import AddNoteForm
from shop.models import Shop


def index(request):
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            Shop.objects.create(
                title=form.cleaned_data["title"], text=form.cleaned_data["text"]
            )
    else:
        form = AddNoteForm()
    shop = Shop.objects.all()
    return render(request, "shop_list.html", {"shop": shop, "form": form})
