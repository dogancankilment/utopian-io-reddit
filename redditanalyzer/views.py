from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from forms import ChoiceForm
import feedparser


def home(request):
    form = ChoiceForm(request.POST or None)

    if request.POST:
        query = feedparser.parse('https://www.reddit.com/r/utopianio/.rss')
        entry_count = len(query['entries'])
        all_entries = query['entries']
        choice = request.POST["example-select"]

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