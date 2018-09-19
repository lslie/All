from django import forms
import re
from .models import UserProFile

#限制字段验证功能的forms
class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=20,required=True)
    email = forms.EmailField(max_length=100)
    url = forms.URLField(max_length=100,min_length=8)
    password = forms.CharField(max_length=20,required=True)
    password1 = forms.CharField(max_length=20,required=True)

    #定制验证错误消息
    def clean_username(self):
        username = self.cleaned_data['username']
        #创建一个正则对象com
        com = re.compile('\d+')
        if not com.match(username):
            return username
        else:
            #抛出异常错误
            raise forms.ValidationError('username不合法',code='invalid username')
#
# class UserRegisterForm(forms.ModelForm):
#     username = forms.CharField(max_length=20, min_length=6, required=True)
#     password = forms.CharField(max_length=20, min_length=8, required=True)
#     password1 = forms.CharField(max_length=20, min_length=8, required=True)
#       实例化userProfile，fields里面填写的是我们需要限制条件的字段
#     class Meta():
#         model = UserProFile
#         fields = ['username','password','email','url']

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20,required=True)
    password = forms.CharField(max_length=28,required=True)
