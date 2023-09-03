from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from service.models import InteriorService
from service.models import ProjectCategory
from service.models import InteriorProjects
from service.models import ProjectImage
from service.models import HeroSection
from service.models import AboutSection
from service.models import OurPartner
from service.models import EnquiryData
from django.core.mail import send_mail

def homePage(request):

    service_data=InteriorService.objects.all()
    category=ProjectCategory.objects.all()
    project_list=InteriorProjects.objects.all()
    image_list=ProjectImage.objects.all()
    hero_data=HeroSection.objects.all()
    about_us_data=AboutSection.objects.all()
    our_partner_data=OurPartner.objects.all()
    data={'title':'Home',
          'bdata':'Welcome to Ragvi Design',
          'clist':{'Residential','Comercial'},
          'commercial_category':{'Showroom','office','Salon','Clinic','retail'},
          }
    
   # int_service_data=InteriorService.objects.all()
    #portfolio={
     #       'res': {'/img/portfolio/res-1.jpg','/img/portfolio/res-2.jpg','/img/portfolio/res-3.jpg','/img/portfolio/res-4.jpg','/img/portfolio/res-5.jpg'},
            #'office': {"office-1.jpg","office-2.jpg","office-3.jpg"},
            #'retail': {"retail-1.jpg","retail-2.jpg","retail-3.jpg"},
            #'salon': {"salon-1.jpg","salon-2.jpg","salon-3.jpg"},
               
      #        }
    
    portfolio={
            'residentail_img':[
                {'path': '/img/portfolio/res-1.jpg','name': 'Res-1'},
                {'path': '/img/portfolio/res-2.jpg','name': 'Res-2'},
                {'path': '/img/portfolio/res-3.jpg','name': 'Res-3'},
                {'path': '/img/portfolio/res-4.jpg','name': 'Res-4'},
                {'path': '/img/portfolio/res-5.jpg','name': 'Res-5'},
            ],
            'office_img':[
                {'path': '/img/portfolio/office-1.jpg','name': 'office-1'},
                {'path': '/img/portfolio/office-2.jpg','name': 'office-2'},
                {'path': '/img/portfolio/office-3.jpg','name': 'office-3'},
            ],
            'retail_img':[
                {'path': '/img/portfolio/retail-1.jpg','name': 'retail-1'},
                {'path': '/img/portfolio/retail-2.jpg','name': 'retail-2'},
                {'path': '/img/portfolio/retail-3.jpg','name': 'retail-3'},
            
            ],
            'salon_img':[
                {'path': '/img/portfolio/salon-1.jpg','name': 'salon-1'},
                {'path': '/img/portfolio/salon-2.jpg','name': 'salon-2'},
                {'path': '/img/portfolio/salon-3.jpg','name': 'salon-3'},
            ],
            'clinic_img':[
                {'path': '/img/portfolio/clinic-1.jpg','name': 'clinic-1'},
                {'path': '/img/portfolio/clinic-2.jpg','name': 'clinic-2'},
                {'path': '/img/portfolio/clinic-3.jpg','name': 'clinic-3'},
            ],
            'interior_service_data':service_data,
            'category':category,
            'project_list':project_list,
            'image_list':image_list,
            'hero_data':hero_data,
            'about_us_data':about_us_data,
            'our_partner_data':our_partner_data,
    }
    
    return render(request,"index.html",portfolio)

def aboutUs(request):
    service_data=InteriorService.objects.all()
    category=ProjectCategory.objects.all()
    project_list=InteriorProjects.objects.all()
    image_list=ProjectImage.objects.all()
    about_us_data=AboutSection.objects.all()
    portfolio={
            'interior_service_data':service_data,
            'category':category,
            'project_list':project_list,
            'image_list':image_list,
            'about_us_data':about_us_data,
    }
    return render(request,"about.html",portfolio)

def portfolio(request):
    service_data=InteriorService.objects.all()
    category=ProjectCategory.objects.all()
    project_list=InteriorProjects.objects.all()
    image_list=ProjectImage.objects.all()
    portfolio={
            'residentail_img':[
                {'path': '/img/portfolio/res-1.jpg','name': 'Res-1'},
                {'path': '/img/portfolio/res-2.jpg','name': 'Res-2'},
                {'path': '/img/portfolio/res-3.jpg','name': 'Res-3'},
                {'path': '/img/portfolio/res-4.jpg','name': 'Res-4'},
                {'path': '/img/portfolio/res-5.jpg','name': 'Res-5'},
            ],
            'office_img':[
                {'path': '/img/portfolio/office-1.jpg','name': 'office-1'},
                {'path': '/img/portfolio/office-2.jpg','name': 'office-2'},
                {'path': '/img/portfolio/office-3.jpg','name': 'office-3'},
            ],
            'retail_img':[
                {'path': '/img/portfolio/retail-1.jpg','name': 'retail-1'},
                {'path': '/img/portfolio/retail-2.jpg','name': 'retail-2'},
                {'path': '/img/portfolio/retail-3.jpg','name': 'retail-3'},
            
            ],
            'salon_img':[
                {'path': '/img/portfolio/salon-1.jpg','name': 'salon-1'},
                {'path': '/img/portfolio/salon-2.jpg','name': 'salon-2'},
                {'path': '/img/portfolio/salon-3.jpg','name': 'salon-3'},
            ],
            'clinic_img':[
                {'path': '/img/portfolio/clinic-1.jpg','name': 'clinic-1'},
                {'path': '/img/portfolio/clinic-2.jpg','name': 'clinic-2'},
                {'path': '/img/portfolio/clinic-3.jpg','name': 'clinic-3'},
            ],
            'interior_service_data':service_data,
            'category':category,
            'project_list':project_list,
            'image_list':image_list
    }
    
    return render(request,"portfolio.html",portfolio)

def services(request):
    service_data=InteriorService.objects.all()
    category=ProjectCategory.objects.all()
    project_list=InteriorProjects.objects.all()
    image_list=ProjectImage.objects.all()
    portfolio={
            'interior_service_data':service_data,
            'category':category,
            'project_list':project_list,
            'image_list':image_list
    }
    return render(request,"services.html",portfolio)

def contactUs(request):
    service_data=InteriorService.objects.all()
    category=ProjectCategory.objects.all()
    project_list=InteriorProjects.objects.all()
    image_list=ProjectImage.objects.all()
    portfolio={
            'interior_service_data':service_data,
            'category':category,
            'project_list':project_list,
            'image_list':image_list
    }
    return render(request,"contact.html",portfolio)

def saveEnquiry(request):
    # send_mail(
    # "Test mail for Enquiry",
    # "This is teat message for send enquiry",
    # "roshansetfly@gmail.com",
    # ["ragvidesign@gmail.com"],
    # fail_silently=False,
    # )

    save_status = ''
    try:
        if request.method=="POST":
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone_number=request.POST.get('telephone')
            subject=request.POST.get('subject')
            message=request.POST.get('message')
            save_status = 'Data Saved Successfully'
            model_data=EnquiryData(name=name,email=email,phone_number=phone_number,subject=subject,message=message)
            model_data.save()
            print(email)
    except:
     pass
     save_status = 'Data Not Saved'
    
    return render(request,"contact.html",{'status':save_status})
    