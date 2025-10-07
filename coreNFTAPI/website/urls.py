from django.urls import path
from .views import (
    IndexView,
    aboutView,
    EventView,
    LocationView,
    MailingListView,
    PressView,
    ProtocolView,
    PublicationView,
    ResearchTopic1View,
    ResearchTopic2View,
    ResearchTopic3View,
    TrainingView,
    WorkingGroupView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', aboutView.as_view(), name='about'),
    path('events/', EventView.as_view(), name='events'),
    path('join/', LocationView.as_view(), name='join'),
    path('mailing-list/', MailingListView.as_view(), name='mailing_list'),
    path('press/', PressView.as_view(), name='press'),
    path('protocols/', ProtocolView.as_view(), name='protocols'),
    path('publications/', PublicationView.as_view(), name='publications'),
    path('research-topic-1/', ResearchTopic1View.as_view(), name='research_topic_1'),
    path('research-topic-2/', ResearchTopic2View.as_view(), name='research_topic_2'),
    path('research-topic-3/', ResearchTopic3View.as_view(), name='research_topic_3'),
    path('training/', TrainingView.as_view(), name='training'),
    path('working-group/', WorkingGroupView.as_view(), name='working_group'),
]
