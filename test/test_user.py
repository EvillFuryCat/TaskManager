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

    def test_retrieve(self):
        user = self.create(self.user_attributes)
        response = self.retrieve(user)
        assert response.status_code == HTTPStatus.OK, response.content

    def test_update(self):
        new_username = {"username": "ScaryCat"}
        self.update(new_username)
        assert self.user.username == new_username["username"]

    def test_delete(self):
        new_user = self.create(self.user_attributes)
        response = self.delete(new_user)
        assert response.status_code == HTTPStatus.NO_CONTENT, response.conten