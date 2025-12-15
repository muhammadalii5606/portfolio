from django.contrib import admin
from .models import PortfolioModel,PortfolioTagModel,TechnicalSkillsModel,ProfessionalSkillsModel,ContactModel,ClientModel,EducationModel,WorkExperienceModel,WorkLanguageModel

@admin.register(PortfolioModel)
class PortfolioModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'language', 'description')
    search_fields = ('title', 'language')
    list_filter = ('language',)
    ordering = ('id',)

@admin.register(TechnicalSkillsModel)
class TechnicalSkillsModelAdmin(admin.ModelAdmin):
    list_display = ('lang','value',)
    search_fields = ('lang',)
    list_filter = ('lang',)

@admin.register(ProfessionalSkillsModel)
class TechnicalSkillsModelAdmin(admin.ModelAdmin):
    list_display = ('title','value',)
    search_fields = ('title',)
    list_filter = ('title',)

@admin.register(PortfolioTagModel)
class PortfolioTagModelAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('first_name','email','created_at',)
    search_fields = ('first_name','last_name','email','message',)
    list_filter = ('email','created_at',)

@admin.register(ClientModel)
class ClientModelAdmin(admin.ModelAdmin):
    list_display = ('name','job',)
    search_fields = ('name','job','description',)
    list_filter = ('name',)

@admin.register(EducationModel)
class EducationModelAdmin(admin.ModelAdmin):
    list_display = ('name','year',)
    search_fields = ('name','year','description',)
    list_filter = ('name','year',)

@admin.register(WorkExperienceModel)
class WorkExperienceModelAdmin(admin.ModelAdmin):
    list_display = ('name','year',)
    search_fields = ('name','year','languages',)
    list_filter = ('name',)

@admin.register(WorkLanguageModel)
class WorkLanguageModelAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)