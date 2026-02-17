# HBnB Evolution

This repository contains the progressive development of the **HBnB Evolution** project. Unlike the standard console version, this project is architected into distinct layers and phases.

## 📂 Project Structure

### [Part 1: Technical Documentation](./part1/)
- **Focus:** Architecture design and business logic planning.
- **Output:** Detailed UML diagrams (Package, Class, Sequence) and flowcharts explaining the application layers.

### [Part 2: Business Logic & API](./part2/)
- **Focus:** Backend implementation using Python, Flask, and the Facade pattern.
- **Key Features:**
  - **RESTful API**: Endpoints for Users, Places, Reviews, and Amenities.
  - **Facade Pattern**: Abstraction layer between the API and the Business Logic.
  - **In-Memory Persistence**: A temporary storage system for development.
- **How to Run:** Navigate to the `part2` directory and follow the [Part 2 README](./part2/README.md).

### [Part 3: Database & Authentication](./part3/)
- **Focus:** Transitioning to persistent storage, securing the API, and refining relationships.
- **Key Features:**
  - **SQLAlchemy & SQLite**: Replaced in-memory storage with a relational database (SQLite for dev, adaptable to MySQL).
  - **JWT Authentication**: Secured endpoints using JSON Web Tokens via `Flask-JWT-Extended`.
  - **Security**: Password hashing using `bcrypt`.
  - **Complex Relationships**: Implemented One-to-Many and Many-to-Many relationships (e.g., Places ↔ Amenities).
- **How to Run:** Navigate to the `part3` directory and follow the [Part 3 README](./part3/README.md).

### [Part 4: Frontend Client](./part4/)
- **Focus:** Implementing a dynamic client-side interface to interact with the API.
- **Key Features:**
  - **Dynamic Content**: Uses JavaScript `fetch` API to load Places and Reviews without reloading the page.
  - **Secure Login**: Manages JWT tokens via browser cookies for authenticated actions.
  - **Interactive UI**: Users can view details and submit reviews in real-time.
  - **CORS Support**: Integrated with the backend to allow cross-origin requests.
- **How to Run:** Run `python3 -m http.server 8000` in the root directory and open `localhost:8000/part4/`.

## 🛠 Technologies
- **Language:** Python 3.x, JavaScript (ES6)
- **Framework:** Flask, Flask-RESTx, Flask-SQLAlchemy, Flask-JWT-Extended
- **Tools:** Git, Swagger UI, cURL, SQLite, HTML5, CSS3

## Authors
* **OWAYS Abdulhakim Aljbreen**
* **Bahathiq Mohammed Rateel**
* **Raghad Abdullah Nassef**
