# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table(u'shop_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'saled', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            (u'keywords_string', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            (u'rating_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            (u'rating_sum', self.gf('django.db.models.fields.IntegerField')(default=0)),
            (u'rating_average', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('_meta_title', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gen_description', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('short_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('in_sitemap', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('unit_price', self.gf('cartridge.shop.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('sale_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('sale_price', self.gf('cartridge.shop.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('sale_from', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('sale_to', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('sku', self.gf('cartridge.shop.fields.SKUField')(max_length=20, unique=True, null=True, blank=True)),
            ('num_in_stock', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('available', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('keywords', self.gf('mezzanine.generic.fields.KeywordsField')(object_id_field=u'object_pk', to=orm['generic.AssignedKeyword'])),
            ('rating', self.gf('mezzanine.generic.fields.RatingField')(object_id_field=u'object_pk', to=orm['generic.Rating'])),
        ))
        db.send_create_signal(u'shop', ['Product'])

        # Adding M2M table for field categories on 'Product'
        m2m_table_name = db.shorten_name(u'shop_product_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'shop.product'], null=False)),
            ('category', models.ForeignKey(orm[u'shop.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'category_id'])

        # Adding M2M table for field related_products on 'Product'
        m2m_table_name = db.shorten_name(u'shop_product_related_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_product', models.ForeignKey(orm[u'shop.product'], null=False)),
            ('to_product', models.ForeignKey(orm[u'shop.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_product_id', 'to_product_id'])

        # Adding M2M table for field upsell_products on 'Product'
        m2m_table_name = db.shorten_name(u'shop_product_upsell_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_product', models.ForeignKey(orm[u'shop.product'], null=False)),
            ('to_product', models.ForeignKey(orm[u'shop.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_product_id', 'to_product_id'])

        # Adding model 'ProductImage'
        db.create_table(u'shop_productimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('file', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'images', to=orm['shop.Product'])),
        ))
        db.send_create_signal(u'shop', ['ProductImage'])

        # Adding model 'ProductOption'
        db.create_table(u'shop_productoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('cartridge.shop.fields.OptionField')(max_length=50, null=True)),
        ))
        db.send_create_signal(u'shop', ['ProductOption'])

        # Adding model 'ProductVariation'
        db.create_table(u'shop_productvariation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unit_price', self.gf('cartridge.shop.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('sale_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('sale_price', self.gf('cartridge.shop.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('sale_from', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('sale_to', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('sku', self.gf('cartridge.shop.fields.SKUField')(max_length=20, unique=True, null=True, blank=True)),
            ('num_in_stock', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'variations', to=orm['shop.Product'])),
            ('default', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.ProductImage'], null=True, blank=True)),
            (u'option1', self.gf('cartridge.shop.fields.OptionField')(max_length=50, null=True)),
            (u'option2', self.gf('cartridge.shop.fields.OptionField')(max_length=50, null=True)),
            (u'option3', self.gf('cartridge.shop.fields.OptionField')(max_length=50, null=True)),
        ))
        db.send_create_signal(u'shop', ['ProductVariation'])

        # Adding model 'Category'
        db.create_table(u'shop_category', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('featured_image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('sale', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Sale'], null=True, blank=True)),
            ('price_min', self.gf('cartridge.shop.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('price_max', self.gf('cartridge.shop.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('combined', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'shop', ['Category'])

        # Adding M2M table for field products on 'Category'
        m2m_table_name = db.shorten_name(u'shop_category_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('category', models.ForeignKey(orm[u'shop.category'], null=False)),
            ('product', models.ForeignKey(orm[u'shop.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['category_id', 'product_id'])

        # Adding M2M table for field options on 'Category'
        m2m_table_name = db.shorten_name(u'shop_category_options')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('category', models.ForeignKey(orm[u'shop.category'], null=False)),
            ('productoption', models.ForeignKey(orm[u'shop.productoption'], null=False))
        ))
        db.create_unique(m2m_table_name, ['category_id', 'productoption_id'])

        # Adding model 'Order'
        db.create_table(u'shop_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'prefer_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('billing_detail_first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('billing_detail_last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('billing_detail_street', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('billing_detail_city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('billing_detail_state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('billing_detail_postcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('billing_detail_country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('billing_detail_phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('billing_detail_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('shipping_detail_first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('shipping_detail_last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('shipping_detail_street', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('shipping_detail_city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('shipping_detail_state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('shipping_detail_postcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('shipping_detail_country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('shipping_detail_phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('additional_instructions', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('shipping_type', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('shipping_total', self.gf('cartridge.shop.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('tax_type', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('tax_total', self.gf('cartridge.shop.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('item_total', self.gf('cartridge.shop.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('discount_code', self.gf('cartridge.shop.fields.DiscountCodeField')(max_length=20, blank=True)),
            ('discount_total', self.gf('cartridge.shop.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('total', self.gf('cartridge.shop.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('transaction_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'shop', ['Order'])

        # Adding model 'Cart'
        db.create_table(u'shop_cart', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal(u'shop', ['Cart'])

        # Adding model 'CartItem'
        db.create_table(u'shop_cartitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sku', self.gf('cartridge.shop.fields.SKUField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('unit_price', self.gf('cartridge.shop.fields.MoneyField')(default='0', null=True, max_digits=10, decimal_places=2, blank=True)),
            ('total_price', self.gf('cartridge.shop.fields.MoneyField')(default='0', null=True, max_digits=10, decimal_places=2, blank=True)),
            ('cart', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'items', to=orm['shop.Cart'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
        ))
        db.send_create_signal(u'shop', ['CartItem'])

        # Adding model 'OrderItem'
        db.create_table(u'shop_orderitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sku', self.gf('cartridge.shop.fields.SKUField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('unit_price', self.gf('cartridge.shop.fields.MoneyField')(default='0', null=True, max_digits=10, decimal_places=2, blank=True)),
            ('total_price', self.gf('cartridge.shop.fields.MoneyField')(default='0', null=True, max_digits=10, decimal_places=2, blank=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'items', to=orm['shop.Order'])),
        ))
        db.send_create_signal(u'shop', ['OrderItem'])

        # Adding model 'ProductAction'
        db.create_table(u'shop_productaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'actions', to=orm['shop.Product'])),
            ('timestamp', self.gf('django.db.models.fields.IntegerField')()),
            ('total_cart', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total_purchase', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'shop', ['ProductAction'])

        # Adding unique constraint on 'ProductAction', fields ['product', 'timestamp']
        db.create_unique(u'shop_productaction', ['product_id', 'timestamp'])

        # Adding model 'Sale'
        db.create_table(u'shop_sale', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('discount_deduct', self.gf('cartridge.shop.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('discount_percent', self.gf('cartridge.shop.fields.PercentageField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('discount_exact', self.gf('cartridge.shop.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('valid_from', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('valid_to', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'shop', ['Sale'])

        # Adding M2M table for field products on 'Sale'
        m2m_table_name = db.shorten_name(u'shop_sale_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sale', models.ForeignKey(orm[u'shop.sale'], null=False)),
            ('product', models.ForeignKey(orm[u'shop.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['sale_id', 'product_id'])

        # Adding M2M table for field categories on 'Sale'
        m2m_table_name = db.shorten_name(u'shop_sale_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sale', models.ForeignKey(orm[u'shop.sale'], null=False)),
            ('category', models.ForeignKey(orm[u'shop.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['sale_id', 'category_id'])

        # Adding model 'DiscountCode'
        db.create_table(u'shop_discountcode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('discount_deduct', self.gf('cartridge.shop.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('discount_percent', self.gf('cartridge.shop.fields.PercentageField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('discount_exact', self.gf('cartridge.shop.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('valid_from', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('valid_to', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('code', self.gf('cartridge.shop.fields.DiscountCodeField')(unique=True, max_length=20)),
            ('min_purchase', self.gf('cartridge.shop.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('free_shipping', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('uses_remaining', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'shop', ['DiscountCode'])

        # Adding M2M table for field products on 'DiscountCode'
        m2m_table_name = db.shorten_name(u'shop_discountcode_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('discountcode', models.ForeignKey(orm[u'shop.discountcode'], null=False)),
            ('product', models.ForeignKey(orm[u'shop.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['discountcode_id', 'product_id'])

        # Adding M2M table for field categories on 'DiscountCode'
        m2m_table_name = db.shorten_name(u'shop_discountcode_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('discountcode', models.ForeignKey(orm[u'shop.discountcode'], null=False)),
            ('category', models.ForeignKey(orm[u'shop.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['discountcode_id', 'category_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ProductAction', fields ['product', 'timestamp']
        db.delete_unique(u'shop_productaction', ['product_id', 'timestamp'])

        # Deleting model 'Product'
        db.delete_table(u'shop_product')

        # Removing M2M table for field categories on 'Product'
        db.delete_table(db.shorten_name(u'shop_product_categories'))

        # Removing M2M table for field related_products on 'Product'
        db.delete_table(db.shorten_name(u'shop_product_related_products'))

        # Removing M2M table for field upsell_products on 'Product'
        db.delete_table(db.shorten_name(u'shop_product_upsell_products'))

        # Deleting model 'ProductImage'
        db.delete_table(u'shop_productimage')

        # Deleting model 'ProductOption'
        db.delete_table(u'shop_productoption')

        # Deleting model 'ProductVariation'
        db.delete_table(u'shop_productvariation')

        # Deleting model 'Category'
        db.delete_table(u'shop_category')

        # Removing M2M table for field products on 'Category'
        db.delete_table(db.shorten_name(u'shop_category_products'))

        # Removing M2M table for field options on 'Category'
        db.delete_table(db.shorten_name(u'shop_category_options'))

        # Deleting model 'Order'
        db.delete_table(u'shop_order')

        # Deleting model 'Cart'
        db.delete_table(u'shop_cart')

        # Deleting model 'CartItem'
        db.delete_table(u'shop_cartitem')

        # Deleting model 'OrderItem'
        db.delete_table(u'shop_orderitem')

        # Deleting model 'ProductAction'
        db.delete_table(u'shop_productaction')

        # Deleting model 'Sale'
        db.delete_table(u'shop_sale')

        # Removing M2M table for field products on 'Sale'
        db.delete_table(db.shorten_name(u'shop_sale_products'))

        # Removing M2M table for field categories on 'Sale'
        db.delete_table(db.shorten_name(u'shop_sale_categories'))

        # Deleting model 'DiscountCode'
        db.delete_table(u'shop_discountcode')

        # Removing M2M table for field products on 'DiscountCode'
        db.delete_table(db.shorten_name(u'shop_discountcode_products'))

        # Removing M2M table for field categories on 'DiscountCode'
        db.delete_table(db.shorten_name(u'shop_discountcode_categories'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'generic.assignedkeyword': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'AssignedKeyword'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'assignments'", 'to': u"orm['generic.Keyword']"}),
            'object_pk': ('django.db.models.fields.IntegerField', [], {})
        },
        u'generic.keyword': {
            'Meta': {'object_name': 'Keyword'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'generic.rating': {
            'Meta': {'object_name': 'Rating'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_pk': ('django.db.models.fields.IntegerField', [], {}),
            'rating_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ratings'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'keywords': ('mezzanine.generic.fields.KeywordsField', [], {'object_id_field': "u'object_pk'", 'to': u"orm['generic.AssignedKeyword']"}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'shop.cart': {
            'Meta': {'object_name': 'Cart'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'shop.cartitem': {
            'Meta': {'object_name': 'CartItem'},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'items'", 'to': u"orm['shop.Cart']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sku': ('cartridge.shop.fields.SKUField', [], {'max_length': '20'}),
            'total_price': ('cartridge.shop.fields.MoneyField', [], {'default': "'0'", 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'unit_price': ('cartridge.shop.fields.MoneyField', [], {'default': "'0'", 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        },
        u'shop.category': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Category', '_ormbases': [u'pages.Page']},
            'combined': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'featured_image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'options': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'product_options'", 'blank': 'True', 'to': u"orm['shop.ProductOption']"}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'price_max': ('cartridge.shop.fields.MoneyField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'price_min': ('cartridge.shop.fields.MoneyField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['shop.Product']", 'symmetrical': 'False', 'blank': 'True'}),
            'sale': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.Sale']", 'null': 'True', 'blank': 'True'})
        },
        u'shop.discountcode': {
            'Meta': {'object_name': 'DiscountCode'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'discountcode_related'", 'blank': 'True', 'to': u"orm['shop.Category']"}),
            'code': ('cartridge.shop.fields.DiscountCodeField', [], {'unique': 'True', 'max_length': '20'}),
            'discount_deduct': ('cartridge.shop.fields.MoneyField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'discount_exact': ('cartridge.shop.fields.MoneyField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'discount_percent': ('cartridge.shop.fields.PercentageField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'free_shipping': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'min_purchase': ('cartridge.shop.fields.MoneyField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['shop.Product']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uses_remaining': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'valid_from': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'valid_to': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'shop.order': {
            'Meta': {'ordering': "(u'-id',)", 'object_name': 'Order'},
            'additional_instructions': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'billing_detail_city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'billing_detail_country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'billing_detail_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'billing_detail_first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'billing_detail_last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'billing_detail_phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'billing_detail_postcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'billing_detail_state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'billing_detail_street': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'discount_code': ('cartridge.shop.fields.DiscountCodeField', [], {'max_length': '20', 'blank': 'True'}),
            'discount_total': ('cartridge.shop.fields.MoneyField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_total': ('cartridge.shop.fields.MoneyField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'prefer_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'shipping_detail_city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'shipping_detail_country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'shipping_detail_first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'shipping_detail_last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'shipping_detail_phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'shipping_detail_postcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'shipping_detail_state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'shipping_detail_street': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'shipping_total': ('cartridge.shop.fields.MoneyField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'shipping_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tax_total': ('cartridge.shop.fields.MoneyField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'tax_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'total': ('cartridge.shop.fields.MoneyField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'shop.orderitem': {
            'Meta': {'object_name': 'OrderItem'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'items'", 'to': u"orm['shop.Order']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sku': ('cartridge.shop.fields.SKUField', [], {'max_length': '20'}),
            'total_price': ('cartridge.shop.fields.MoneyField', [], {'default': "'0'", 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'unit_price': ('cartridge.shop.fields.MoneyField', [], {'default': "'0'", 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'})
        },
        u'shop.product': {
            'Meta': {'object_name': 'Product'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['shop.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'keywords': ('mezzanine.generic.fields.KeywordsField', [], {'object_id_field': "u'object_pk'", 'to': u"orm['generic.AssignedKeyword']"}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'num_in_stock': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'rating': ('mezzanine.generic.fields.RatingField', [], {'object_id_field': "u'object_pk'", 'to': u"orm['generic.Rating']"}),
            u'rating_average': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            u'rating_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'rating_sum': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'related_products': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_products_rel_+'", 'blank': 'True', 'to': u"orm['shop.Product']"}),
            'sale_from': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sale_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'sale_price': ('cartridge.shop.fields.MoneyField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'sale_to': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'saled': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'sku': ('cartridge.shop.fields.SKUField', [], {'max_length': '20', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'unit_price': ('cartridge.shop.fields.MoneyField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'upsell_products': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'upsell_products_rel_+'", 'blank': 'True', 'to': u"orm['shop.Product']"})
        },
        u'shop.productaction': {
            'Meta': {'unique_together': "((u'product', u'timestamp'),)", 'object_name': 'ProductAction'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'actions'", 'to': u"orm['shop.Product']"}),
            'timestamp': ('django.db.models.fields.IntegerField', [], {}),
            'total_cart': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_purchase': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'shop.productimage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'ProductImage'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'images'", 'to': u"orm['shop.Product']"})
        },
        u'shop.productoption': {
            'Meta': {'object_name': 'ProductOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('cartridge.shop.fields.OptionField', [], {'max_length': '50', 'null': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        u'shop.productvariation': {
            'Meta': {'ordering': "(u'-default',)", 'object_name': 'ProductVariation'},
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.ProductImage']", 'null': 'True', 'blank': 'True'}),
            'num_in_stock': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'option1': ('cartridge.shop.fields.OptionField', [], {'max_length': '50', 'null': 'True'}),
            u'option2': ('cartridge.shop.fields.OptionField', [], {'max_length': '50', 'null': 'True'}),
            u'option3': ('cartridge.shop.fields.OptionField', [], {'max_length': '50', 'null': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'variations'", 'to': u"orm['shop.Product']"}),
            'sale_from': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sale_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'sale_price': ('cartridge.shop.fields.MoneyField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'sale_to': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sku': ('cartridge.shop.fields.SKUField', [], {'max_length': '20', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'unit_price': ('cartridge.shop.fields.MoneyField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'})
        },
        u'shop.sale': {
            'Meta': {'object_name': 'Sale'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'sale_related'", 'blank': 'True', 'to': u"orm['shop.Category']"}),
            'discount_deduct': ('cartridge.shop.fields.MoneyField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'discount_exact': ('cartridge.shop.fields.MoneyField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'discount_percent': ('cartridge.shop.fields.PercentageField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['shop.Product']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'valid_from': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'valid_to': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['shop']