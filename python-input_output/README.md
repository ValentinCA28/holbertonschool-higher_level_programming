# Python - Input/Output

This project explores file input/output operations and JSON serialization in Python, covering reading, writing, and manipulating files and JSON data.

## Description

File handling is a crucial part of programming. This project demonstrates various techniques for working with files in Python, including reading and writing text files, working with JSON data format, and serializing Python objects.

## Learning Objectives

- How to open, read, write and close files in Python
- Understanding file modes (read, write, append)
- Working with the `with` statement for file handling
- Converting Python objects to JSON format and vice versa
- Understanding JSON serialization and deserialization
- Using the `json` module (`json.dump()`, `json.dumps()`, `json.load()`, `json.loads()`)
- Serializing class instances to JSON
- Working with command-line arguments using `sys.argv`

## Requirements

- Python 3.x
- All files are interpreted/compiled on Ubuntu
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use the pycodestyle (version 2.8.*)
- All files must be executable
- All modules should have documentation
- All classes should have documentation
- All functions should have documentation

## Project Structure

```
python-input_output/
├── 0-read_file.py              # Read and print file contents
├── 1-write_file.py             # Write text to a file
├── 2-append_write.py           # Append text to a file
├── 3-to_json_string.py         # Convert object to JSON string
├── 4-from_json_string.py       # Parse JSON string to object
├── 5-save_to_json_file.py      # Save object to JSON file
├── 6-load_from_json_file.py    # Load object from JSON file
├── 7-add_item.py               # Script to add items to a JSON list
├── 8-class_to_json.py          # Convert class instance to dict
├── 9-student.py                # Student class with JSON conversion
└── 10-student.py               # Student class with filtered JSON
```

## Tasks

### 0. Read file

**File:** `0-read_file.py`

Function that reads a text file (UTF-8) and prints it to stdout.

**Prototype:** `def read_file(filename=""):`

**Example:**
```python
read_file("my_file_0.txt")
```

---

### 1. Write to a file

**File:** `1-write_file.py`

Function that writes a string to a text file (UTF-8) and returns the number of characters written.

**Prototype:** `def write_file(filename="", text=""):`

**Features:**
- Creates the file if it doesn't exist
- Overwrites the content if the file exists
- Returns the number of characters written

**Example:**
```python
nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)  # Output: 29
```

---

### 2. Append to a file

**File:** `2-append_write.py`

Function that appends a string at the end of a text file (UTF-8) and returns the number of characters added.

**Prototype:** `def append_write(filename="", text=""):`

**Features:**
- Creates the file if it doesn't exist
- Appends to the end if the file exists
- Returns the number of characters added

**Example:**
```python
nb_characters = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters)
```

---

### 3. To JSON string

**File:** `3-to_json_string.py`

Function that returns the JSON representation of an object (string).

**Prototype:** `def to_json_string(my_obj):`

**Example:**
```python
my_list = [1, 2, 3]
s = to_json_string(my_list)
print(s)  # Output: [1, 2, 3]
print(type(s))  # Output: <class 'str'>
```

---

### 4. From JSON string to Object

**File:** `4-from_json_string.py`

Function that returns a Python object represented by a JSON string.

**Prototype:** `def from_json_string(my_str):`

**Example:**
```python
s = '[1, 2, 3]'
my_list = from_json_string(s)
print(my_list)  # Output: [1, 2, 3]
print(type(my_list))  # Output: <class 'list'>
```

---

### 5. Save Object to a file

**File:** `5-save_to_json_file.py`

Function that writes an Object to a text file, using JSON representation.

**Prototype:** `def save_to_json_file(my_obj, filename):`

**Example:**
```python
my_dict = { 'id': 12, 'name': "John", 'places': ["San Francisco", "Tokyo"] }
save_to_json_file(my_dict, "my_dict.json")
```

---

### 6. Create object from a JSON file

**File:** `6-load_from_json_file.py`

Function that creates an Object from a JSON file.

**Prototype:** `def load_from_json_file(filename):`

