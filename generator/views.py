from django.shortcuts import render
from django.http import HttpResponse
from .forms import Generator

import wifi_qrcode_generator
import qrcode
import qrcode.image.svg
from io import BytesIO


# Create your views here.


def generate(request, wifi_name, password, encryption):
    wifi_info = f"WIFI:T:{encryption}; S:{wifi_name}; P:{password};;"
    qr = qrcode.make(wifi_info)
    response = HttpResponse(content_type='image/png')
    qr.save(response)
    return response








# def generate(request):
#     if request.method == "POST":
#         form = Generator(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
#             #     ssid=form['wifi_name'], hidden=False, authentication_type=form['encryption'], password=form['password']
#             # )
#             # qr_code.print_ascii()
#             # qr_code.make_image().save('qr.png')
#             # qr = qrcode.make(form)
#             # response = HttpResponse(content_type="image/png")
#             # qr.save(response)
#     else:
#         form = Generator()
#     return render(request, 'generator/index.html', {'form': form})


# def img(request):
#     ok = QrCode()
#     qr = wifi_qrcode_generator.generator.wifi_qrcode(ssid=ok.wifi_name, hidden=False, authentication_type=ok.encryption,
#                                                      password=ok.password)
#     qr.print_ascii()
#     qr.make_image().save('qr.png')
#
#     return render(request, 'generator/ok.html', {'ok': ok.objects.all()})
