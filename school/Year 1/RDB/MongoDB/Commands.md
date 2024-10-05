# General
```json
use s32007 // Use specific database
show dbs // Show all dbs
use doc // Uses a doc of name 'doc', if it doesn't exist it "creates" it
show collections // Shows all collections
db.createCollection('Name')
```

# Inserting

```json
db.CollectionName.insertOne({"key": 5})
db.CollectionName.insertMany([{"key": 2}, {"key": 3}])
db.CollectionName.insertOne({
"key": val,
"key2": val2
})
```

# Find
```json
db.ColName.find() // Shows all documents that exist
db.ColName.find({key: 20})
db.ColName.findOne() // Shows first element
db.ColName.find({}, {key: 1}) // Shows only value when set to 1, 0 not display
db.ColName.updateOne({key: oldValue}, {$set: {key: newValue}})
db.ColName.deleteOne({key: value})
```

# Aggregate
```json
db.collection.aggregate([
	{$match: {key: {$gt: 4500}}}
])

db.collection.aggregate([
	{$match: {key: val}}, // Returns all columns that hold specified key
	{$limit: n} // How many columns to return, order matters
	{$sort: -1} // Reverse sort (DESC)
	{$sort: {key: 1}}
	{$count: key} // Returns how many of a value shows up
])

db.collection.aggregate([ // Aggregates based on average range, always needs _id
	// id decides which fields to sum up and group by
	{$group: {_id: key, averageVal: {$avg: "$val"}}}
	// Aggregate based on two distinct keys
	{$group: {_id: [key, key2], averageVal: {$avg: "$val"}}}
])

db.collection.aggregate( // Creates 'files' that store the result
[
{
	$facet {
		"Long Sort": [
			{$match: {key: {$gt: 3500}}},
			{$sort: {ranege: 1}}
		],
		"Short key": [
			{$match: {key: {$lte: 3500}}},
			{$sort: {key: 1}}
		]
	}
}])

db.collection.aggregate([
	{$project: {key: 1}} // Shows only key
])
```

# Look-Up
```json
db.collection.aggregate([
	{$lookup: // Matches on a foreign collection and adds a new key from the "as" field that contains the data of the foreign collection where it matches
	{
		from: collection,
		localField: local_key,
		foreignField: foreign_key,
		as: "new_key"	
	}
	}
])
```

# Updating
```json
db.collection.updateOne({"key": "Value"}, {$set: {"key": "value", "key2": "value2"}})
db.collection.updateOne({"key": "Value"}, {$unset: {"key": 1}) // Finds by first key, value
db.collection.updateMany({}, {}) // Updates many...
db.collection.updateOne({"key": "Value"}, {$addToSet: {"key": value}) // Add to array 
db.collection.updateOne({"key": "Value"}, {$pull: {"key": value}) // Remove from
db.collection.updateOne({"key": "Value"}, {$pop: {"key": -1}) // Remove first
db.collection.updateOne({"key": "Value"}, {$push: {"key": "value"}) // Add to end
```

# Deleting
```json
db.collection.deleteMany({"key", "value"})
```

# Dates
```json
$currentDate: {year: {$type: "date"}} // Date
$currentDate: {year: {$type: "timestamp"}} // In seconds
```