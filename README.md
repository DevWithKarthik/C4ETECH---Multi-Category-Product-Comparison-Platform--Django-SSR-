📱 C4ETECH – Technology Product Comparison Platform

C4ETECH is a full-stack Django web application inspired by GSMArena, designed to showcase and compare modern technology products such as Smartphones, Laptops, Tablets, and Home Appliances.
The platform uses server-side rendering (SSR) with Django templates and a relational MySQL database to deliver dynamic, scalable, and maintainable content.

🚀 Key Features

🔹 Multi-Category Platform
Smartphones, Laptops, Tablets, and Home Appliances handled via separate Django apps.

🔹 Brand & Product Hierarchy
Clean relational structure using ForeignKey relationships:

Brand → Product → Overview → Key Specifications

🔹 Server-Side Rendering (SSR)
Dynamic pages rendered using Django templates for better SEO and performance.

🔹 Reusable UI Architecture
Common header, footer, and layout shared across all apps using Django template inheritance.

🔹 Responsive Design
Fully responsive UI built with HTML, CSS, and Bootstrap, optimized for desktop, tablet, and mobile screens.

🔹 Database-Driven Content
Product details dynamically loaded from MySQL, not hardcoded.

🔹 Custom Management Commands
Structured data population using Django management commands (populate_*) for brands, products, overviews, and key specs.

🛠 Tech Stack
    Frontend
        HTML5
        CSS3
        Bootstrap 5

    Django Templates (SSR)

    Backend
        Python
        Django Framework

    Database
        MySQL
    
    Tools
        VS Code
        Git & GitHub
        MySQL Workbench

🧠 What I Learned

    Designing normalized database schemas

    Implementing multi-app Django architecture

    Writing custom Django management commands

    Handling static files and media correctly

    Building SSR applications suitable for SEO

    Applying real-world backend logic using relational data

📌 Future Enhancements

    🔐 User authentication & login

    🔍 Advanced search & filtering

    ⭐ Product comparison feature

    📊 Admin dashboard improvements

    ☁️ Cloud deployment (AWS)



👨‍💻 Author

    Karthik M
    Python Full-Stack Developer
    📍 Erode, India