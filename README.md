# AirBnB Clone
## Description
This is a simple AirBnB clone built on python. The project is still ongoing, presently models have been created for the airbnb products, a file storage system is incoprorated to persist data through sessions and a console have been built with basic commands to help users interact with the storage system.

## How to start the console
To start the console, follow these steps:
- First, clone the repo, you need not install any extra package, all packages used are builtins in python.
- From the project root directory, simply run the ``console.py`` file.On a bash shell, you could simple use ``./console.py``
## Commands recognised by the console
1. help

   The help command prints a list of all possible commands. The help command followed by a command prints the help text for that command. You can use this to see info on how to use these commands (or follow through here).
```
   Usage:

	(hbnb) help

	(hbnb) help <command>
```
2. quit

   The quit command quits the console.
```
   Usage:

	(hbnb) quit
```
3. create

   Creates a new instance of a class and saves it to storage. Also, prints the id of the new instance.
```
   Usage:

	(hbnb) create <classname>
```
4. show

   Prints the string representation of an instance based on the class name and id
```
   Usage:

	(hbnb) show <classname> <id>
```
5. all

   Prints the string representation of all instances based on the classname passed as an argument.
```
   Usage:

	(hbnb) all <classname>

	Classname is optional, default is BaseModel
```
6. update

   Updates an instance based on the class name and id by adding or updating attribute.
   When ``id``, ``created_at``, ``updated_at`` are passed as attribute name, no update action is carried out as these attributes cannot be updated.
```
   Usage:

	(hbnb) update <class name> <id> <attribute name> "<attribute value>"
```
7. Destroy

   Deletes an instance based on the class name and id
```
   Usage:

	(hbnb) destroy <class name> <id>
```
## Extras
For now, the classnames recognised by the console are _*BaseModel*_, _*User*_, _*State*_, _*City*_, _*Amenity*_, _*Place*_, and _*Review*_. The console is case-sensitive, so these names, when used, should be used exactly as seen.
## Contributors
[Jerry Wonder](https://github.com/JerryWonder2126)

[Charles Ezebuike](https://github.com/zunique90)
