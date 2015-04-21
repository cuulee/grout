# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields
import django.contrib.gis.db.models.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSchema',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('version', models.IntegerField()),
                ('schema', django_pgjson.fields.JsonBField()),
                ('label', models.CharField(max_length=50)),
                ('slug', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('occurred_from', models.DateTimeField()),
                ('occurred_to', models.DateTimeField()),
                ('label', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=3857)),
                ('data', django_pgjson.fields.JsonBField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecordSchema',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('version', models.IntegerField()),
                ('schema', django_pgjson.fields.JsonBField()),
                ('record_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='recordschema',
            unique_together=set([('record_type', 'version')]),
        ),
        migrations.AddField(
            model_name='record',
            name='schema_id',
            field=models.ForeignKey(to='ashlar.RecordSchema'),
        ),
        migrations.AlterUniqueTogether(
            name='itemschema',
            unique_together=set([('slug', 'version')]),
        ),
    ]
