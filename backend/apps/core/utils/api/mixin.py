from rest_framework import viewsets, mixins


class EnablePartialUpdateMixin:
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class ListUpdateMixer(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    pass


class ListDestroyMixer(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    pass
