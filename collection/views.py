from django.shortcuts import render

from index.appviews import AppBaseTemplateView


class CollectionView(AppBaseTemplateView):
    template_name = 'collection/collection.html'
