from django.shortcuts import render
from cowsayapp.models import CowsayInput
from cowsayapp.form import CowsayForm
from subprocess import check_output


def main(request):
    if request.method == "POST":
        form = CowsayForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CowsayInput.objects.create(
                body=data['body']
            )
            display = check_output(["cowsay", data['body']]).decode("utf-8")  # decode converts the text from bite to string
            return render(request, 'main.html', {'form': form, 'display': display})
    form = CowsayForm()
    return render(request, 'main.html', {'form': form})


def recents(request):
    viewable = ""
    data = CowsayInput.objects.order_by('-id')[:10]
    for x in data:
        viewable += check_output(["cowsay", x.body]).decode("utf-8")
    return render(request, 'history.html', {'viewable': viewable})
