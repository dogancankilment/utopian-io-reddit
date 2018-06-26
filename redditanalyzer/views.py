from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from forms import ChoiceForm
from authentication.models import Queries
from django.contrib.auth.decorators import login_required
import feedparser


@login_required()
def analysis(request):
    form = ChoiceForm(request.POST or None)

    if request.POST:
        query_url = request.POST["query_url"]
        query = feedparser.parse(query_url + str('.rss'))
        entry_count = len(query['entries'])
        all_entries = query['entries']
        choice = request.POST["example-select"]

        if request.user:
            new_query = Queries()
            new_query.url = query_url
            new_query.which_user = request.user

            new_query.save()

        c = {"request": request,
             "all_entries": all_entries,
             "choice": choice,
             "entry_count": entry_count}

        c.update(csrf(request))

        return render_to_response("results/utopian-io-reddit-feed.html", c)

    c = {"request": request,
         "form": form}

    c.update(csrf(request))

    return render_to_response("forms/make-choice.html", c)


def home(request):
    c = {"request": request}
    c.update(csrf(request))
    return render_to_response("home/index.html", c)


def show_old_queries(request):
    all_queries = Queries.objects.filter(which_user=request.user)

    c = {"request": request,
         "all_queries": all_queries}

    c.update(csrf(request))

    return render_to_response("auth/queries.html", c)