import pytest
from store.models import Category, Product
from django.contrib.auth import get_user_model
User = get_user_model()
# Crear un usuario


@pytest.mark.django_db
def test_crear_categoria():
    categoria = Category.objects.create(
        name='Guitarras',
        slug='guitarras'
    )

    assert categoria.slug == 'guitarras'


def test_crear_categoria_noslug():
    error = False
    try:
        categoria = Category.objects.create(
            name='guitarra',
            slug=''
        )
    except:
        error = True

    assert not error


def test_crear_categoria_noname():
    error = False
    try:
        categoria = Category.objects.create(
            name='',
            slug='guitarra'

        )
    except:
        error = True

    assert not error


@pytest.mark.django_db
def test_crear_producto():
    # Para crear un producto, se debe crear una categoría.
    categoria = Category.objects.create(
        name='Guitarras',
        slug='guitarras'
    )
    # Para crear un produto, debe haber un usuario registrado.
    user = User.objects.create_user(
        username='hugo',
        email='hugo@gmail.com',
        password='123'
    )
    # Creación del producto
    producto = Product.objects.create(
        category=categoria,
        created_by=user,
        name='Guitarra Eléctrica Les Paul 70s Deluxe Cherry Sunburst',
        brand='Gibson',
        description='Lanzada por primera vez en 1969, la Deluxe vio la introducción de la Mini Humbucker™ en la alineación de Les Paul™. Los Mini Humbuckers conservan el rendimiento sin zumbidos de sus primos de tamaño completo, pero con una tonalidad algo más clara y brillante.',
        slug='Guitarra-Eléctrica-Les-Paul-70s-Deluxe-Cherry-Sunburst',
        price=3500000,
        in_stock=True,
        is_active=True
    )

    assert producto.brand == 'Gibson'


@pytest.mark.django_db
def test_crear_producto_nocategoria():
    error = False
    try:
        user = User.objects.create_user(
            username='hugo',
            email='hugo@gmail.com',
            password='123'
        )
        producto = Product.objects.create(
            created_by=user,
            name='Guitarra Eléctrica Les Paul 70s Deluxe Cherry Sunburst',
            brand='Gibson',
            description='Lanzada por primera vez en 1969, la Deluxe vio la introducción de la Mini Humbucker™ en la alineación de Les Paul™. Los Mini Humbuckers conservan el rendimiento sin zumbidos de sus primos de tamaño completo, pero con una tonalidad algo más clara y brillante.',
            slug='Guitarra-Eléctrica-Les-Paul-70s-Deluxe-Cherry-Sunburst',
            price=3500000,
            in_stock=True,
            is_active=True
        )
    except:
        error = True
    assert not error


def test_crear_producto_nouser():
    error = False
    try:
        categoria = Category.objects.create(
            name='Guitarras',
            slug='guitarras'

        )
        producto = Product.objects.create(
            category=categoria,
            name='Guitarra Eléctrica Les Paul 70s Deluxe Cherry Sunburst',
            brand='Gibson',
            description='Lanzada por primera vez en 1969, la Deluxe vio la introducción de la Mini Humbucker™ en la alineación de Les Paul™. Los Mini Humbuckers conservan el rendimiento sin zumbidos de sus primos de tamaño completo, pero con una tonalidad algo más clara y brillante.',
            slug='Guitarra-Eléctrica-Les-Paul-70s-Deluxe-Cherry-Sunburst',
            price=3500000,
            in_stock=True,
            is_active=True
        )
    except:
        error = True
    assert not error


def test_crear_producto_nouserycat():
    error = False
    try:
        producto = Product.objects.create(
            name='Guitarra Eléctrica Les Paul 70s Deluxe Cherry Sunburst',
            brand='Gibson',
            description='Lanzada por primera vez en 1969, la Deluxe vio la introducción de la Mini Humbucker™ en la alineación de Les Paul™. Los Mini Humbuckers conservan el rendimiento sin zumbidos de sus primos de tamaño completo, pero con una tonalidad algo más clara y brillante.',
            slug='Guitarra-Eléctrica-Les-Paul-70s-Deluxe-Cherry-Sunburst',
            price=3500000,
            in_stock=True,
            is_active=True
        )
    except:
        error = True
    assert not error


