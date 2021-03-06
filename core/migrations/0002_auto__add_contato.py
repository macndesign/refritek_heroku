# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contato'
        db.create_table(u'core_contato', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('maps', self.gf('django.db.models.fields.TextField')()),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Contato'])


    def backwards(self, orm):
        # Deleting model 'Contato'
        db.delete_table(u'core_contato')


    models = {
        u'core.contato': {
            'Meta': {'object_name': 'Contato'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'data_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maps': ('django.db.models.fields.TextField', [], {})
        },
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