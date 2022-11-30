import zipfile
from io import BytesIO

from celery import shared_task
from django.http import HttpResponse
# pdf creation
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# model
from apps.post.models import PostModel

from django.core.files import File
from apps.post.models import PostModel
import os
from fpdf import FPDF


@shared_task(name='task.generate_pdf')
def generate_pdf():
    print("__________inside celery download all pdfs task______")
    events = PostModel.objects.all()
    for event in events:
        print(event.id)
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
        print(BASE_DIR)
        pdf.output(BASE_DIR + '/media/event_pdf/' + str(event.id) + ".pdf")
        field = BASE_DIR + '/media/event_pdf/' + str(event.id) + ".pdf"
        print("??????????????", field)
        PostModel.objects.filter(id=event.id).update(download_file=field)

    return HttpResponse("success")


"""
@shared_task(name='task.generate_pdf')
def generate_pdf():
    print("__________inside celery download all pdfs task______")
    events = PostModel.objects.all()
    for event in events:
        print(event.id)
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=A4)
        p.drawString(260, 800, "POST DETAIL PRINT")
        p.line(5, 780, 590, 780)  # drawing a line starting and ending coordinates given (0 to 600 is width A4 paper)
        x1 = 20
        y1 = 750
        data = PostModel.objects.filter(id=event.id).values('event_title', 'event_date', 'content', 'location')[0]
        for key, val in data.items():  # data is a dictionary or kwargs
            p.drawString(x1, y1, f"{key}   -  {val}")
            print(key, val)
            y1 = y1 - 60
        p.showPage()
        p.save()  ##
        # p.setTitle(data.get('event_title'))
        buffer.seek(0)
        ######
        pdf = FPDF()
        pdf.add_page()
        # set font style and size for pdf
        pdf.set_font('Arial', size=16)
        # creating cell
        pdf.cell(200, 10, txt="Trial to generate a pdf file.", ln=2, align='C')
        # save file with extension
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # /Users/bibinkunjumon/PycharmProjects/eventPlannerWeb
        print(BASE_DIR)
        pdf.output(BASE_DIR+'/media/event_pdf/'+str(event.id) + ".pdf")
        #######
        print(buffer,str(event.id))
        field = File(buffer, name=(str(event.id) + ".pdf"))
        #field = File(buffer,name=(data.get("event_title"))+ ".pdf")
        PostModel.objects.filter(id=event.id).update(download_file=field)
        #PostModel.objects.create(user_id=event.id,download_file=field)

        # Set the mime type
        #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename= name=str(event.id) + ".pdf"
        filepath = BASE_DIR + '/media/event_pdf/' + filename
        mime_type, _ = mimetypes.guess_type(filepath)

    return FileResponse(buffer, as_attachment=True, filename=data.get('event_title'),content_type=mime_type)



def generate_pdfOne(request, *args, **kwargs):
    print("__________inside celery task______")
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    p.drawString(260, 800, "POST DETAIL PRINT")
    p.line(5, 780, 590, 780)  # drawing a line starting and ending coordinates given (0 to 600 is width A4 paper)
    x1 = 20
    y1 = 750
    data = PostModel.objects.filter(id=kwargs.get('pk')).values('event_title', 'event_date', 'content', 'location')[0]
    print(data)
    for key, val in data.items():#data is a dictionary or kwargs
        p.drawString(x1, y1, f"{key}   -  {val}")
        y1 = y1 - 60
    p.showPage()
    p.save()
    # p.setTitle(data.get('event_title'))
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=data.get('event_title'))"""
