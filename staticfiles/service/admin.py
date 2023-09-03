from django.contrib import admin
from service.models import InteriorService
from service.models import ProjectCategory
from service.models import InteriorProjects
from service.models import ProjectImage
from service.models import HeroSection
from service.models import AboutSection
from service.models import OurPartner
from service.models import EnquiryData
class InteriorServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_heading','service_desc')
admin.site.register(InteriorService,InteriorServiceAdmin)

class ProjectCategoryAdmin(admin.ModelAdmin):
    category_display=('category')
admin.site.register(ProjectCategory,ProjectCategoryAdmin)

class InteriorProjectsAdmin(admin.ModelAdmin):
    project_display=('category','name','short_address','description','project_value','cover_image')
admin.site.register(InteriorProjects,InteriorProjectsAdmin)

class ProjectImageAdmin(admin.ModelAdmin):
    image_display=('project','image')
admin.site.register(ProjectImage,ProjectImageAdmin)

class HeroSectionAdmin(admin.ModelAdmin):
    hero_display=('heading','description','image')
admin.site.register(HeroSection,HeroSectionAdmin)

class AboutSectionAdmin(admin.ModelAdmin):
    about_display=('title','heading','title','about_me','about_me_more')
admin.site.register(AboutSection,AboutSectionAdmin)

class OurPartnerAdmin(admin.ModelAdmin):
    about_display=('name','logo')
admin.site.register(OurPartner,OurPartnerAdmin)

class EnquiryDataAdmin(admin.ModelAdmin):
    enquiry_display=('name','email','phone_number','subject','message')
admin.site.register(EnquiryData,EnquiryDataAdmin)


# Register your models here.
