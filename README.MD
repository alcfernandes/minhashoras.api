# MinhasHoras.API
[![Maintainability](https://api.codeclimate.com/v1/badges/63de08d06582d8cb4ca5/maintainability)](https://codeclimate.com/github/alcfernandes/minhashoras.api/maintainability)

Project documentation available at
[MinhasHoras.docs](https://minhashoras.readthedocs.io).

MinhasHoras.API is a Python API built using the Django framework, designed to help track the time spent on clients, 
projects, and tasks. This API will serve a web client that aims to provide a simple solution for managing time where 
users can register clients, projects, tasks, log the time spent on each activity, and generate reports on the total time
spent per client, project, task, etc.

## Disclaimer

This project serves as a laboratory for the implementation of best practices in software project design and development. This project focuses particularly on the development of APIs using Python and Django. Our primary objective is to create a well-structured and maintainable codebase, ensuring the use of effective coding standards and techniques.

Please note that this application is a **work in progress**, and is not yet a finished product. It is continuously being refined and improved, with a strong emphasis on implementing and experimenting with best practices in the software development lifecycle.

## Project Goals

1. Demonstrate the application of best practices in project management and software development.
2. Create a scalable, maintainable, and efficient codebase using Python and Django.
3. Design and develop APIs adhering to RESTful principles and other widely accepted standards.

## Current Status

This project is currently under active development. Contributions, suggestions, and feedback are welcomed and appreciated. As we work on refining and expanding the application, we will continue to apply and explore best practices to ensure the highest quality of code and functionality.

As a reminder, this application is not a finished product, and its primary purpose is to serve as a learning and experimentation platform for developers interested in honing their skills and understanding of best practices in software development, particularly in the context of Python, Django, and API development.

Thank you for visiting our project repository. We hope you find it useful and informative, and we welcome your contributions to our ongoing journey towards


## Main Features

- Register clients, projects, and tasks
- Log time spent on each activity
- Generate time reports by client, project, task, and more

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
Please refer to the API documentation (available at `/api/schema/swagger-ui/` when running the development server) for detailed information on how to use the Minhashoras API, including available endpoints and required parameters.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.







