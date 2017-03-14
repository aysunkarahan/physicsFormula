from django.db import models

#Red pk 1
class Seviye(models.Model):
    ad = models.CharField(max_length =250)
    konu = models.CharField(max_length =250)

    def __str__(self):
        return self.ad +' - '+ self.konu

class Kelime(models.Model):
        seviye = models.ForeignKey(Seviye, on_delete=models.CASCADE)
        kelime_adi =models.CharField(max_length=250)
        anlami =models.CharField(max_length=250)


        def __str__(self):
            return self.kelime_adi
