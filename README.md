📦 PhiMart - E-commerce API

PhiMart is a backend e-commerce API built with Django REST Framework (DRF).
It provides endpoints for managing products, categories, carts, and orders with JWT authentication powered by Djoser.
API documentation is available via Swagger UI using drf_yasg.

🚀 Features

🔐 JWT Authentication (Login, Register, Refresh)

🛍️ Products & Categories Management

🛒 Cart System (Add / Remove items)

📦 Orders API

📑 Swagger API Documentation

🛠️ Tech Stack

Django

Django REST Framework

Djoser
 (JWT Authentication)

drf-yasg
 (Swagger API Docs)

[SQLite / PostgreSQL] (Any supported DB)

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/phimart.git
cd phimart

2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Apply migrations
python manage.py migrate

5️⃣ Create superuser (for admin panel)
python manage.py createsuperuser

6️⃣ Run the development server
python manage.py runserver

🔑 Authentication

This project uses JWT Authentication with Djoser.
Endpoints include:

auth/jwt/create/ → Get access & refresh token

auth/jwt/refresh/ → Refresh access token

auth/jwt/verify/ → Verify token

📚 API Endpoints
Products & Categories

GET /api/products/ → List products

GET /api/products/{id}/ → Retrieve single product

GET /api/categories/ → List categories

Cart

POST /api/cart/ → Create / Add to cart

GET /api/cart/ → Get user cart

DELETE /api/cart/{id}/ → Remove item

Orders

POST /api/orders/ → Place order

GET /api/orders/ → Get user orders

📖 API Documentation

Once the server is running, open:

Swagger UI → http://127.0.0.1:8000/swagger/

ReDoc → http://127.0.0.1:8000/redoc/

📂 Project Structure
phimart/
│── product/         # Product & Category APIs
│── cart/            # Cart APIs
│── order/           # Order APIs
│── users/           # Authentication & User management
│── phimart/         # Project config
│── requirements.txt # Dependencies
│── manage.py

🤝 Contributing

Fork the repo

Create a new branch (feature/awesome-feature)

Commit your changes

Push to your branch

Open a Pull Request

📜 License

This project is licensed under the MIT License.