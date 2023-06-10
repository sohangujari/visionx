from django.shortcuts import render
from openjourney import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        # Retrieve the text input from the form
        prompt_text = request.POST.get('text_input')

        image_data = modelx(prompt_text)

        image_url = image_data.save("visionxai.png")

        image_vision = image_url.show("visionxai.png")

        # Render the result template with the image data
        return render(request, 'result.html', {'image_data': image_vision})
    
    # Render the input template initially
    return render(request, 'index.html')