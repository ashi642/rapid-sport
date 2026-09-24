# RAPID SPORT

### *SPORT YET CLASSY*

A modern sports e-commerce website built with **Python Django**, designed to provide a simple and user-friendly platform for browsing sports products, placing orders, and creating customized jerseys.

---

##  About the Project

**Rapid Sport** is a full-stack sports e-commerce web application developed using Django.

The platform allows customers to explore sports products, view product details, order products, and submit requests for customized jerseys. An administrative dashboard is included for managing products and orders.

The project focuses on combining a clean, responsive user interface with a structured Django backend and SQLite database.

---

##  Features

###  Home Page

* Attractive hero section
* Sports-focused navigation
* Featured products
* Best-selling products
* Product categories
* Responsive design

###  Product Shopping

* Browse available sports products
* Filter products by category
* View detailed product information
* Select product size
* Check product availability
* Add products to cart
* Update cart quantities
* Remove products from cart

###  Custom Jersey

* Create customized jersey requests
* Enter name and jersey number
* Select team
* Select size
* Upload team/logo image
* Submit customization request

###  Cart & Checkout

* Add products to cart
* Update quantities
* Remove products
* Checkout form
* Customer information collection
* Order confirmation

###  Order Management

* Customer order details
* Product and size information
* Quantity management
* Custom name and number
* Delivery address
* Order status tracking
* Pending, Shipped and Delivered statuses

###  Admin Management

* Django admin interface
* Manage products
* Manage orders
* Manage custom jersey requests
* Update order status
* Manage stock and product information

---

##  Technologies Used

| Technology           | Purpose                  |
| -------------------- | ------------------------ |
| **Python**           | Backend programming      |
| **Django**           | Web framework            |
| **HTML5**            | Page structure           |
| **CSS3**             | Styling                  |
| **Tailwind CSS**     | Responsive UI            |
| **JavaScript**       | Client-side interactions |
| **SQLite**           | Database                 |
| **Django Templates** | Frontend rendering       |
| **Pillow**           | Image processing         |
| **Git & GitHub**     | Version control          |

---

##  Project Architecture

```text
rapid-sport/
│
├── manage.py
│
├── rapid_sport/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── shop/
│   ├── migrations/
│   ├── templates/
│   │   └── shop/
│   ├── static/
│   │   └── shop/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── media/
│
├── .gitignore
├── requirements.txt
└── README.md
```

> **Note:** The `media/`, database, and virtual-environment files are excluded from version control through `.gitignore`.

---

##  Database Models

The application uses Django ORM with SQLite.

### Product

Stores sports product information including:

* Product name
* Category
* Price
* Size
* Stock
* Product image
* Description
* Featured status
* Creation date

### Order

Stores customer order information including:

* Customer name
* Phone number
* Product
* Size
* Quantity
* Custom name
* Custom number
* Address
* Order status
* Creation date

### CustomJersey

Stores customized jersey requests including:

* Customer name
* Phone number
* Name on jersey
* Jersey number
* Team
* Size
* Logo
* Request status

---

##  Product Categories

Rapid Sport supports multiple product categories:

*  Football
*  Cricket
*  Custom Jerseys
*  Accessories

---

##  Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ashi642/rapid-sport.git
```

Move into the project directory:

```bash
cd rapid-sport
```

---

### 2. Create a Virtual Environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

---

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

If `requirements.txt` is not available, install the main dependencies:

```powershell
pip install django pillow
```

---

### 4. Apply Database Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Create an Admin Account

```powershell
python manage.py createsuperuser
```

Follow the prompts to create your administrator account.

---

### 6. Run the Development Server

```powershell
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

---

##  Admin Dashboard

The project uses Django's built-in administration system to manage the application.

Administrators can:

* Add and edit products
* Manage product stock
* View customer orders
* Update order status
* Manage custom jersey requests
* Upload product images
* Manage product categories

---

##  User Interface

The frontend is built using:

* Django Templates
* HTML5
* CSS3
* Tailwind CSS
* JavaScript

The interface is designed to be responsive and accessible across desktop and mobile screen sizes.

---

##  Application Flow

```text
Customer
   │
   ▼
Home Page
   │
   ├── Browse Products
   │       │
   │       ▼
   │   Product Details
   │       │
   │       ▼
   │      Cart
   │       │
   │       ▼
   │    Checkout
   │       │
   │       ▼
   │   Order Placed
   │
   └── Custom Jersey
           │
           ▼
      Custom Request
```

---

##  Future Enhancements

Planned improvements include:

* Online payment integration
* Customer authentication
* Customer order history
* Product reviews and ratings
* Wishlist functionality
* Search and advanced filtering
* Email order notifications
* Improved inventory management
* Order tracking
* Deployment to a production server
* REST API integration

---

##  Security Considerations

For production deployment:

* Store Django `SECRET_KEY` in environment variables
* Configure `DEBUG=False`
* Configure allowed hosts
* Use HTTPS
* Protect database credentials
* Configure secure static and media file handling
* Use a production-ready database when required

---

##  Learning Outcomes

This project provided practical experience in:

* Django project and app development
* Python backend development
* Django ORM and database management
* CRUD operations
* Django templates
* Form handling
* File and image uploads
* Shopping cart implementation
* Order management
* Admin dashboard development
* Responsive frontend development
* Git and GitHub version control

---

##  Project

**Rapid Sport — Sport Yet Classy**

A Django-based sports e-commerce web application developed as a full-stack web development project.

---

##  License

This project is intended for educational and portfolio purposes.

---

 **If you find this project useful, consider giving the repository a star!**
