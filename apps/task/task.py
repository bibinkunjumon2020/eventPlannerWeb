from uuid import uuid4

from celery import shared_task
from django.http import HttpResponse
from apps.post.models import PostModel
import os
from fpdf import FPDF


@shared_task(name='task.generate_pdf')
def generate_pdf():
    print("__________inside celery download all pdfs task______")
    events = PostModel.objects.all()
    for event in events:
        x1 = 100
        y1 = 20
        pdf = FPDF()
        pdf.add_page()
        # set font style and size for pdf
        pdf.set_font('Arial', size=16)
        pdf.cell(200, 10, txt="POST DETAIL PRINT", ln=1, align='C')
        data = PostModel.objects.filter(id=event.id).values('event_title', 'event_date', 'content', 'location')[0]
        for key, val in data.items():  # data is a dictionary or kwargs
            pdf.cell(x1, y1, txt=f"{key}   -  {val}", ln=1)
            print(key, val)
        # save file with extension
        BASE_DIR = os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))))  # /Users/bibinkunjumon/PycharmProjects/eventPlannerWeb
        #creating file name and saving - basedir+the dir we want+ random name.
        file_name = BASE_DIR + '/media/event_pdf/' + uuid4().hex + str(event.id) + ".pdf"
        # pdf.output(BASE_DIR + '/media/event_pdf/' + str(event.id) + ".pdf")
        pdf.output(file_name)
        # field = BASE_DIR + '/media/event_pdf/' + str(event.id) + ".pdf"

        print("file path", file_name)
        PostModel.objects.filter(id=event.id).update(download_file=file_name) # latest name to model

    return HttpResponse("success")
