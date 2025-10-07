from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class aboutView(TemplateView):
    template_name = 'pages/about.html'


class EventView(TemplateView):
    template_name = 'pages/events.html'


class LocationView(TemplateView):
    template_name = 'pages/join.html'


class MailingListView(TemplateView):
    template_name = 'pages/mailing-list.html'


class PressView(TemplateView):
    template_name = 'pages/press.html'


class ProtocolView(TemplateView):
    template_name = 'pages/protocols.html'


class PublicationView(TemplateView):
    template_name = 'pages/publications.html'


class ResearchTopic1View(TemplateView):
    template_name = 'pages/research-topic-1.html'


class ResearchTopic2View(TemplateView):
    template_name = 'pages/research-topic-2.html'


class ResearchTopic3View(TemplateView):
    template_name = 'pages/research-topic-3.html'


class TrainingView(TemplateView):
    template_name = 'pages/training.html'


class WorkingGroupView(TemplateView):
    template_name = 'pages/working-group.html'
