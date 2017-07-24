# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-08 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_arch_projects_mainimgchange'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='architects_supervision',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='architects_supervision',
            name='cost_name',
        ),
        migrations.RemoveField(
            model_name='architects_supervision',
            name='description',
        ),
        migrations.RemoveField(
            model_name='architects_supervision',
            name='name',
        ),
        migrations.RemoveField(
            model_name='architects_supervision',
            name='terms',
        ),
        migrations.RemoveField(
            model_name='architects_supervision',
            name='terms_name',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='construction_documents_description',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='construction_documents_name',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='cost_name',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='description',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='desing_development_name',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='name',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='schematic_desing_name',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='terms',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='terms_name',
        ),
        migrations.RemoveField(
            model_name='interior_design',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='interior_design',
            name='cost_name',
        ),
        migrations.RemoveField(
            model_name='interior_design',
            name='description',
        ),
        migrations.RemoveField(
            model_name='interior_design',
            name='name',
        ),
        migrations.RemoveField(
            model_name='interior_design',
            name='paragraphs_name',
        ),
        migrations.RemoveField(
            model_name='interior_design',
            name='terms',
        ),
        migrations.RemoveField(
            model_name='interior_design',
            name='terms_name',
        ),
        migrations.RemoveField(
            model_name='paragraphs_arch_cd',
            name='language',
        ),
        migrations.RemoveField(
            model_name='paragraphs_arch_cd',
            name='paragraph',
        ),
        migrations.RemoveField(
            model_name='paragraphs_arch_dd',
            name='language',
        ),
        migrations.RemoveField(
            model_name='paragraphs_arch_dd',
            name='paragraph',
        ),
        migrations.RemoveField(
            model_name='paragraphs_arch_sd',
            name='language',
        ),
        migrations.RemoveField(
            model_name='paragraphs_arch_sd',
            name='paragraph',
        ),
        migrations.RemoveField(
            model_name='paragraphs_as',
            name='language',
        ),
        migrations.RemoveField(
            model_name='paragraphs_as',
            name='paragraph',
        ),
        migrations.RemoveField(
            model_name='paragraphs_id',
            name='language',
        ),
        migrations.RemoveField(
            model_name='paragraphs_id',
            name='paragraph',
        ),
        migrations.RemoveField(
            model_name='paragraphs_pd',
            name='language',
        ),
        migrations.RemoveField(
            model_name='paragraphs_pd',
            name='paragraph',
        ),
        migrations.RemoveField(
            model_name='product_design',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='product_design',
            name='cost_name',
        ),
        migrations.RemoveField(
            model_name='product_design',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product_design',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product_design',
            name='paragraphs_name',
        ),
        migrations.RemoveField(
            model_name='product_design',
            name='terms',
        ),
        migrations.RemoveField(
            model_name='product_design',
            name='terms_name',
        ),
        migrations.AddField(
            model_name='architects_supervision',
            name='cost_en',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architects_supervision',
            name='cost_name_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architects_supervision',
            name='cost_name_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architects_supervision',
            name='cost_name_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architects_supervision',
            name='cost_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architects_supervision',
            name='cost_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architects_supervision',
            name='description_en',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='architects_supervision',
            name='description_ru',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='architects_supervision',
            name='description_ua',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='architects_supervision',
            name='name_en',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architects_supervision',
            name='name_ru',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architects_supervision',
            name='name_ua',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architects_supervision',
            name='terms_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architects_supervision',
            name='terms_name_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architects_supervision',
            name='terms_name_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architects_supervision',
            name='terms_name_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architects_supervision',
            name='terms_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architects_supervision',
            name='terms_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='construction_documents_description_en',
            field=models.CharField(default='description', max_length=100),
        ),
        migrations.AddField(
            model_name='architecture',
            name='construction_documents_description_ru',
            field=models.CharField(default='description', max_length=100),
        ),
        migrations.AddField(
            model_name='architecture',
            name='construction_documents_description_ua',
            field=models.CharField(default='description', max_length=100),
        ),
        migrations.AddField(
            model_name='architecture',
            name='construction_documents_name_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='construction_documents_name_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='construction_documents_name_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='cost_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='cost_name_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='cost_name_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='cost_name_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='cost_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='cost_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='description_en',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='architecture',
            name='description_ru',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='architecture',
            name='description_ua',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='architecture',
            name='desing_development_name_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='desing_development_name_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='desing_development_name_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='name_en',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='name_ru',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='name_ua',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='schematic_desing_name_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='schematic_desing_name_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='schematic_desing_name_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='terms_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='terms_name_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='terms_name_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='terms_name_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='terms_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='architecture',
            name='terms_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interior_design',
            name='cost_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interior_design',
            name='cost_name_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interior_design',
            name='cost_name_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interior_design',
            name='cost_name_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interior_design',
            name='cost_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interior_design',
            name='cost_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interior_design',
            name='description_en',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='interior_design',
            name='description_ru',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='interior_design',
            name='description_ua',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='interior_design',
            name='name_en',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interior_design',
            name='name_ru',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interior_design',
            name='name_ua',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interior_design',
            name='paragraphs_name_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interior_design',
            name='paragraphs_name_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interior_design',
            name='paragraphs_name_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interior_design',
            name='terms_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interior_design',
            name='terms_name_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interior_design',
            name='terms_name_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interior_design',
            name='terms_name_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interior_design',
            name='terms_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interior_design',
            name='terms_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paragraphs_arch_cd',
            name='paragraph_en',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_arch_cd',
            name='paragraph_ru',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_arch_cd',
            name='paragraph_ua',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_arch_dd',
            name='paragraph_en',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_arch_dd',
            name='paragraph_ru',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_arch_dd',
            name='paragraph_ua',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_arch_sd',
            name='paragraph_en',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_arch_sd',
            name='paragraph_ru',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_arch_sd',
            name='paragraph_ua',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_as',
            name='paragraph_en',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_as',
            name='paragraph_ru',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_as',
            name='paragraph_ua',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_id',
            name='paragraph_en',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_id',
            name='paragraph_ru',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_id',
            name='paragraph_ua',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_pd',
            name='paragraph_en',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_pd',
            name='paragraph_ru',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_pd',
            name='paragraph_ua',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='product_design',
            name='cost_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_design',
            name='cost_name_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_design',
            name='cost_name_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_design',
            name='cost_name_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_design',
            name='cost_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_design',
            name='cost_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_design',
            name='description_en',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='product_design',
            name='description_ru',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='product_design',
            name='description_ua',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='product_design',
            name='name_en',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_design',
            name='name_ru',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_design',
            name='name_ua',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_design',
            name='paragraphs_name_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_design',
            name='paragraphs_name_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_design',
            name='paragraphs_name_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_design',
            name='terms_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_design',
            name='terms_name_en',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_design',
            name='terms_name_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_design',
            name='terms_name_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_design',
            name='terms_ru',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_design',
            name='terms_ua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
