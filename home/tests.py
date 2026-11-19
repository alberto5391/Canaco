from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Categoria, Publicacion


class HomeViewTests(TestCase):
    def test_search_only_returns_matching_published_news(self):
        categoria = Categoria.objects.create(nombre='Tecnología')
        matching = Publicacion.objects.create(
            titulo='Herramientas de IA',
            resumen='Inteligencia aplicada a empresas.',
            contenido='Contenido de prueba.',
            categoria=categoria,
            estado=Publicacion.ESTADO_PUBLICADO,
        )
        Publicacion.objects.create(
            titulo='Otra noticia',
            resumen='Sin relación con la búsqueda.',
            contenido='Contenido de prueba.',
            estado=Publicacion.ESTADO_PUBLICADO,
        )
        Publicacion.objects.create(
            titulo='Borrador de inteligencia',
            resumen='No debe aparecer en portada.',
            contenido='Contenido de prueba.',
            estado=Publicacion.ESTADO_BORRADOR,
        )

        response = self.client.get(reverse('home:index'), {'q': ' inteligencia '})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['search_query'], 'inteligencia')
        self.assertEqual(list(response.context['publicaciones']), [matching])
        self.assertEqual(list(response.context['categorias']), [categoria])


class ProfileViewTests(TestCase):
    def test_profile_displays_the_users_role(self):
        roles = (
            ('colaborador', False, False, 'Colaborador'),
            ('editor', True, False, 'Editor'),
            ('administrador', True, True, 'Administrador'),
        )

        for username, is_staff, is_superuser, expected_role in roles:
            with self.subTest(role=expected_role):
                user = User.objects.create_user(
                    username=username,
                    password='test-password',
                    is_staff=is_staff,
                    is_superuser=is_superuser,
                )
                self.client.force_login(user)

                response = self.client.get(reverse('home:perfil'))

                self.assertEqual(response.status_code, 200)
                self.assertContains(response, expected_role)
                self.client.logout()
