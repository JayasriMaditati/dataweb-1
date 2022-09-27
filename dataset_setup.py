import dataset

db = dataset.connect("sqlite:///shopping_list.db")

try:
    db.begin()
    db['list'].drop()
    table = db['list']
    items = [
        {"description":"apples"},
        {"description":"broccoli"},
        {"description":"pizza"},
        {"description":"tangerine"},
        {"description":"potatoes"},
        ]
    #for item in items:
    #    table.insert(item)
    table.insert_many(items)
    db.commit()
except Exception as e:
    db.rollback()

print("done.")
