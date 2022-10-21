import factory
from http import HTTPStatus

from base_test_class import TestViewSetBase
from factories import UserFactory


class TestUserViewSet(TestViewSetBase):
    basename = "users"
    user_attributes = factory.build(dict, FACTORY_CLASS=UserFactory)

    users_attributes = factory.build_batch(dict, FACTORY_CLASS=UserFactory, size=5)

    @staticmethod
    def expected_details(entity: dict, attributes: dict):
        return {**attributes, "id": entity["id"]}

    def test_create(self):
        user = self.create(self.user_attributes)
        expected_response = self.expected_details(user, self.user_attributes)
        assert user == expected_response

    def test_retrieve(self):
        user = self.create(self.user_attributes)
        expected_response = self.expected_details(user, self.user_attributes)
        response = self.retrieve(user["id"])
        assert response == expected_response

    def test_retrieve_list(self):
        user = self.retrieve(self.user.id)
        users_list = self.create_list(self.users_attributes)
        users_list.insert(0, user)
        response = self.retrieve_list()
        assert response == users_list

    def test_unauthorized_retrieve(self):
        user = self.create(self.user_attributes)
        response = self.unauthorized_retrieve(user["id"])
        expected_error = "Учетные данные не были предоставлены."
        assert response["detail"] == expected_error

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
