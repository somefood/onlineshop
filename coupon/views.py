from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone # 서버, 국가에 맞게 적용하기 위해 사용
from django.views.decorators.http import require_POST
from .models import Coupon
from .forms import AddCouponForm


@require_POST
def add_coupon(request):
    now = timezone.now()
    form  = AddCouponForm(request.POST)

    if form.is_valid():
        code = form.cleaned_data['code'] # request.POST.get() 이렇게도 할 수 있으나, 위험하기에 form을 만들어서 해주자

        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        use_from__lte=now, use_to__gte=now, active=True) # 대소문자 가리지 않고 일치하는거
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None

    return redirect('cart:detail')