@pytest.mark.django_db
def test_crear_producto_noname():
    error = False
    try:
        categoria = Category.objects.create(
            name='Guitarras',
            slug='guitarras'
        )
        user = User.objects.create_user(
            username='hugo',
            email='hugo@gmail.com',
            password='123'
        )
        producto = Product.objects.create(
            category=categoria,
            created_by=user,
            brand='Gibson',
            description='Lanzada por primera vez en 1969, la Deluxe vio la introducción de la Mini Humbucker™ en la alineación de Les Paul™. Los Mini Humbuckers conservan el rendimiento sin zumbidos de sus primos de tamaño completo, pero con una tonalidad algo más clara y brillante.',
            slug='Guitarra-Eléctrica-Les-Paul-70s-Deluxe-Cherry-Sunburst',
            price=3500000,
            in_stock=True,
            is_active=True
        )
    except:
        error = True
    assert not error


def test_crear_producto_noprice():
    error = False
    try:
        categoria = Category.objects.create(
            name='Guitarras',
            slug='guitarras'
        )
        user = User.objects.create_user(
            username='hugo',
            email='hugo@gmail.com',
            password='123'
        )
        producto = Product.objects.create(
            category=categoria,
            created_by=user,
            brand='Gibson',
            description='Lanzada por primera vez en 1969, la Deluxe vio la introducción de la Mini Humbucker™ en la alineación de Les Paul™. Los Mini Humbuckers conservan el rendimiento sin zumbidos de sus primos de tamaño completo, pero con una tonalidad algo más clara y brillante.',
            slug='Guitarra-Eléctrica-Les-Paul-70s-Deluxe-Cherry-Sunburst',
            in_stock=True,
            is_active=True
        )
    except:
        error = True
    assert not error


def test_crear_producto_nostock():
    error = False
    try:
        categoria = Category.objects.create(
            name='Guitarras',
            slug='guitarras'
        )
        user = User.objects.create_user(
            username='hugo',
            email='hugo@gmail.com',
            password='123'
        )
        producto = Product.objects.create(
            category=categoria,
            created_by=user,
            brand='Gibson',
            description='Lanzada por primera vez en 1969, la Deluxe vio la introducción de la Mini Humbucker™ en la alineación de Les Paul™. Los Mini Humbuckers conservan el rendimiento sin zumbidos de sus primos de tamaño completo, pero con una tonalidad algo más clara y brillante.',
            slug='Guitarra-Eléctrica-Les-Paul-70s-Deluxe-Cherry-Sunburst',
            price=3500000,
            is_active=True
        )
    except:
        error = True
    assert not error


def test_crear_producto_noisactive():
    error = False
    try:
        categoria = Category.objects.create(
            name='Guitarras',
            slug='guitarras'
        )
        user = User.objects.create_user(
            username='hugo',
            email='hugo@gmail.com',
            password='123'
        )
        producto = Product.objects.create(
            category=categoria,
            created_by=user,
            brand='Gibson',
            description='Lanzada por primera vez en 1969, la Deluxe vio la introducción de la Mini Humbucker™ en la alineación de Les Paul™. Los Mini Humbuckers conservan el rendimiento sin zumbidos de sus primos de tamaño completo, pero con una tonalidad algo más clara y brillante.',
            slug='Guitarra-Eléctrica-Les-Paul-70s-Deluxe-Cherry-Sunburst',
            price=3500000,
            in_stock=True,
        )
    except:
        error = True
    assert not error


def test_crear_producto_noslug():
    error = False
    try:
        categoria = Category.objects.create(
            name='Guitarras',
            slug='guitarras'
        )
        user = User.objects.create_user(
            username='hugo',
            email='hugo@gmail.com',
            password='123'
        )
        producto = Product.objects.create(
            category=categoria,
            created_by=user,
            brand='Gibson',
            description='Lanzada por primera vez en 1969, la Deluxe vio la introducción de la Mini Humbucker™ en la alineación de Les Paul™. Los Mini Humbuckers conservan el rendimiento sin zumbidos de sus primos de tamaño completo, pero con una tonalidad algo más clara y brillante.',
            price=3500000,
            in_stock=True,
            is_active=True

        )
    except:
        error = True
    assert not error
