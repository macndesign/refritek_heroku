# coding: utf-8
from django.db import models


class Pagina(models.Model):
    name = models.CharField(max_length=75)
    author = models.CharField(u'Author metatag', max_length=120)
    keywords = models.TextField(u'Keywords metatag')
    description = models.TextField(u'Description metatag')

    titulo_destaque = models.CharField(u'Título de destaques', max_length=120)
    subtitulo_destaque = models.CharField(u'Sub-título de destaques', max_length=120)
    titulo_empresa = models.CharField(u'Título de empresas', max_length=120)
    subtitulo_empresa = models.CharField(u'Sub-título de empresas', max_length=120)
    titulo_contato = models.CharField(u'Título de contato', max_length=120)
    subtitulo_contato = models.CharField(u'Sub-título de contato', max_length=120)
    titulo_sobre = models.CharField(u'Título de sobre a empresa', max_length=120)
    subtitulo_sobre = models.CharField(u'Sub-título de sobre a empresa', max_length=120)

    footer_content = models.TextField(u'Footer content')

    data_criacao = models.DateTimeField(
        verbose_name=u'Data de criação',
        auto_now_add=True,
        editable=True
    )
    data_atualizacao = models.DateTimeField(
        verbose_name=u'Data de atualização',
        auto_now=True,
        editable=True
    )

    def __unicode__(self):
        return self.name


class SliderQuerySet(models.query.QuerySet):
    def ativos(self):
        return self.filter(ativo=True)


class SliderManager(models.Manager):
    def get_query_set(self):
        return SliderQuerySet(self.model, using=self._db)

    def ativos(self):
        return self.get_query_set().ativos()


class Slider(models.Model):
    ordenacao = models.PositiveSmallIntegerField(u'Ordenação', default=0)
    nome = models.CharField(max_length=120)
    imagem = models.ImageField(upload_to='sliders')
    titulo = models.CharField(u'Título', max_length=120, blank=True)
    desc = models.TextField(u'Descrição', blank=True)
    html_desc = models.TextField(u'Desc. HTML', blank=True)
    url = models.URLField('URL', blank=True)
    ativo = models.BooleanField(default=False)

    data_criacao = models.DateTimeField(
        verbose_name=u'Data de criação',
        auto_now_add=True,
        editable=True
    )
    data_atualizacao = models.DateTimeField(
        verbose_name=u'Data de atualização',
        auto_now=True,
        editable=True
    )

    objects = SliderManager()

    class Meta:
        ordering = ['ordenacao', 'nome']

    def __unicode__(self):
        return self.nome


class EmpresaQuerySet(models.query.QuerySet):
    def ativos(self):
        return self.filter(ativo=True)


class EmpresaManager(models.Manager):
    def get_query_set(self):
        return EmpresaQuerySet(self.model, using=self._db)

    def ativos(self):
        return self.get_query_set().ativos()


class Empresa(models.Model):
    ordenacao = models.PositiveSmallIntegerField(u'Ordenação', default=0)
    nome = models.CharField(max_length=120)
    imagem = models.ImageField(upload_to='empresas')
    ativo = models.BooleanField(default=False)

    data_criacao = models.DateTimeField(
        verbose_name=u'Data de criação',
        auto_now_add=True,
        editable=True
    )
    data_atualizacao = models.DateTimeField(
        verbose_name=u'Data de atualização',
        auto_now=True,
        editable=True
    )

    def get_absolute_url(self):
        return '/empresa/%s/' % self.pk

    objects = EmpresaManager()

    class Meta:
        ordering = ['ordenacao', 'nome']

    def __unicode__(self):
        return self.nome


class ProdutoQuerySet(models.query.QuerySet):
    def ativos(self):
        return self.filter(ativo=True)

    def destaques(self):
        return self.filter(destaque=True)


class ProdutoManager(models.Manager):
    def get_query_set(self):
        return ProdutoQuerySet(self.model, using=self._db)

    def ativos(self):
        return self.get_query_set().ativos()

    def destaques(self):
        return self.get_query_set().destaques()


