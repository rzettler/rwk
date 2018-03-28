from django.db import models
from django.utils import timezone


class RWK_Mannschaft(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
		
		
class RWK_Schuetze(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
		
		
class RWK_Eintrag(models.Model):
    SCHUSS_ANZAHL = (
		(0, '0'),
		(1, '1'),
		(2, '2'),
		(3, '3'),
		(4, '4'),
		(5, '5'),
		(6, '6'),
		(7, '7'),
		(8, '8'),
		(9,'9'),
		(10,'10'),
	)
    rwk_schuetze = models.ForeignKey(RWK_Schuetze, on_delete=models.CASCADE)
    rwk_mannschaft = models.ForeignKey(RWK_Mannschaft, on_delete=models.CASCADE)
    fight_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=200, default="not_set")
    ringe=models.IntegerField()
    anzahl_0er=models.IntegerField(default=0, choices=SCHUSS_ANZAHL)
    anzahl_1er=models.IntegerField(default=0, choices=SCHUSS_ANZAHL)
    anzahl_2er=models.IntegerField(default=0, choices=SCHUSS_ANZAHL)
    anzahl_3er=models.IntegerField(default=0, choices=SCHUSS_ANZAHL)
    anzahl_4er=models.IntegerField(default=0, choices=SCHUSS_ANZAHL)
    anzahl_5er=models.IntegerField(default=0, choices=SCHUSS_ANZAHL)
    anzahl_6er=models.IntegerField(default=0, choices=SCHUSS_ANZAHL)
    anzahl_7er=models.IntegerField(default=0, choices=SCHUSS_ANZAHL)
    anzahl_8er=models.IntegerField(default=0, choices=SCHUSS_ANZAHL)
    betrag=models.FloatField(default=0)

    def publish(self):
        self.save()

    def __str__(self):
        return self.rwk_schuetze.name + ' ' + self.rwk_mannschaft.name
		
class RWK_Einzahlung(models.Model):
    rwk_schuetze = models.ForeignKey(RWK_Schuetze, on_delete=models.CASCADE)
    betrag = models.FloatField(default=0)
    tag_der_einzahlung = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=200, default="not_set")

    def publish(self):
        self.save()

    def __str__(self):
        return self.rwk_schuetze.name + ' ' + self.tag_der_einzahlung.strftime("%d.%m.%Y")
