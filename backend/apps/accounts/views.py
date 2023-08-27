from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseBadRequest, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class Login(TemplateView):
    model = template_name = "accounts/login.html"


class Logout(LogoutView):
    next_page = reverse_lazy("login")


def ajax_login(request):
    data = {"redirect": reverse_lazy("login")}

    if request.is_ajax():
        ...
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        if email and password:
            # Test email/password combination
            user = authenticate(email=email, password=password)
            # Found a match
            if user is not None:
                # User is active
                if user.is_active:
                    # Officially log the user in
                    login(request, user)
                    data["success"] = True
                    data["redirect"] = reverse_lazy("admin:index")
                else:
                    data["success"] = False
                    data["error"] = "Usuário não esta ativo"
            else:
                data["success"] = False
                data["error"] = "Email e/ou senha errados"

            return JsonResponse(data, safe=True)

    # Request method is not POST or one of email or password is missing
    return HttpResponseBadRequest()


def ajax_logout(request):
    data = {"redirect": reverse_lazy("login")}

    if request.user.is_authenticated:
        logout(request)
        data["success"] = True

    else:
        data["success"] = False

    return JsonResponse(data)
    return JsonResponse(data)
