# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pagina'
        db.create_table(u'core_pagina', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('keywords', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('titulo_empresa', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('subtitulo_empresa', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('titulo_contato', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('subtitulo_contato', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('titulo_sobre', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('subtitulo_sobre', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('footer_content', self.gf('django.db.models.fields.TextField')()),
            ('data_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Pagina'])

        # Adding model 'Slider'
        db.create_table(u'core_slider', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ordenacao', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('imagem', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('desc', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('html_desc', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Slider'])

        # Adding model 'Empresa'
        db.create_table(u'core_empresa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ordenacao', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('imagem', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Empresa'])

        # Adding model 'Produto'
        db.create_table(u'core_produto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ordenacao', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('thumb', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('imagem', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Empresa'])),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Produto'])

        # Adding model 'Sobre'
        db.create_table(u'core_sobre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Sobre'])


    def backwards(self, orm):
        # Deleting model 'Pagina'
        db.delete_table(u'core_pagina')

        # Deleting model 'Slider'
        db.delete_table(u'core_slider')

        # Deleting model 'Empresa'
        db.delete_table(u'core_empresa')

        # Deleting model 'Produto'
        db.delete_table(u'core_produto')

        # Deleting model 'Sobre'
        db.delete_table(u'core_sobre')


    models = {
        u'core.empresa': {
            'Meta': {'ordering': "['ordenacao', 'nome']", 'object_name': 'Empresa'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'data_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'ordenacao': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'core.pagina': {
            'Meta': {'object_name': 'Pagina'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'data_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'footer_content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'subtitulo_contato': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'subtitulo_empresa': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'subtitulo_sobre': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'titulo_contato': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'titulo_empresa': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'titulo_sobre': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'core.produto': {
            'Meta': {'ordering': "['ordenacao', 'nome']", 'object_name': 'Produto'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'data_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'ordenacao': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'core.slider': {
            'Meta': {'ordering': "['ordenacao', 'nome']", 'object_name': 'Slider'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'data_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'html_desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'ordenacao': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'core.sobre': {
            'Meta': {'object_name': 'Sobre'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'data_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['core']