# Minhashoras.API

Minhashoras.API is a Python API built using the Django framework, designed to help track the time spent on clients, projects, and tasks. This open-source project aims to provide an easy-to-use solution for managing time in a flexible and efficient manner. Users can register clients, projects, tasks, and log the time spent on each activity. It also allows generating reports on the total time spent per client, project, task, etc.

## Features

- Register clients, projects, and tasks
- Log time spent on each activity
- Generate time reports by client, project, task, and more
- Open-source and easy to integrate with other systems

## Installation

This project uses PIP for dependency management. Make sure you have Python and PIP installed on your machine. Then, follow the steps below to set up the TimeTrackingAPI:

1. Clone this repository:
```bash
git clone https://github.com/alcfernandes/minhashoras.api.git minhashoras-api
```

2. Navigate to the project directory:
```bash
cd minhashoras-api
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

- On Windows:
  ```
  .\venv\Scripts\activate
  ```

- On Linux/MacOS:
  ```
  source venv/bin/activate
  ```

5. Install the dependencies:
```bash
pip install -r requirements/local.txt
```

6. Apply migrations:
```bash
python manage.py migrate
```

7. Run the development server:
```bash
python manage.py runserver
```
The API should now be running on `http://127.0.0.1:8000/`.

## Usage
Please refer to the API documentation (available at `/docs` when running the development server) for detailed information on how to use the TimeTrackingAPI, including available endpoints and required parameters.

## Contributing
We welcome contributions from the community! Please feel free to submit issues, feature requests, or pull requests to help improve the TimeTrackingAPI.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.







