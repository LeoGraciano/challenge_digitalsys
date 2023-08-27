from rest_framework.throttling import UserRateThrottle, BaseThrottle, SimpleRateThrottle
from django.core.cache import caches


class CustomAbstractRequest():

    # def allow_request(self, request, view):
    #     if not PlanUser.objects.filter(user=request.user, plan__name=self.scope).exists():
    #         if not request.user.is_staff:
    #             return True

    #     self.rate = self.get_rate()
    #     self.num_requests, self.duration = self.parse_rate(self.rate)

    #     return super().allow_request(request, view)

    # def get_cache_key(self, request, view):
    #     if request.user.is_authenticated:
    #         ident = request.user.pk
    #     else:
    #         ident = self.get_ident(request)

    #     return self.cache_format % {
    #         'scope': self.scope,
    #         'ident': ident
    #     }
    ...


class StaffRateThrottle(CustomAbstractRequest, SimpleRateThrottle):
    cache = caches['default']
    scope = 'staff'


class VipRateThrottle(CustomAbstractRequest, SimpleRateThrottle):
    cache = caches['default']
    scope = 'vip'


class PremiumRateThrottle(CustomAbstractRequest, SimpleRateThrottle):
    cache = caches['default']
    scope = 'premium'
