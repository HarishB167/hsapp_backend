from django.contrib import admin
from mindmaps.models import Branch, BranchLine, Mindmap


class BranchInline(admin.TabularInline):
    autocomplete_fields = ['mindmap']
    min_num = 1
    max_num = 10
    model = Branch
    extra = 0

class BranchLineInline(admin.TabularInline):
    autocomplete_fields = ['branch']
    min_num = 1
    model = BranchLine
    extra = 0

# Register your models here.
@admin.register(Mindmap)
class MindmapAdmin(admin.ModelAdmin):
    inlines = [BranchInline]
    search_fields = ['title']
    class Meta:
        list_display = ['title', 'category', 'revisions']
    

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    inlines = [BranchLineInline]
    search_fields = ['title']
    class Meta:
        list_display = ['title']

@admin.register(BranchLine)
class BranchLineAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ['content']

