import os
from typing import Any, Dict

from django.contrib.sites import requests
from django.http import HttpResponseForbidden, FileResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from django.views.generic.edit import FormMixin

from Conf import settings
from app_pages import models
from app_pages import forms


class PortfolioView(FormMixin, ListView):
    template_name = 'index.html'
    model = models.PortfolioModel
    context_object_name = 'posts'
    form_class = forms.ContactForm

    def get_success_url(self):
        return reverse_lazy('pages:home')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()

            return self.form_valid(form)
        else:

            return self.form_invalid(form)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tech_skills'] = models.TechnicalSkillsModel.objects.all()
        context['pro_skills'] = models.ProfessionalSkillsModel.objects.all()
        context['tags'] = models.PortfolioTagModel.objects.all()
        context['clients'] = models.ClientModel.objects.all()
        context['educations'] = models.EducationModel.objects.all()
        context['works'] = models.WorkExperienceModel.objects.all()
        context['languages'] = models.WorkLanguageModel.objects.all()

        return context


# @require_POST
# @csrf_exempt
# def download_cv(request):
#     """
#     reCAPTCHA orqali CV faylini yuklash
#     """
#     print("\n" + "=" * 60)
#     print("📥 DOWNLOAD CV FUNKSIYASI CHAQIRILDI")
#
#     # 1. reCAPTCHA tokenini olish
#     recaptcha_response = request.POST.get('g-recaptcha-response', '').strip()
#     print(f"reCAPTCHA token: {'*' * 20 if recaptcha_response else 'YOQ'}")
#
#     # 2. Agar DEBUG rejimda bo'lsak, reCAPTCHA ni o'tkazib yuborish
#     DEBUG_MODE = getattr(settings, 'DEBUG', True)
#
#     if DEBUG_MODE:
#         print("🔧 DEBUG REJIM: reCAPTCHA tekshiruvi o'tkazildi")
#         recaptcha_valid = True
#     else:
#         # Haqiqiy reCAPTCHA tekshiruvi
#         if not recaptcha_response:
#             print("❌ reCAPTCHA tokeni yo'q")
#             return HttpResponseForbidden("reCAPTCHA tasdiqlanmadi!")
#
#         # Google reCAPTCHA tekshiruvi
#         recaptcha_data = {
#             'secret': getattr(settings, 'RECAPTCHA_SECRET_KEY', ''),
#             'response': recaptcha_response
#         }
#
#         try:
#             verify_response = requests.post(
#                 'https://www.google.com/recaptcha/api/siteverify',
#                 data=recaptcha_data,
#                 timeout=10
#             )
#             verify_result = verify_response.json()
#             recaptcha_valid = verify_result.get('success', False)
#
#             print(f"reCAPTCHA natija: {'✅ MUVOFAQQIYATLI' if recaptcha_valid else '❌ MUVAFFAQIYATSIZ'}")
#             if not recaptcha_valid:
#                 print("Xatolar:", verify_result.get('error-codes', []))
#
#         except Exception as e:
#             print(f"❌ reCAPTCHA server xatosi: {e}")
#             return HttpResponseForbidden("reCAPTCHA server bilan bog'lanishda xato")
#
#     # 3. Agar reCAPTCHA to'g'ri bo'lsa
#     if recaptcha_valid:
#         from .models import ResumeModel
#         resume = ResumeModel.objects.first()
#
#         if resume and resume.cv_file:
#             try:
#                 file_path = resume.cv_file.path
#                 print(f"📄 Fayl yo'li: {file_path}")
#
#                 # Fayl mavjudligini tekshirish
#                 if not os.path.exists(file_path):
#                     print(f"❌ Fayl yo'lida mavjud emas: {file_path}")
#                     return HttpResponseForbidden("CV fayli topilmadi")
#
#                 # Fayl nomi
#                 file_name = os.path.basename(file_path)
#                 if not file_name:
#                     file_name = "MuhammadAlis_resume.pdf"
#
#                 print(f"✅ Fayl mavjud. Yuklanmoqda: {file_name}")
#
#                 # FileResponse qaytarish
#                 response = FileResponse(
#                     open(file_path, 'rb'),
#                     as_attachment=True,
#                     filename=file_name
#                 )
#                 response['Content-Type'] = 'application/pdf'
#                 print("🎉 Fayl yuklashga tayyor!")
#                 return response
#
#             except FileNotFoundError:
#                 print(f"❌ Fayl topilmadi: {file_path}")
#                 return HttpResponseForbidden("CV fayli topilmadi")
#             except Exception as e:
#                 print(f"❌ Xato: {str(e)}")
#                 return HttpResponseForbidden(f"Faylni ochishda xato: {str(e)}")
#         else:
#             print("❌ CV ma'lumotlari topilmadi")
#             return HttpResponseForbidden("CV topilmadi. Iltimos, admin panel orqali CV yuklang.")
#     else:
#         print("❌ reCAPTCHA tasdiqlanmadi")
#         return HttpResponseForbidden("reCAPTCHA tasdiqlanmadi!")

def download_cv(request):
    """
    CV ni yuklab olish uchun view funksiyasi
    """
    if request.method == 'POST':
        # 1. reCAPTCHA tekshirish
        recaptcha_response = request.POST.get('g-recaptcha-response')

        if not recaptcha_response:
            return JsonResponse({
                'error': 'Please complete the captcha'
            }, status=400)

        # 2. reCAPTCHA validatsiyasi (ixtiyoriy)
        # Agar reCAPTCHA kerak bo'lsa:
        """
        recaptcha_secret = "YOUR_RECAPTCHA_SECRET_KEY"
        data = {
            'secret': recaptcha_secret,
            'response': recaptcha_response
        }

        # Google ga so'rov yuborish
        response = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data=data
        )

        result = response.json()

        if not result.get('success'):
            return JsonResponse({
                'error': 'Captcha verification failed'
            }, status=400)
        """

        # 3. CV faylini topish
        cv_filename = "MuhammadAlis_resume.pdf"

        # Birinchi static papkada qidirish
        static_path = os.path.join(settings.STATIC_ROOT, 'resume', cv_filename)

        # Agar STATIC_ROOT da yo'q bo'lsa, STATICFILES_DIRS da qidirish
        if not os.path.exists(static_path):
            for static_dir in settings.STATICFILES_DIRS:
                test_path = os.path.join(static_dir, 'resume', cv_filename)
                if os.path.exists(test_path):
                    static_path = test_path
                    break

        # 4. Agar static da topilmasa, media papkasida qidirish
        if not os.path.exists(static_path):
            media_path = os.path.join(settings.MEDIA_ROOT, 'resume', cv_filename)
            if os.path.exists(media_path):
                static_path = media_path

        # 5. Faylni tekshirish
        if not os.path.exists(static_path):
            return JsonResponse({
                'error': 'CV file not found on server'
            }, status=404)

        # 6. PDF faylni yuborish
        try:
            response = FileResponse(
                open(static_path, 'rb'),
                content_type='application/pdf'
            )

            # Yuklab olish uchun sozlash
            response['Content-Disposition'] = f'attachment; filename="MuhammadAli_Abdusattorov_CV.pdf"'

            # Cache control
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'

            return response

        except Exception as e:
            return JsonResponse({
                'error': f'Error reading file: {str(e)}'
            }, status=500)

    # Agar GET so'rov bo'lsa
    else:
        return JsonResponse({
            'error': 'Method not allowed. Use POST.'
        }, status=405)