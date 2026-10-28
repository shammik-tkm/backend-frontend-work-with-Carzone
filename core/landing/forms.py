from django import forms
from .models import GalleryCategory, GalleryItem

class GalleryItemForm(forms.ModelForm):
    class Meta:
        model = GalleryItem
        fields = ['title', 'category', 'badge_text', 'description', 'image_before', 'image_after', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-3 bg-[#08090c] border border-brand-border rounded-xl text-white text-sm focus:outline-none focus:border-brand-orange'}),
            'category': forms.Select(attrs={'class': 'w-full px-4 py-3 bg-[#08090c] border border-brand-border rounded-xl text-white text-sm focus:outline-none focus:border-brand-orange'}),
            'badge_text': forms.TextInput(attrs={'class': 'w-full px-4 py-3 bg-[#08090c] border border-brand-border rounded-xl text-white text-sm focus:outline-none focus:border-brand-orange'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-4 py-3 bg-[#08090c] border border-brand-border rounded-xl text-white text-sm focus:outline-none focus:border-brand-orange', 'rows': 3}),
            'image_before': forms.FileInput(attrs={'class': 'w-full text-slate-400 text-sm'}),
            'image_after': forms.FileInput(attrs={'class': 'w-full text-slate-400 text-sm'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'w-5 h-5 accent-brand-orange'}),
        }