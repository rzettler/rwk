from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model

from .models import RWK_Mannschaft
from .models import RWK_Schuetze
from .models import RWK_Eintrag
from .models import RWK_Einzahlung

class MannschaftForm(forms.ModelForm):

    class Meta:
        model = RWK_Mannschaft
        fields = ('name',)
		
class SchuetzeForm(forms.ModelForm):

    class Meta:
        model = RWK_Schuetze
        fields = ('name',)
		
class EintragForm(forms.ModelForm):

    class Meta:
        model = RWK_Eintrag
        fields = ('rwk_schuetze', 'rwk_mannschaft', 'fight_date' , 'ringe', 'anzahl_8er', 'anzahl_7er', 'anzahl_6er', 'anzahl_5er', 'anzahl_4er', 'anzahl_3er', 'anzahl_2er', 'anzahl_1er', 'anzahl_0er', )
		
class EinzahlungForm(forms.ModelForm):

    class Meta:
        model = RWK_Einzahlung
        fields = ('rwk_schuetze', 'betrag', 'tag_der_einzahlung')
		
User = get_user_model()
class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	
	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("This user does not exist")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect password")
			if not user.is_active:
				raise forms.ValidationError("This user is no longer active")
		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'password')
