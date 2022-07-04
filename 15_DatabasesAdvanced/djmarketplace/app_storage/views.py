from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from app_storage.models import Good, Article, Cart, Order
from app_loyalty.models import Balance, BalanceStatus
from app_storage.forms import CartAddStockForm, CreateOrderButtonForm
from django.db import transaction
from django.contrib import messages


class ShowcaseListView(ListView):
    model = Article
    template_name = 'app_storage/showcase.html'
    context_object_name = 'showcase'
    queryset = Article.objects.select_related('good').select_related('store').all()


class ShowCaseDetailView(DetailView):
    model = Article
    template_name = 'app_storage/good.html'
    context_object_name = 'good'

    def get_context_data(self, **kwargs):
        context = super(ShowCaseDetailView, self).get_context_data()
        context['cartadd_stock_form'] = CartAddStockForm()

        return context

    def post(self, request, pk):
        cartadd_stock = CartAddStockForm(request.POST)
        user = request.user
        good = super(ShowCaseDetailView, self).get_object()
        cart = Cart.objects.filter(user=user).select_related('article').all()

        with transaction.atomic():
            if cartadd_stock.is_valid():
                # Проверяем, достаточно ли стока на товаре, чтобы добавить его в корзину
                if not good.stock >= cartadd_stock.cleaned_data['stock']:
                    messages.success(request, 'Good is run out of stock, you can add to cart only {} pcs.'.format(good.stock))
                    return HttpResponseRedirect('/good/'+str(good.article_id))

                try:
                    # изменить кол-во товара в корзине
                    current_cart_good = cart.get(article=good.article_id)
                    current_cart_good.quantity += cartadd_stock.cleaned_data['stock']
                    current_cart_good.save()
                except:
                    # если товара в корзине нет, то создать новую запись
                    Cart.objects.create(
                        user=user,
                        article=good,
                        quantity=cartadd_stock.cleaned_data['stock']
                    )
                # изменить сток добавленного в корзину товара
                good.stock -= cartadd_stock.cleaned_data['stock']
                good.save()

        return HttpResponseRedirect('/cart')


class CartView(View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        cart = Cart.objects.filter(user=user).select_related('article').all()
        create_order_button_form = CreateOrderButtonForm()

        cart_total_sum = 0
        for row in cart:
            row.sum_price = row.article.price * row.quantity
            cart_total_sum += row.sum_price
            row.save()

        query_params = {
            'cart': cart,
            'cart_total_sum': cart_total_sum,
            'create_order_button_form': create_order_button_form,
        }

        return render(request, 'app_storage/cart.html', query_params)

    def post(self, request):
        user = self.request.user
        cart = Cart.objects.filter(user=user).select_related('article').all()
        bonus_account = Balance.objects.get(user_id=user)

        with transaction.atomic():
            # Рассчитываем стомость корзины для списания и списываем товар со стока
            cart_total_sum = 0
            for row in cart:
                Order.objects.create(
                    user=user,
                    article=row.article,
                    quantity=row.quantity,
                    price=row.quantity * row.article.price
                )
                cart_total_sum += row.quantity * row.article.price # стоимость корзины
                row.article.stock -= row.quantity # сток

            # Проверяем, что на счете достаточно средств
            if not bonus_account.balance >= cart_total_sum:
                messages.success(request, 'Insufficient funds on your account')
                return HttpResponseRedirect('/cart/')

            # После проверки списываем сумму заказа со счета
            bonus_account.balance -= cart_total_sum
            bonus_account.save()
            cart.delete()

            # Получаем таблицу статусов
            balanse_statuses = BalanceStatus.objects.all()

            # Если у юзера максимальный статус, то больше повышений не производится
            if bonus_account.status == 'Best friend':
                pass
            # Если статус не максимальый, то вычисляем, какой статус нужно назначить
            else:
                total_check = 0
                orders = Order.objects.filter(user=user).select_related('article').all()
                for order in orders:
                    total_check += order.article.price * order.quantity

                # Если сумма покупок от 500$ до 2000$, то назначаем статус Friend
                if total_check > 500 and total_check <= 2000:
                    bonus_account.status = balanse_statuses.get(status='Friend')
                    bonus_account.save()
                # Если сумма покупок выше 2000$, то назначаем статус Best friend
                elif total_check > 2000:
                    bonus_account.status = balanse_statuses.get(status='Best friend')
                    bonus_account.save()

        return HttpResponseRedirect('/account')