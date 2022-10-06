class Topic:
    def __init__(self, id_: int, topic: str, storage_folder: str):
        self.id_ = id_
        self.topic = topic
        self.storage_folder = storage_folder

    def edit(self, new_topic: str, new_storage_folder: str):
        self.topic = new_topic
        self.storage_folder = new_storage_folder

    def __repr__(self):
        return f"Topic {self.id_}: {self.topic} in {self.storage_folder}"
