import factory
from http import HTTPStatus

from base_test_class import TestViewSetBase
from factories import TaskFactory


class TestTaskViewSet(TestViewSetBase):
    basename = "task"
    task_attributes = factory.build(dict, FACTORY_CLASS=TaskFactory)
    
    tasks_attributes = factory.build_batch(dict, FACTORY_CLASS=TaskFactory, size=5)

    @staticmethod
    def expected_details(entity: dict, attributes: dict):
        return {**attributes, "id": entity["id"]}

    def test_create(self):
        task = self.create(self.task_attributes)
        expected_response = self.expected_details(task, self.task_attributes)
        assert task["description"] == expected_response["description"]

    def test_retrieve_list(self):
        tasks = self.create_list(self.tasks_attributes)
        response = self.retrieve_list()
        assert response == tasks

    def test_retrieve(self):
        task = self.create(self.task_attributes)
        response = self.retrieve(task["id"])
        expected_response = self.expected_details(task, self.task_attributes)
        assert response["id"] == expected_response["id"]

    def test_unauthorized_retrieve(self):
        task = self.create(self.task_attributes)
        response = self.unauthorized_retrieve(task["id"])
        expected_error = 'Учетные данные не были предоставлены.'
        assert response['detail'] == expected_error

    def test_update(self):
        task = self.create(self.task_attributes)
        new_data = {"deadline": "2022-12-31T09:18:55Z", "title": "I want to go on vacation"}
        expected_response = self.update(new_data, task["id"])
        updated_task = self.retrieve(task["id"])
        assert updated_task == expected_response

    def test_delete(self):
        task = self.create(self.task_attributes)
        expected_response = self.delete(task["id"])
        assert expected_response.status_code == HTTPStatus.NO_CONTENT
