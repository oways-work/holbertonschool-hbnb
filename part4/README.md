# HBnB Evolution - Part 4: Frontend Client

This directory contains the client-side application for the HBnB project. It uses vanilla JavaScript to interact with the backend API dynamically, providing a responsive user experience without page reloads.

## 🌟 Features
- **User Authentication:** Implements secure Login using JWT (JSON Web Tokens).
- **Dynamic Content Loading:** Fetches Places and Reviews from the API using the `fetch` API.
- **Review System:** Allows authenticated users to post reviews for properties in real-time.
- **Responsive Design:** A clean, grid-based layout using CSS3 that adapts to different screen sizes.
- **Security:** Handles token storage in browser cookies (`token=...`) for session management.

## 📁 File Structure
- `index.html`: The main landing page displaying the grid of all available places.
- `login.html`: The user login interface.
- `place.html`: A detailed view for a specific property (Place).
- `add_review.html`: The form for submitting a new review.
- `assets/js/scripts.js`: The core logic file. It handles:
  - API calls (GET/POST).
  - DOM manipulation to inject HTML.
  - Cookie management for JWTs.
- `assets/css/styles.css`: Global styling for consistent layout (margins, padding, colors).

## 🔧 How It Works
1. **Authentication Flow:**
   - User enters credentials -> `POST /api/v1/auth/login`.
   - Server returns an `access_token`.
   - JavaScript saves this token in a cookie.
   python3 -m http.server 8000server:t.our backend is already running on port 5000): `Authorization` header.

# HBnB Evolution - Part 4: Frontend Client

This directory contains the client-side application for the HBnB project. It uses vanilla JavaScript to interact with the backend API dynamically, providing a responsive user experience without page reloads.

## 🌟 Features
- **User Authentication:** Implements secure Login using JWT (JSON Web Tokens).
- **Dynamic Content Loading:** Fetches Places and Reviews from the API using the `fetch` API.
- **Review System:** Allows authenticated users to post reviews for properties in real-time.
- **Responsive Design:** A clean, grid-based layout using CSS3 that adapts to different screen sizes.
- **Security:** Handles token storage in browser cookies (`token=...`) for session management.

## 📁 File Structure
- `index.html`: The main landing page displaying the grid of all available places.
- `login.html`: The user login interface.
- `place.html`: A detailed view for a specific property (Place).
- `add_review.html`: The form for submitting a new review.
- `assets/js/scripts.js`: The core logic file. It handles:
  - API calls (GET/POST).
  - DOM manipulation to inject HTML.
  - Cookie management for JWTs.
- `assets/css/styles.css`: Global styling for consistent layout (margins, padding, colors).

## 🔧 How It Works
1. **Authentication Flow:**
   - User enters credentials -> `POST /api/v1/auth/login`.
   - Server returns an `access_token`.
   - JavaScript saves this token in a cookie.
   python3 -m http.server 8000server:t.our backend is already running on port 5000): `Authorization` header.
