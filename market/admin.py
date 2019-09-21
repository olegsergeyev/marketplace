from django.contrib import admin
from market.models import Item  # абсолютные пути это плохо

admin.site.register(Item)
