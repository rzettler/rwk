from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .models import RWK_Mannschaft
from .models import RWK_Schuetze
from .models import RWK_Eintrag
from .models import RWK_Einzahlung
from .forms import MannschaftForm
from .forms import SchuetzeForm
from .forms import EintragForm
from .forms import EinzahlungForm
from .forms import UserForm
from .forms import UserLoginForm

# Create your views here.

def home(request):
    rwk_schuetzen = RWK_Schuetze.objects.all()
    betraege = {}
    for schuetze in rwk_schuetzen:
        eintraege = RWK_Eintrag.objects.filter(rwk_schuetze=schuetze)
        einzahlungen = RWK_Einzahlung.objects.filter(rwk_schuetze=schuetze)
        betrag = 0
        for entry in einzahlungen:
            betrag = betrag + entry.betrag
        for entry in eintraege:
            betrag = betrag - entry.betrag
        betraege[schuetze] = betrag
    return render(request, 'rwkapp/start.html', {'betraege':betraege})

def eintraege_list(request):
    rwk_eintraege = RWK_Eintrag.objects.all()
    return render(request, 'rwkapp/eintraege_list.html', {'rwk_eintraege': rwk_eintraege})

def eintraege_detail(request, pk):
    eintrag = get_object_or_404(RWK_Eintrag, pk=pk)
    return render(request, 'rwkapp/eintraege_detail.html', {'eintrag': eintrag})

@login_required(login_url='login')
def eintrag_new(request):
    if request.method == "POST":
        form = EintragForm(request.POST)
        if form.is_valid():
            eintrag = form.save(commit=False)
            eintrag.created_date = timezone.now()
            eintrag.created_by = request.user
            eintrag.betrag=eintrag.anzahl_8er*0.25+eintrag.anzahl_7er*0.5+eintrag.anzahl_6er*0.75+eintrag.anzahl_5er*1.0+eintrag.anzahl_4er*1.25+eintrag.anzahl_3er*1.5+eintrag.anzahl_2er*1.75+eintrag.anzahl_1er*2.0+eintrag.anzahl_0er*2.25
            if eintrag.ringe < 375:
                eintrag.betrag = eintrag.betrag + 1.0
            if eintrag.betrag > 5.0:   #Top-Stopp
                eintrag.betrag = 5.0		
            eintrag.save()
            return redirect('eintraege_detail', pk=eintrag.pk)
    else:
        form = EintragForm()
    return render(request, 'rwkapp/eintrag_new.html', {'form': form})
	
def schuetzen_list(request):
    rwk_schuetzen = RWK_Schuetze.objects.all()
    return render(request, 'rwkapp/schuetzen_list.html', {'rwk_schuetzen': rwk_schuetzen})

def schuetzen_detail(request, pk):
    schuetze = get_object_or_404(RWK_Schuetze, pk=pk)
    return render(request, 'rwkapp/schuetzen_detail.html', {'schuetze': schuetze})

@login_required(login_url='login')
def schuetze_new(request):
    if request.method == "POST":
        form = SchuetzeForm(request.POST)
        if form.is_valid():
            schuetze = form.save(commit=False)
            schuetze.created_date = timezone.now()
            schuetze.save()
            return redirect('schuetzen_detail', pk=schuetze.pk)
    else:
        form = SchuetzeForm()
    return render(request, 'rwkapp/schuetze_new.html', {'form': form})

def mannschaft_list(request):
    rwk_mannschaften = RWK_Mannschaft.objects.all()
    return render(request, 'rwkapp/mannschaft_list.html', {'rwk_mannschaften': rwk_mannschaften})

def mannschaft_detail(request, pk):
    mannschaft = get_object_or_404(RWK_Mannschaft, pk=pk)
    return render(request, 'rwkapp/mannschaft_detail.html', {'mannschaft': mannschaft})

@login_required(login_url='login')
def mannschaft_new(request):
    if request.method == "POST":
        form = MannschaftForm(request.POST)
        if form.is_valid():
            mannschaft = form.save(commit=False)
            mannschaft.created_date = timezone.now()
            mannschaft.save()
            return redirect('mannschaft_detail', pk=mannschaft.pk)
    else:
        form = MannschaftForm()
    return render(request, 'rwkapp/mannschaft_new.html', {'form': form})
	
def einzahlungen_list(request):
    rwk_einzahlungen = RWK_Einzahlung.objects.all()
    return render(request, 'rwkapp/einzahlungen_list.html', {'rwk_einzahlungen': rwk_einzahlungen})

def einzahlung_detail(request, pk):
    einzahlung = get_object_or_404(RWK_Einzahlung, pk=pk)
    return render(request, 'rwkapp/einzahlung_detail.html', {'einzahlung': einzahlung})

@login_required(login_url='login')
def einzahlung_new(request):
    if request.method == "POST":
        form = EinzahlungForm(request.POST)
        if form.is_valid():
            einzahlung = form.save(commit=False)
            einzahlung.created_date = timezone.now()
            einzahlung.created_by = request.user
            einzahlung.save()
            return redirect('einzahlung_detail', pk=einzahlung.pk)
    else:
        form = EinzahlungForm()
    return render(request, 'rwkapp/einzahlung_new.html', {'form': form})
	
class UserFormView(View):
	form_class = UserForm
	template_name = 'rwkapp/reg_form.html'
	
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('/login/?next=%s' % (request.path))
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})
	
	def post(self, request):
		if not request.user.is_authenticated:
			return redirect('/login/?next=%s' % (request.path))
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			
			user = authenticate(username=username, password=password)
			
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('home')
		return render(request, self.template_name, {'form': form})
		
def login_view(request):
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect(request.GET['next'])
	return render(request, 'rwkapp/login_form.html', {'form': form, 'title': title})

def logout_view(request):
	logout(request)
	print(request.GET['next'])

	return redirect(request.GET['next'])
