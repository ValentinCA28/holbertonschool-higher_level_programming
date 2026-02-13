# Python - Serialization

This project explores different serialization and deserialization techniques in Python, including JSON, Pickle, CSV, and XML formats.

## Description

Serialization is the process of converting a data structure or object into a format that can be stored or transmitted and reconstructed later. This project demonstrates various serialization methods used in Python applications.

## Learning Objectives

- Understand the concept of serialization and deserialization
- Work with JSON format for data interchange
- Use the Pickle module to serialize Python objects
- Convert CSV data to JSON format
- Implement XML serialization and deserialization
- Handle file I/O operations in Python
- Implement error handling for file operations

## Requirements

- Python 3.x
- All files are interpreted/compiled on Ubuntu
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- Code should use the pycodestyle (version 2.8.*)
- All files must be executable

## Project Structure

```
python-serialization/
├── task_00_basic_serialization.py    # JSON serialization
├── task_01_pickle.py                 # Pickle serialization with custom class
├── task_02_csv.py                    # CSV to JSON conversion
├── task_03_xml.py                    # XML serialization
├── data.json                         # Sample JSON data
├── data.csv                          # Sample CSV data
├── data.xml                          # Sample XML data
├── object.pkl                        # Sample pickle object
└── tests/                            # Test files
```

## Tasks

### 0. Basic Serialization

**File:** `task_00_basic_serialization.py`

Implements basic JSON serialization and deserialization functions:
- `serialize_and_save_to_file(data, filename)`: Serializes a Python dictionary to a JSON file
- `load_and_deserialize(filename)`: Loads and deserializes data from a JSON file

**Example:**
```python
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
serialize_and_save_to_file(data, "data.json")
loaded_data = load_and_deserialize("data.json")
```

### 1. Pickling Custom Classes

**File:** `task_01_pickle.py`

Demonstrates the use of Python's Pickle module to serialize and deserialize custom objects.

**Features:**
- `CustomObject` class with attributes: name, age, is_student
- `display()` method to print object details
- `serialize(filename)` method to save object to a file
- `deserialize(filename)` class method to load object from a file
- Error handling for file operations

**Example:**
```python
obj = CustomObject("Alice", 25, True)
obj.display()
obj.serialize("object.pkl")
loaded_obj = CustomObject.deserialize("object.pkl")
```

### 2. Converting CSV Data to JSON Format

**File:** `task_02_csv.py`

Converts CSV data to JSON format using Python's csv and json modules.

**Function:**
- `convert_csv_to_json(filename_csv)`: Reads a CSV file and converts it to JSON
  - Returns `True` if successful
  - Returns `False` if file is not found

**Example:**
```python
convert_csv_to_json("data.csv")
# Creates data.json with the converted data
```

### 3. Serializing and Deserializing with XML

**File:** `task_03_xml.py`

Implements XML serialization and deserialization using Python's `xml.etree.ElementTree` module.

**Functions:**
- `serialize_to_xml(dictionary, filename)`: Converts a Python dictionary to an XML file
- `deserialize_from_xml(filename)`: Reads an XML file and returns a Python dictionary

**Example:**
```python
data = {
    "name": "Bob",
    "age": "28",
    "city": "Paris"
}
serialize_to_xml(data, "data.xml")
loaded_data = deserialize_from_xml("data.xml")
```

## Usage

Each module can be imported and used independently:

```python
# JSON Serialization
from task_00_basic_serialization import serialize_and_save_to_file, load_and_deserialize

# Pickle Serialization
from task_01_pickle import CustomObject

# CSV to JSON
from task_02_csv import convert_csv_to_json

# XML Serialization
from task_03_xml import serialize_to_xml, deserialize_from_xml
```

## Testing

Test files are available in the `tests/` directory:
- `test_task_00_basic_serialization.py`
- `test_task_01_pickle.py`
- `test_task_02_csv.py`

Run tests using:
```bash
python3 -m pytest tests/
```

Or run individual test files:
```bash
python3 tests/test_task_00_basic_serialization.py
```

## Author

Holberton School Project

## License

This project is part of the Holberton School curriculum.
