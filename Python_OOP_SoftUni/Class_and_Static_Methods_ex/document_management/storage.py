from typing import List

from more_itertools import first_true

from category import Category
from document import Document
from topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)
        else:
            raise ValueError('Category already exists')

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)
        else:
            raise ValueError('Topic already exists')

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)
        else:
            raise ValueError('Document already exists')

    def edit_category(self, category_id: int, new_name: str):
        category_to_edit = first_true(self.categories, None, lambda c: c.id_ == category_id)
        if category_to_edit:
            category_to_edit.name = new_name
        else:
            raise ValueError('Category not found')

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic_to_edit = first_true(self.topics, None, lambda t: t.id_ == topic_id)
        if topic_to_edit:
            topic_to_edit.topic = new_topic
            topic_to_edit.storage_folder = new_storage_folder
        else:
            raise ValueError('Topic not found')

    def edit_document(self, document_id: int, new_file_name: str):
        document_to_edit = first_true(self.documents, None, lambda d: d.id_ == document_id)
        if document_to_edit:
            document_to_edit.file_name = new_file_name
        else:
            raise ValueError('Document not found')

    def delete_category(self, category_id):
        category_to_delete = first_true(self.categories, None, lambda c: c.id_ == category_id)
        if category_to_delete:
            self.categories.remove(category_to_delete)
        else:
            raise ValueError('Category not found')

    def delete_topic(self, topic_id):
        topic_to_delete = first_true(self.topics, None, lambda t: t.id_ == topic_id)
        if topic_to_delete:
            self.topics.remove(topic_to_delete)
        else:
            raise ValueError('Topic not found')

    def delete_document(self, document_id):
        document_to_delete = first_true(self.documents, None, lambda d: d.id_ == document_id)
        if document_to_delete:
            self.documents.remove(document_to_delete)
        else:
            raise ValueError('Document not found')

    def get_document(self, document_id):
        document = first_true(self.documents, None, lambda d: d.id_ == document_id)
        if document:
            return document
        else:
            raise ValueError('Document not found')

    def __repr__(self):
        return '\n'.join([str(d) for d in self.documents])
