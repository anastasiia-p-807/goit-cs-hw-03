from pymongo import MongoClient
from bson.objectid import ObjectId

# Подключение к MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['cats_db']
collection = db['cats']

# Функции CRUD

# Create: Создание записи
def create_cat(name, age, features):
    cat = {"name": name, "age": age, "features": features}
    collection.insert_one(cat)
    print(f"Кот '{name}' добавлен в базу данных.")

# Read: Получить все записи
def read_all():
    for cat in collection.find():
        print(cat)

# Read: Получить запись по имени
def read_cat_by_name(name):
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Кот с именем '{name}' не найден.")

# Update: Обновить возраст кота по имени
def update_cat_age(name, age):
    result = collection.update_one({"name": name}, {"$set": {"age": age}})
    if result.modified_count:
        print(f"Возраст кота '{name}' обновлён до {age}.")
    else:
        print(f"Кот с именем '{name}' не найден.")

# Update: Добавить характеристику коту по имени
def add_feature_to_cat(name, feature):
    result = collection.update_one({"name": name}, {"$push": {"features": feature}})
    if result.modified_count:
        print(f"Характеристика '{feature}' добавлена коту '{name}'.")
    else:
        print(f"Кот с именем '{name}' не найден.")

# Delete: Удалить запись по имени
def delete_cat_by_name(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count:
        print(f"Кот '{name}' удалён из базы данных.")
    else:
        print(f"Кот с именем '{name}' не найден.")

def delete_all():
    result = collection.delete_many({})
    print(f"Удалено {result.deleted_count} записей.")

if __name__ == "__main__":
    create_cat("barsik", 3, ["ходит в капці", "дає себе гладити", "рудий"])
    create_cat("murzik", 5, ["игривый", "любить воду"])

    read_all()

    read_cat_by_name("barsik")

    update_cat_age("barsik", 4)

    add_feature_to_cat("barsik", "лояльный")

    delete_cat_by_name("murzik")

    delete_all()