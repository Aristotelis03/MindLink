from django import forms
from .models import Post, Comments

# class CustomClearableFileInput(forms.ClearableFileInput):
#     def get_template_substitution_values(self, value):
#         return {
#             'initial': self.initial_text,
#             'input_text': 'Picture',  # Change this text
#             'clear_template': '',
#             'clear_checkbox_label': self.clear_checkbox_label,
#         }
    
class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'picture', 'video']
# class CreatePostForm(forms.Form):
    # content = forms.CharField(
    #     widget=forms.Textarea(attrs={'placeholder': 'Enter your content here...'}),
    # )
    # picture = forms.ImageField(required=False)
    # video = forms.FileField(required=False)

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     # Add custom validation logic for the 'name' field if needed
    #     return name
    # class Meta: 
    #     model = Post
    #     fields = ['content', 'picture', 'video']

class CreateCommentForm(forms.ModelForm):
    post_id = forms.IntegerField(widget=forms.HiddenInput())
    comment = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Comments
        fields = ['comment','post_id']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the rendering of each field if needed
        self.fields['comment'].widget.attrs.update({'class': 'form-control','placeholder':'Comment'})
        self.fields['post_id'].widget.attrs.update({'class': 'form-control'})