class Produto(models.Model):
    ordenacao = models.PositiveSmallIntegerField(u'Ordenação', default=0)
    nome = models.CharField(max_length=120)
    desc = models.TextField(u'Descrição', blank=True)
    thumb = models.ImageField(upload_to='produtos')
    imagem = models.ImageField(upload_to='produtos')
    empresa = models.ForeignKey('Empresa')
    destaque = models.BooleanField(default=False)
    ativo = models.BooleanField(default=False)

    data_criacao = models.DateTimeField(
        verbose_name=u'Data de criação',
        auto_now_add=True,
        editable=True
    )
    data_atualizacao = models.DateTimeField(
        verbose_name=u'Data de atualização',
        auto_now=True,
        editable=True
    )

    def get_absolute_url(self):
        return '/produto/%s/' % self.pk

    objects = ProdutoManager()

    class Meta:
        ordering = ['ordenacao', 'nome']

    def __unicode__(self):
        return self.nome


class CartaoQuerySet(models.query.QuerySet):
    def ativos(self):
        return self.filter(ativo=True)


class CartaoManager(models.Manager):
    def get_query_set(self):
        return CartaoQuerySet(self.model, using=self._db)

    def ativos(self):
        return self.get_query_set().ativos()


class Cartao(models.Model):
    ordenacao = models.PositiveSmallIntegerField(u'Cartão', default=0)
    nome = models.CharField(max_length=120)
    imagem = models.ImageField(upload_to='cartao')
    ativo = models.BooleanField(default=False)

    data_criacao = models.DateTimeField(
        verbose_name=u'Data de criação',
        auto_now_add=True,
        editable=True
    )
    data_atualizacao = models.DateTimeField(
        verbose_name=u'Data de atualização',
        auto_now=True,
        editable=True
    )

    def get_absolute_url(self):
        return '/cartao/%s/' % self.pk

    objects = CartaoManager()

    class Meta:
        ordering = ['ordenacao', 'nome']
        verbose_name = u'Cartão'
        verbose_name_plural = u'Cartões'

    def __unicode__(self):
        return self.nome


class SobreQuerySet(models.query.QuerySet):
    def ativos(self):
        return self.filter(ativo=True)


class SobreManager(models.Manager):
    def get_query_set(self):
        return SobreQuerySet(self.model, using=self._db)

    def ativos(self):
        return self.get_query_set().ativos()


class Sobre(models.Model):
    desc = models.TextField(u'Descrição')
    ativo = models.BooleanField(default=False)

    data_criacao = models.DateTimeField(
        verbose_name=u'Data de criação',
        auto_now_add=True,
        editable=True
    )
    data_atualizacao = models.DateTimeField(
        verbose_name=u'Data de atualização',
        auto_now=True,
        editable=True
    )

    objects = SobreManager()

    class Meta:
        verbose_name_plural = 'Textos sobre a empresa'

    def __unicode__(self):
        return self.desc


class ContatoQuerySet(models.query.QuerySet):
    def ativos(self):
        return self.filter(ativo=True)


class ContatoManager(models.Manager):
    def get_query_set(self):
        return ContatoQuerySet(self.model, using=self._db)

    def ativos(self):
        return self.get_query_set().ativos()


class Contato(models.Model):
    maps = models.TextField(
        help_text=u'Cole aqui o código HTML pra incorporar o mapa do Google Maps ao site com largura de 100% e altura '
                  u'de 300px'
    )
    desc = models.TextField(u'Descrição')
    ativo = models.BooleanField(default=False)

    data_criacao = models.DateTimeField(
        verbose_name=u'Data de criação',
        auto_now_add=True,
        editable=True
    )
    data_atualizacao = models.DateTimeField(
        verbose_name=u'Data de atualização',
        auto_now=True,
        editable=True
    )

    objects = ContatoManager()

    def __unicode__(self):
        return self.desc