**Example:**
```python
obj = load_from_json_file("my_dict.json")
print(obj)
print(type(obj))
```

---

### 7. Load, add, save

**File:** `7-add_item.py`

Script that adds all arguments to a Python list, and then saves them to a file.

**Features:**
- Uses `save_to_json_file` and `load_from_json_file` functions
- Saves to `add_item.json`
- Creates the file if it doesn't exist
- Appends arguments to existing list

**Usage:**
```bash
./7-add_item.py "Best" "School"
./7-add_item.py "Python" "is" "cool"
cat add_item.json
# Output: ["Best", "School", "Python", "is", "cool"]
```

---

### 8. Class to JSON

**File:** `8-class_to_json.py`

Function that returns the dictionary description with simple data structure for JSON serialization of an object.

**Prototype:** `def class_to_json(obj):`

**Features:**
- Returns the `__dict__` of the object
- Works with serializable attributes (list, dict, string, integer, boolean)

**Example:**
```python
from 8-my_class import MyClass

m = MyClass("John")
m.number = 89
print(type(m))  # Output: <class '8-my_class.MyClass'>
print(m)

mj = class_to_json(m)
print(type(mj))  # Output: <class 'dict'>
print(mj)
```

---

### 9. Student to JSON

**File:** `9-student.py`

Class `Student` that defines a student with JSON serialization capability.

**Attributes:**
- `first_name`
- `last_name`
- `age`

**Methods:**
- `__init__(self, first_name, last_name, age)`: Initializes a student
- `to_json(self)`: Returns the dictionary representation of Student instance

**Example:**
```python
students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

for student in students:
    j_student = student.to_json()
    print(type(j_student))  # Output: <class 'dict'>
    print(j_student)
```

---

### 10. Student to JSON with filter

**File:** `10-student.py`

Class `Student` with enhanced JSON serialization that can filter attributes.

**Methods:**
- `to_json(self, attrs=None)`: Returns dictionary representation
  - If `attrs` is a list of strings, only attributes contained in this list are retrieved
  - Otherwise, all attributes are retrieved

**Example:**
```python
student = Student("John", "Doe", 23)

# Get all attributes
j_student = student.to_json()
print(j_student)  # Output: {'first_name': 'John', 'last_name': 'Doe', 'age': 23}

# Get only specific attributes
j_student = student.to_json(['first_name', 'age'])
print(j_student)  # Output: {'first_name': 'John', 'age': 23}
```

---

## Usage Examples

### Reading Files
```python
from 0-read_file import read_file
read_file("my_file.txt")
```

### Writing Files
```python
from 1-write_file import write_file
from 2-append_write import append_write

write_file("output.txt", "Hello, World!\n")
append_write("output.txt", "Appended text\n")
```

### JSON Operations
```python
from 3-to_json_string import to_json_string
from 4-from_json_string import from_json_string
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Convert to JSON string
data = {"name": "Alice", "age": 30}
json_str = to_json_string(data)

# Convert from JSON string
obj = from_json_string(json_str)

# Save to file
save_to_json_file(data, "data.json")

# Load from file
loaded_data = load_from_json_file("data.json")
```

### Working with Classes
```python
from 9-student import Student
from 8-class_to_json import class_to_json

student = Student("Bob", "Smith", 25)
student_dict = student.to_json()
print(student_dict)

# Using class_to_json function
generic_dict = class_to_json(student)
```

## Key Concepts

### The `with` Statement
The `with` statement ensures proper acquisition and release of resources:
```python
with open("file.txt", "r") as f:
    content = f.read()
# File is automatically closed after the block
```

### File Modes
- `"r"` - Read (default)
- `"w"` - Write (overwrites)
- `"a"` - Append
- `"r+"` - Read and write

### JSON Module
- `json.dumps(obj)` - Convert object to JSON string
- `json.loads(str)` - Convert JSON string to object
- `json.dump(obj, file)` - Write object to file as JSON
- `json.load(file)` - Read JSON from file and convert to object

## Author

Holberton School Project

## License

This project is part of the Holberton School curriculum.
