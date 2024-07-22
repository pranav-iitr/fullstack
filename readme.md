# Kuku FM Fullstack Assignment

This repository contains the fullstack assignment for Kuku FM, featuring a Django backend and a Next.js frontend with TypeScript.

## Project Structure

│<br>
├── backend/ # Django backend<br>
│ ├── manage.py<br>
│ ├── requirements.txt<br>
│ └── ... # other Django-related files and directories<br>
│<br>
└── frontend/ # Next.js frontend with TypeScript<br>
├── package.json<br>
├── tsconfig.json<br>
└── ... # other Next.js-related files and directories<br>


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

```plaintext
+-------------------+            +-------------------+           +------------------------+
|      Author       |            |       Genre       |           |       Audiobook        |
+-------------------+            +-------------------+           +------------------------+
| - id (PK)         |            | - id (PK)         |           | - id (PK)              |
| - name            |            | - name            |           | - title                |
+-------------------+            +-------------------+           | - author_id (FK)       |
                                                                  | - cover_image          |
                                                                  | - description          |
                                                                  | - average_rating       |
                                                                  | - total_reviews        |
                                                                  | - seo_title            |
                                                                  | - seo_description      |
                                                                  | - seo_keywords         |
                                                                  +------------------------+
                                                                                 |
                                                                                 |
+--------------------------------------+                                         |
|       Audiobook_Genre (Intermediate) |-----------------------------------------+
+--------------------------------------+
| - id (PK)                            |
| - audiobook_id (FK)                  |
| - genre_id (FK)                      |
+--------------------------------------+
```

## design insqiration
https://figma.com/design/3fiyEQRBcfXF08fFYT6h0V/Pixelz-Kit---Bookstore-Web?node-id=210-5622&t=dhY3ce452IYS6JKE-0

## Contac Details

For any questions or suggestions, please contact [pranavleo22@gmail.com](mailto:pranavleo22@gmail.comcom).
