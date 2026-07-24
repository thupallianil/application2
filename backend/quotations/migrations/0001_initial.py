# Recreated migration — fixes model name (Quote→Quotation) and field name (quote_id→quotation_id)

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotation_id', models.CharField(max_length=50, unique=True)),
                ('amount', models.CharField(max_length=50)),
                ('status', models.CharField(
                    choices=[
                        ('Accepted', 'Accepted'),
                        ('Pending', 'Pending'),
                        ('Rejected', 'Rejected'),
                    ],
                    max_length=20,
                )),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
            ],
        ),
    ]
