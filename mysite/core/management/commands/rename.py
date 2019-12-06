from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Rename a Django Project'

    def add_arguments(self,parser):
        # parser.add_argument('-p','--prefix')
        parser.add_argument('new_project_name',type=str,help='The new Django Project name')

    def handle(self,*args,**kwargs):
        new_project_name = kwargs['new_project_name']

        # logic to rename the project
        files_to_rename = ['mysite/settings/base.py',
                          'mysite/wsgi.py',
                          'manage.py'
                        ]
        folder_to_rename = 'mysite'

        for f in files_to_rename:
            with open(f,'r') as file:
                filedata = file.read()
            
            filedata = filedata.replace('demo',new_project_name)

            with open(f,'w') as file:
                file.write(filedata)

        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(self.style.SUCCESS('Project has been rename to %s' % new_project_name))

