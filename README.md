# 🌟 KouroshAsli Portfolio Website

A modern portfolio website built with Django, featuring a hacker theme and multilingual support.

<div align="center">
  <img src="static/images/portfolio-preview.png" alt="KouroshAsli Portfolio Preview" width="800px">
  <br>
  <a href="https://t.me/KouroshAsli">
    <img src="https://img.shields.io/badge/Telegram-@KouroshAsli-blue?style=flat-square&logo=telegram" alt="Telegram">
  </a>
  <a href="https://github.com/kouroshasli">
    <img src="https://img.shields.io/badge/GitHub-kouroshasli-black?style=flat-square&logo=github" alt="GitHub">
  </a>
</div>

## 🚀 Features

- 🌐 Bilingual Support (English & Swedish)
- 🎨 Modern Hacker-Style Theme
- 📱 Fully Responsive Design
- ⚡ Fast & Optimized Performance
- 🔄 Smooth Animations & Transitions
- 🌙 Dark Mode by Default
- 🔒 Secure Admin Panel
- 📝 Blog System
- 📬 Contact Form
- 🌍 Multi-language Support

## 🛠️ Tech Stack

- Python 3.x
- Django 5.0
- Bootstrap 5
- PostgreSQL
- HTML5/CSS3
- JavaScript

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/kouroshasli/portfolio.git
cd portfolio
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
EMAIL_HOST=your-email-host
EMAIL_PORT=your-email-port
EMAIL_HOST_USER=your-email
EMAIL_HOST_PASSWORD=your-email-password
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

8. Visit `http://127.0.0.1:8000` in your browser

## 🔧 Configuration

### Admin Panel
- URL: `http://127.0.0.1:8000/admin/`
- Default credentials:
  - Username: `kouroshasli`
  - Password: `1234`

### Translation Management
- URL: `http://127.0.0.1:8000/rosetta/`
- Access through admin panel

## 📁 Project Structure

```
portfolio/
├── kouroshasli/          # Project settings
├── main/                 # Main application
├── static/              # Static files
│   ├── css/
│   ├── js/
│   └── images/
├── templates/           # HTML templates
├── locale/             # Translation files
└── media/              # User uploaded files
```

## 🌐 Live Demo

Visit the live demo at: [https://kouroshasli.github.io](https://kouroshasli.github.io)

## 📞 Contact

- Telegram: [@KouroshAsli](https://t.me/KouroshAsli)
- GitHub: [kouroshasli](https://github.com/kouroshasli)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- Special thanks to all contributors
- Inspired by modern portfolio designs
- Built with ❤️ by KouroshAsli

---

<div align="center">
  Made with ❤️ by <a href="https://t.me/KouroshAsli">KouroshAsli</a>
</div>

# TK Project

This is a Django-based portfolio website.

## Features
- Modern UI
- Multi-language support
- Responsive design
- Contact form
- Project showcase

## Installation
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver` 