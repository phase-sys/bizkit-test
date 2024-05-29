# BizKit Interview Task

**I have removed ```{"id": "1", "name": "John Doe", "age": 29, "occupation": "Developer"},``` in the read me file in both of the following test cases as it does not appear to be following the condition. It should show in the result as reflected in the following results:**

- **Request:** http://127.0.0.1:5000/search?id=5&name=Joe&age=30&occupation=Arc

  **Result:**
  ```
  [
    {"id": "2", "name": "Jane Doe", "age": 30, "occupation": "Engineer"},
    {"id": "3", "name": "Joe Doe", "age": 25, "occupation": "Designer"},
    {"id": "4", "name": "John Smith", "age": 28, "occupation": "Architect"},
    {"id": "5", "name": "Jane Smith", "age": 31, "occupation": "Manager"},
    {"id": "6", "name": "Joe Smith", "age": 24, "occupation": "Designer"}
  ]
  ```

- That means that with the examples above, the following request: http://127.0.0.1:5000/search?id=5&name=Joe&age=30&occupation=Arc, should return:

  ```
  [
    {"id": "5", "name": "Jane Smith", "age": 31, "occupation": "Manager"},
    {"id": "3", "name": "Joe Doe", "age": 25, "occupation": "Designer"},
    {"id": "6", "name": "Joe Smith", "age": 24, "occupation": "Designer"},
    {"id": "2", "name": "Jane Doe", "age": 30, "occupation": "Engineer"},
    {"id": "4", "name": "John Smith", "age": 28, "occupation": "Architect"}
  ]
  ```
