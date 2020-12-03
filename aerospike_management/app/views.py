from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .forms import BackupForm

@login_required(login_url="/login/")
def index(request):
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))



def backup_data(request):
    msg = None
    success = False

    if request.method == "POST":
        form = BackupForm(request.POST)
        if form.is_valid():
        #     form.save()
            namespace = form.cleaned_data.get("namespace")
            dest_ntk_addr = form.cleaned_data.get("dest_ntk_addr")
            srcfilesys = form.cleaned_data.get("srcfilesys")
            ssh_username = form.cleaned_data.get("ssh_username")
            ssh_password = form.cleaned_data.get("ssh_password")
                # user = authenticate(username=username, password=raw_password)

            msg = 'Getting data %s , %s, %s, %s, %s,',namespace,dest_ntk_addr,srcfilesys,ssh_password,ssh_username
            success = True
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.", msg)
            # return redirect("/login/")

        # else:
        # msg = 'Form is not valid %s',form.errors
    else:
        form = BackupForm()

    return render(request, "ui-forms.html", {"form": form, "msg": msg, "success": success})

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))