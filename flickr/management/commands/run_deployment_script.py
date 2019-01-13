import flickrapi
import json
from urllib.request import urlopen
from tempfile import NamedTemporaryFile


from django.core.files import File
from django.core.management import BaseCommand


from flickr.models import Profile, Flickrgroup, Photo
from infilect.settings import api_key, api_secret

class Command(BaseCommand):

    def handle(self, *args, **options):

        print("processing......................................")

        user = Profile.objects.all()[0]
        user.nsid = "144234201@N08"
        user.name = "emon0727"
        user.save()

        flickr = flickrapi.FlickrAPI(api_key, api_secret, format='json')
        groups_list = json.loads(flickr.people.getGroups(user_id="144234201@N08"))['groups']['group']

        for group in groups_list:

            grup = Flickrgroup.objects.create( nsid = group['nsid'], group_name = group['name'])

            grup.profile_set.add(user)

            photo_list = json.loads(flickr.groups.pools.getPhotos(group_id = grup.nsid, per_page='50'))['photos']['photo']
            for photo in photo_list:

                foto = Photo.objects.create(photo_id = photo['id'], secret = photo['secret'], server=photo['server'],
                                             farm=photo['farm'], title=photo['title'] ,owner_name=photo['ownername']
                                             ,group = grup)

                url = 'http://farm'+str(foto.farm)+'.staticflickr.com/'+str(foto.server)+'/'+str(foto.photo_id)+'_'+str(foto.secret)+'.jpg'

                foto.image_url  = url


                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(urlopen(url).read())
                img_temp.flush()
                foto.image.save(f"{foto.photo_id}+'_'+{foto.title}+.jpg", File(img_temp))
                foto.save()


        print("############---------Completed-----------################")


