# Kuku FM Fullstack Assignment

This repository contains the fullstack assignment for Kuku FM, featuring a Django backend and a Next.js frontend with TypeScript.

## Project Structure

│
├── backend/ # Django backend
│ ├── manage.py
│ ├── requirements.txt
│ └── ... # other Django-related files and directories
│
└── frontend/ # Next.js frontend with TypeScript
├── package.json
├── tsconfig.json
└── ... # other Next.js-related files and directories


## Prerequisites

Ensure you have the following installed on your machine:
- Python 3.x
- Node.js and npm
- Docker (optional, for running the database in a container)

## Backend Setup (Django)

1. **Navigate to the backend directory:**

    ```sh
    cd backend
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required Python packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

## Frontend Setup (Next.js with TypeScript)

1. **Navigate to the frontend directory:**

    ```sh
    cd ../frontend
    ```

2. **Install the required npm packages:**

    ```sh
    npm install
    ```

3. **Run the development server:**

    ```sh
    npm run dev
    ```



## Usage

- Access the Django admin panel at `http://localhost:8000/admin`
- Access the Next.js frontend at `http://localhost:3000`

## Database Diagram

+-------------------+ +-------------------+ +---------------------+
| Author | | Genre | | Audiobook |
+-------------------+ +-------------------+ +---------------------+
| - id (PK) | | - id (PK) | | - id (PK) |
| - name | | - name | | - title |
+-------------------+ +-------------------+ | - author_id (FK) |
| - cover_image |
| - description |
| - average_rating |
| - total_reviews |
| - seo_title |
| - seo_description |
| - seo_keywords |
+---------------------+
|
|
+----------------------+----------------------+
| |
+-------------+ +-------------+
| audiobook_genre | | Author |
+-------------+ +-------------+
| - audiobook_id (FK) | | - audiobooks |
| - genre_id (FK) | +-------------+
+-------------+

## design insqiration
https://figma.com/design/3fiyEQRBcfXF08fFYT6h0V/Pixelz-Kit---Bookstore-Web?node-id=210-5622&t=dhY3ce452IYS6JKE-0


For any questions or suggestions, please contact [pranavleo22@gmail.com](mailto:pranavleo22@gmail.comcom).
