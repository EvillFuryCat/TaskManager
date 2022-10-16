import factory
from http import HTTPStatus

from base_test_class import TestViewSetBase
from factories import UserFactory


class TestUserViewSet(TestViewSetBase):
    basename = "users"
    user_attributes = factory.build(dict, FACTORY_CLASS=UserFactory)

    @staticmethod
    def expected_details(entity: dict, attributes: dict):
        return {**attributes, "id": entity["id"]}

    def test_create(self):
        user = self.create(self.user_attributes)
        expected_response = self.expected_details(user, self.user_attributes)
        assert user == expected_response

    def test_retrieve_list(self):
        response = self.retrieve_list()
        assert response.status_code == HTTPStatus.OK, response.content

    def test_retrieve(self):
        user = self.create(self.user_attributes)
        expected_response = self.retrieve(user["id"])
        assert user == expected_response

    def test_unauthorized_retrieve(self):
        user = self.create(self.user_attributes)
        response = self.unauthorized_retrieve(user["id"])
        assert response.status_code == HTTPStatus.FORBIDDEN, response.content

    def test_update(self):
        user = self.create(self.user_attributes)
        new_data = {"username": "ScaryCat"}
        expected_response = self.update(new_data, user["id"])
        updated_user = self.retrieve(user["id"])
        assert updated_user == expected_response

    def test_delete(self):
        user = self.create(self.user_attributes)
        expected_response = self.delete(user["id"])
        assert expected_response.status_code == HTTPStatus.NO_CONTENT
