<h1 align="center">HolbertonBnB AirBnB clone</h1>
<p align="center">The Console</p>

<b align="center">Description</b>
This project is the first piece to cloning AirBnB. This is a back-end API that\
 (the console) handles objects and data.
<h3>Classes</h3>
<h3>BaseModel</h3>
This is the baseclass of the model from which all other classes inherit from.<br>
Ths class has three attributes:<br>
1.id<br>
2.created_at: type datetime<br>
3.updated_at: type datetime<br>

<h3>FileStorage</h3><br>
Inherits from BaseClass.
This represnts the storage engine that handles serialization and deserialization of data.
It serialiazes objects to json and saves them to a file. It also deserializes json data to objects

<h3>Amenity, City, Review, State, User:</h3><br>
These classes inherit from Baseclass and represent the data to be handled

<h3>Usage</h3><br>
To use the console in interactive mode, run the file console.py<br>
To use it non-interactivley, pipe any of the valid commands to console.py.


<h3>Valid Console Commands</h3><br>
```

* **show**
  * Usage: `show <class> <id>` or `<class>.show(<id>)`

Prints the string representation of a class instance based on a given id.

```


* **all**
  * Usage: `all` or `all <class>` or `<class>.all()`

Prints the string representations of all instances of a given class. If no
class name is provided, the command prints all instances of every class.

```

* **update**
  * Usage: `update <class> <id> <attribute name> "<attribute value>"` or
`<class>.update(<id>, <attribute name>, <attribute value>)` or `<class>.update(
<id>, <attribute dictionary>)`.

Updates a class instance based on a given id with a given key/value attribute
pair or dictionary of attribute pairs. If `update` is called with a single
key/value attribute pair, only "simple" attributes can be updated (ie. not
`id`, `created_at`, and `updated_at`). However, any attribute can be updated by
providing a dictionary.

```
```

* **show**
  * Usage: `show <class> <id>` or `<class>.show(<id>)`

Prints the string representation of a class instance based on a given id.

```

```
* **destroy**
  * Usage: `destroy <class> <id>` or `<class>.destroy(<id>)`

Deletes a class instance based on a given id. The storage file `file.json` 
is updated accordingly.

```

