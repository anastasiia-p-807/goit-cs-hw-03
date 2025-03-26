from pymongo import MongoClient
from bson.objectid import ObjectId

class CatManager:
    def __init__(self, uri='mongodb://localhost:27017/', db_name='local', collection_name='cats'):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create_cat(self, name, age, features):
        cat = {"name": name, "age": age, "features": features}
        self.collection.insert_one(cat)
        print(f"Cat '{name}' added to the database.")

    def read_all(self):
        for cat in self.collection.find():
            print(cat)

    def read_cat_by_name(self, name):
        cat = self.collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Cat with the name '{name}' not found.")

    def update_cat_age(self, name, age):
        result = self.collection.update_one({"name": name}, {"$set": {"age": age}})
        if result.modified_count:
            print(f"Age of '{name}' updated to {age}.")
        else:
            print(f"Cat with the name '{name}' not found.")

    def add_feature_to_cat(self, name, feature):
        result = self.collection.update_one({"name": name}, {"$push": {"features": feature}})
        if result.modified_count:
            print(f"Feature '{feature}' added to '{name}'.")
        else:
            print(f"Cat with the name '{name}' not found.")

    def delete_cat_by_name(self, name):
        result = self.collection.delete_one({"name": name})
        if result.deleted_count:
            print(f"Cat '{name}' deleted from the database.")
        else:
            print(f"Cat with the name '{name}' not found.")

    def delete_all(self):
        result = self.collection.delete_many({})
        print(f"Deleted {result.deleted_count} records.")

if __name__ == "__main__":
    manager = CatManager()

    manager.create_cat("barsik", 3, ["wears slippers", "enjoys being pet", "ginger"])
    manager.create_cat("murzik", 5, ["playful", "likes water"])
    manager.create_cat("pushok", 2, ["calm", "soft fur", "loves children"])
    manager.create_cat("simba", 4, ["active", "sociable", "hunter"])
    manager.create_cat("leo", 6, ["lazy", "smart", "keeps order"])

    manager.read_all()
    manager.read_cat_by_name("barsik")
    manager.update_cat_age("barsik", 4)
    manager.add_feature_to_cat("barsik", "loyal")
    manager.delete_cat_by_name("murzik")
    
    #manager.delete_all()