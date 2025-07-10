from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_rename_name_serviceprovider_provider_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceprovider',
            old_name='contact_info',
            new_name='location',
        ),
    ]
