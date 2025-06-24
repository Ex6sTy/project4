from rest_framework.test import APITestCase


class VehicleTestCase(APITestCase):

    def setUp(self):
        pass

    def test_create_car(self):
        """ Тестирование создания машины """
        data = {
            'title': 'Test',
            'description': 'Test'
        }
        self.client.post(
            '/cars/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'milage': [], 'title': 'Test', 'description': 'Test', 'owner': None}
        )

        self.assertTrue(
            Car.objects.all().exists()
        )

    def test_list_car(self):
        """ Тестирование списка машин """

        Car.objects.create(
            title='list test',
            description='list test',
        )
        response = self.client.get(
            '/cars/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'id': 2, 'milage': [], 'title': 'list test', 'description': 'list test', 'owner': None}]
        )