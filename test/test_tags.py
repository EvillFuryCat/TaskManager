import factory
from http import HTTPStatus

from base_test_class import TestViewSetBase
from factories import TagFactory


class TestTagViewSet(TestViewSetBase):
    basename = "tags"
    tag_attributes = factory.build(dict, FACTORY_CLASS=TagFactory)

    tags_attributes = factory.build_batch(dict, FACTORY_CLASS=TagFactory, size=5)

    @staticmethod
    def expected_details(entity: dict, attributes: dict):
        return {**attributes, "id": entity["id"]}

    def test_create(self):
        tag = self.create(self.tag_attributes)
        expected_response = self.expected_details(tag, self.tag_attributes)
        assert tag == expected_response

    def test_retrieve(self):
        tag = self.create(self.tag_attributes)
        expected_response = self.expected_details(tag, self.tag_attributes)
        response = self.retrieve(tag["id"])
        assert response == expected_response

    def test_retrieve_list(self):
        tags = self.create_list(self.tags_attributes)
        response = self.retrieve_list()
        assert response == tags

    def test_unauthorized_retrieve(self):
        tag = self.create(self.tag_attributes)
        response = self.unauthorized_retrieve(tag["id"])
        expected_error = "Учетные данные не были предоставлены."
        assert response["detail"] == expected_error

    def test_update(self):
        tag = self.create(self.tag_attributes)
        new_data = {"title": "DRAKONKAPUSTA"}
        expected_response = self.update(new_data, tag["id"])
        updated_tag = self.retrieve(tag["id"])
        assert updated_tag == expected_response

    def test_delete(self):
        tag = self.create(self.tag_attributes)
        expected_response = self.delete(tag["id"])
        assert expected_response.status_code == HTTPStatus.NO_CONTENT
