from rest_framework import serializers

from stores.models import Store, Product, ProductBuy, ProductAdd


class StoreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name',)


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'count', 'in_stock',)


class StoreDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True)

    class Meta:
        model = Store
        fields = ('id', 'name', 'products',)


class ProductBuySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBuy
        fields = ('product', 'count',)

    def create(self, validated_data):
        store_pk = self.context['store_pk']
        bought_product_id = validated_data.get('product').id
        bought_count = validated_data.get('count')
        product = Product.objects.filter(
            id=bought_product_id, store_id=store_pk, in_stock=True
        ).first()
        remainder = product.count - bought_count
        if remainder > 0:
            product.count = remainder
            product.save()
            return ProductBuy.objects.create(**validated_data)
        elif remainder == 0:
            product.count = remainder
            product.in_stock = False
            product.save()
            return ProductBuy.objects.create(**validated_data)
        elif remainder < 0:
            raise Exception(f"Insufficient quantity of {product.name}.")


class ProductAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAdd
        fields = ('product', 'count',)

    def create(self, validated_data):
        store_pk = self.context['store_pk']
        added_product_id = validated_data.get('product').id
        added_count = validated_data.get('count')
        product = Product.objects.filter(
            id=added_product_id, store_id=store_pk
        ).first()
        total = product.count + added_count
        product, _ = Product.objects.update_or_create(
            id=added_product_id, store_id=store_pk,
            defaults={'count': total},
        )
        return ProductAdd.objects.create(**validated_data)
