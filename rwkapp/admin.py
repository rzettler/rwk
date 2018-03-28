from django.contrib import admin
from .models import RWK_Mannschaft
from .models import RWK_Schuetze
from .models import RWK_Eintrag
from .models import RWK_Einzahlung


# Register your models here.
admin.site.register(RWK_Mannschaft)
admin.site.register(RWK_Schuetze)
admin.site.register(RWK_Eintrag)
admin.site.register(RWK_Einzahlung)
