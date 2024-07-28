# Bookstore Project

Welcome to the Bookstore Project! This project is designed to help you learn Django and understand its core concepts through a practical application. Below you'll find detailed information on the project's setup, features, and usage.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [API Documentation](#api-documentation)
7. [Learning Outcomes](#learning-outcomes)
8. [Contributing](#contributing)
9. [License](#license)

## Project Overview

The Bookstore Project is a web application developed using Django. It features a dynamic interface for browsing and managing a collection of books. The project includes user authentication, book listings, and a user profile section that demonstrates the use of REST APIs and Ajax for asynchronous data fetching.

## Features

- **User Authentication**: Register, login, and manage user accounts.
- **Book Listings**: View, add, edit, and delete book entries.
- **User Profiles**: Update user profile information using REST APIs and Ajax.
- **Django Templates**: Render dynamic HTML content using Django templates.
- **Class-Based and Functional Views**: Compare and understand the use of both types of views in Django.
- **API Documentation with Swagger**: Interactive API documentation generated using Swagger.

## Technologies Used

- **Django**: Web framework for developing the application.
- **Django REST Framework**: For building RESTful APIs.
- **Swagger**: For API documentation.
- **Ajax**: For asynchronous data fetching and updating user profiles.
- **SQLite**: Default database for development.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/bookstore-project.git
    cd bookstore-project
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

6. **Open your browser** and navigate to `http://127.0.0.1:8000`.

## Usage

- **Homepage**: Browse the list of books.
- **User Registration/Login**: Create a new account or log in to an existing account.
- **Book Management**: Add, edit, and delete books from your collection.
- **Profile Management**: Update your profile information using the user profile page.

## API Documentation

### User Profile API

- **GET /api/profile/**: Retrieve user profile information.
- **PUT/PATCH /api/profile/**: Update user profile information.

### Example AJAX Request

```javascript
$.ajax({
    url: '/api/profile/',
    type: 'GET',
    success: function(data) {
        console.log(data);
    }
});
```

## Learning Outcomes

By working on this project, you'll gain a better understanding of:

- Django's class-based and functional views.
- Working with Django templates for dynamic content rendering.
- Building and consuming RESTful APIs using Django REST Framework.
- Using Ajax for asynchronous operations in web applications.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize the sections further to fit your project and preferences!

