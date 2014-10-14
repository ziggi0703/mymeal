import datetime
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.views import generic

from decision_maker.models import Restaurant


def vote_form(request):
    date = datetime.datetime.today().strftime('%Y%m%d')
    restaurants = Restaurant.objects.order_by('name')
    context = {'date': date,
               'restaurants': restaurants}

    return render(request, 'decision_maker/vote_form.html', context)


def vote(request, date):
    try:
        selected_restaurant = Restaurant.objects.all().get(pk=request.POST['restaurant'])
    except (KeyError, Restaurant.DoesNotExist):
        return render(request, 'decision_maker/vote_form.html',
                      {'restaurants': Restaurant.objects.all().order_by('name'),
                       'date': date})
    else:
        selected_restaurant.todays_vote += 1
        selected_restaurant.save()

        return HttpResponseRedirect(reverse('decision_maker:user_result', args=(selected_restaurant.id,)))


class IndexView(generic.ListView):
    template_name = 'decision_maker/index.html'
    context_object_name = 'restaurants'

    def get_queryset(self):
        """
        :return: all restaurants in table Restaurant
        """
        return Restaurant.objects.all().order_by('name')


class DetailView(generic.DetailView):
    model = Restaurant
    template_name = 'decision_maker/detail.html'


class UserResultView(generic.DetailView):
    model = Restaurant
    template_name = 'decision_maker/user_result.html'