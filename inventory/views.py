from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
import qrcode
from io import BytesIO
from django.http import HttpResponse
from .models import Equipment
from django.views.generic import ListView
from .models import Equipment
from django.shortcuts import render, redirect
from .forms import EquipmentForm
# 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
import openai
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import openai
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


from bs4 import BeautifulSoup
#import fitz  # PyMuPDF



from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from bs4 import BeautifulSoup
  # PyMuPDF
import requests



class EquipmentListView(ListView):
    model = Equipment
    template_name = 'equipment_list.html'
    context_object_name = 'equipment_list'

class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = 'equipment_detail.html'
    context_object_name = 'equipment'

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        data = f"ID: {self.object.unique_identifier}\nName: {self.object.name}\nDate Registered: {self.object.date_registered}"
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        return buffer.getvalue()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        response = HttpResponse(content_type='image/png')
        response['Content-Disposition'] = f'attachment; filename="qr_{self.object.unique_identifier}.png"'
        buffer = self.generate_qr_code()
        response.write(buffer)
        return response


def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:equipment-list')
    else:
        form = EquipmentForm()
    
    context = {'form': form}
    return render(request, 'inventory/add_equipment.html', context)



### this chatbot helps especially in coding and indexing of diseases icd 10 etc
class ChatbotView(View):
    # Add your OpenAI API key here
    OPENAI_API_KEY = ''

    template_name = 'inventory/chatgpt.html'  # Template name

    preloaded_messages = {
        'hello': 'Welcome to Joytech Healthcare! How can I assist you?',
        'company_info': 'Our company provides a wide range of healthcare solutions.',
        'product_info': 'You can find detailed information about our products on our website: https://www.joytechhealthcare.com/products',
        'contact_info': 'You can reach our customer support team at support@joytechhealthcare.com.',
        'pdf_info': 'Sure, here is the link to our company brochure: [Company Brochure](https://www.researchgate.net/publication/328701401_FULL_THESIS)',
        'website_info': 'Sure, here is the link to our product information page: [Product Info](https://www.joytechhealthcare.com/products)',
        # Add more predefined messages as needed
    }

    @method_decorator(csrf_exempt)  # Disable CSRF protection for this view
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def extract_text_from_pdf(self, pdf_url):
        # ... (your existing code)
        try:
            pdf_document = fitz.open(pdf_url)
            text = ''
            for page_num in range(pdf_document.page_count):
                page = pdf_document.load_page(page_num)
                text += page.get_text()
            pdf_document.close()
            return text
        except Exception as e:
            print('Error extracting text from PDF:', e)
            return 'Sorry, there was an error extracting the text from the PDF.'

    def extract_text_from_webpage(self, webpage_url):
        try:
            response = requests.get(webpage_url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the main content element based on class or id
            main_content = soup.find('div', class_='mw-parser-output')
            if not main_content:
                return 'Unable to extract content from the webpage.'

            # Extract text from the main content
            text = ''
            for paragraph in main_content.find_all('p'):
                text += paragraph.get_text() + '\n'

            return text
        except Exception as e:
            print('Error extracting text from webpage:', e)
            return 'Sorry, there was an error extracting the text from the webpage.'


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        user_message = request.POST.get('message', '').strip()

        if user_message == '':
            return JsonResponse({'response': 'No response'})

        # Check if the user's message matches a predefined prompt
        if user_message in self.preloaded_messages:
            chatbot_response = self.preloaded_messages[user_message]
        elif user_message == 'pdf_info':
            pdf_url = 'https://www.researchgate.net/publication/328701401_FULL_THESIS'
            pdf_text = self.extract_text_from_pdf(pdf_url)
            chatbot_response = pdf_text
        elif user_message == 'website_info':
            webpage_url = 'https://en.wikipedia.org/wiki/Tesla,_Inc.'
            webpage_text = self.extract_text_from_webpage(webpage_url)
            chatbot_response = webpage_text
        else:
            chatbot_response = 'I apologize, but I am unable to answer that question at the moment.'

        return JsonResponse({'response': chatbot_response})



