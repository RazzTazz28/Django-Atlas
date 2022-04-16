from django import forms
from django.core.files.images import get_image_dimensions
from django.forms import ModelForm
from .models import UserProfile


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:
            '''w, h = get_image_dimensions(avatar)

            # validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                    '%s x %s pixels or smaller.' % (max_width, max_height))'''

            # validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                                            'GIF or PNG image.')

            # validate file size
            if len(avatar) > (100 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 100k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar