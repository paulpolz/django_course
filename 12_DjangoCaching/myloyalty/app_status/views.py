from django.shortcuts import render
from django.views.generic.base import View
from app_status.models import Bonus, Offer, Purchase
from django.core.cache import cache


class PersonalAccount(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionError('You are not logged in')

        user = request.user

        special_offers_cache_key = 'special_offers:{}'.format(user)
        promo_events_cache_key = 'promo_events:{}'.format(user)

        # Если длина словаря 0, значит кэш пустой
        if len(cache.get_many([special_offers_cache_key, promo_events_cache_key])) == 0:
            special_offers = Offer.objects.filter(is_special_offer=True).all()
            promo_events = Offer.objects.filter(is_promo_event=True).all()

            cache_data = {
                special_offers_cache_key: special_offers,
                promo_events_cache_key: promo_events
            }
            
            cache.set_many(cache_data, 30*60)

        balance = Bonus.objects.get(user=user).balance
        purchases = Purchase.objects.filter(user=user).all()

        context={
            'balance': balance,
            'user': user,
            'special_offers': cache.get(special_offers_cache_key),
            'promo_events': cache.get(promo_events_cache_key),
            'purchases': purchases
        }

        return render(request, 'app_status/account.html', context=context)