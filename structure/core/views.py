from flask import render_template,request,Blueprint,session,redirect,url_for
# from structure.models import User,app,PaymentMethod,Payment
# from structure.team.views import team
from sqlalchemy.orm import load_only
from flask_login import login_required
# from structure.core.forms import QRCodeData,PaymentMethodForm
import secrets
from structure import db
# import qrcode
# import random
# import requests
# import json
# import uuid Passw0rd@100




core = Blueprint('core',__name__)

@core.route('ussd')
def ussd(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        print("...")
        print("number")
        print(phone_number)
        response = ""    
        if text == "":
            response = "CON Welcome to our News subscription service \n"
            response += "1. Sport \n"
            response += "2. political \n"
            response += "3. Local  \n"
            response += "4. International"    
        elif text == "1":
            response = "CON Select Your Preferred Sport Plans \n"
            response += "1. Daily @ N100 \n"
            response += "2. Weekly @ N50 \n"
            response += "3. Monthly @ N25 "    
        elif text == "1*1":
            response = "CON You will be charged N100 for your Daily Sports news subscription \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"
        elif text == "1*1*1":
            response = "END thank you for subscribing to our daily sport news plan \n"
        elif text == "1*1*2":
            response = "END thank you for your one-off daily sport news plan \n"    
        elif text == "1*2":
            response = "CON You will be charged N50 for our weekly Sports news plan \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"
        elif text == "1*2*1":
            response = "END thank you for subscribing to our weekly sport news plan \n"
        elif text == "1*2*2":
            response = "END thank you for your one-off weekly sport news plan \n"    
        elif text == "1*3":
            response = "CON You will be charged N25 for our monthly Sports news plan \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"
        elif text == "1*3*1":
            response = "END thank you for subscribing to our monthly sport news plan \n"
        elif text == "1*3*2":
            response = "END thank you for your one-off monthly sport news plan \n"
        print("response:")
        print(response)
        return response
        