import pytest
from django.contrib.auth import get_user_model
User= get_user_model()
# Crear un usuario
@pytest.mark.django_db
def test_crear_usuario():
    user = User.objects.create_user(
            username='hugo',
            email='hugo@gmail.com',
            password='123'
    )
    assert user.username == 'hugo'
@pytest.mark.django_db
def test_crear_usuario_nousername():
    error = False
    try:
        user = User.objects.create_user(
                email='hugo@gmail.com',
                password='123'
        )
    except:
        error = True
    assert not error 
@pytest.mark.django_db
def test_crear_usuario_nopassword():
    error = False
    try:
        user = User.objects.create_user(
                username='hugo',
                email='hugo@gmail.com',
        )
    except:
        error = True
    assert not error
@pytest.mark.django_db
def test_crear_usuario_noemail():
    error = False
    try:
        user = User.objects.create_user(
                username='hugo',
                password='123',
        )
    except:
        error = True
    assert not error
def test_crear_usuario_noemailypassword():
    error = False
    try:
        user = User.objects.create_user(
                username='hugo',
        )
    except:
        error = True
    assert not error 
# Crear un super usuario
@pytest.mark.django_db
def test_crear_superusuario():
    user = User.objects.create_superuser(
            username='vicente',
            email='vicente@gmail.com',
            password='123'
    )
    assert user.is_superuser
def test_crear_superusuario_nousername():
    error = False
    try:
        user = User.objects.create_superuser(
                email='vicente@gmail.com',
                password='123'
        )
    except:
        error = True
    assert not error
def test_crear_superusuario_nopassword():
    error = False
    try:
        user = User.objects.create_superuser(
                username='vicente',
                email='vicente@gmail.com',
                
        )
    except:
        error = True
    assert not error 
@pytest.mark.django_db
def test_crear_usuario_staff():
    user = User.objects.create_superuser(
            username='vicente',
            email='vicente@gmail.com',
            password='123',
            is_staff=True
    )
    assert user.is_staff
def test_crear_usuario_staff_nousername():
    error = False
    try:
        user = User.objects.create_superuser(
                email='vicente@gmail.com',
                password='123',
                is_staff=True
        )
    except:
        error = True
    assert not error
@pytest.mark.django_db
def test_usuario_existe():
    User.objects.create_user(
            username='javier',
            email='javier@gmail.com',
            password='123'
    )
    assert User.objects.filter(username='javier').exists()
    
    assert User.objects.filter(username='javier').exists()
# Verificar si existe un super usuario
@pytest.mark.django_db
def test_usuario_existe_fallido():
    # Crear un usuario de prueba en la base de datos
    User.objects.create_user(
            username='javier',
            email='javier@gmail.com',
            password='123'
    )
    # Verificar si el usuario existe en la base de datos
    assert User.objects.filter(username='javier').exists()
    
    # Verificar un usuario que no existe.
    assert not User.objects.filter(username='kevin').exists()

