from django.contrib import admin

from .submodels.models1 import  *
from .submodels.models2 import  *


from .subadmins.albumAdmin import *
from .subadmins.musicianAdmin import *
from .subadmins.personAdmin import *


admin.site.register(Person, PersonAdmin)
admin.site.register(Musician, MusicianAdmin)
admin.site.register(Album, AlbumAdmin)
