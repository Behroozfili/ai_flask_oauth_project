# 🚀 Flask AI API with Google OAuth & Hugging Face

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)
[![AI](https://img.shields.io/badge/AI-Hugging%20Face-orange.svg)](https://huggingface.co/)
[![OAuth](https://img.shields.io/badge/OAuth-Google-red.svg)](https://developers.google.com/identity)

> 🎯 **A modern Flask web application combining secure Google OAuth authentication with powerful AI-driven text classification using Hugging Face Transformers.**

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📦 Prerequisites](#-prerequisites)
- [🚀 Quick Start](#-quick-start)
- [🏗️ Project Structure](#️-project-structure)
- [🌐 API Endpoints](#-api-endpoints)
- [🤖 AI Model](#-ai-model)
- [🧪 Testing](#-testing)
- [🔧 Configuration](#-configuration)
- [🐳 Docker Deployment](#-docker-deployment)
- [🔮 Future Enhancements](#-future-enhancements)
- [🤝 Contributing](#-contributing)
- [📞 Contact](#-contact)
- [📄 License](#-license)

---

## ✨ Features

🔐 **Secure Authentication**
- Google OAuth 2.0 integration
- Session management
- Protected routes

🧠 **AI-Powered Analysis**
- Zero-shot text classification
- Facebook BART-large-MNLI model
- Real-time text analysis

🌐 **RESTful API**
- Clean API endpoints
- JSON responses
- Error handling

🐳 **Production Ready**
- Docker containerization
- Docker Compose setup
- Environment configuration

🧪 **Testing Suite**
- Pytest integration
- Unit tests included
- CI/CD ready

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| **Backend** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white) |
| **Authentication** | ![Google](https://img.shields.io/badge/Google_OAuth-4285F4?style=flat&logo=google&logoColor=white) |
| **AI/ML** | ![Hugging Face](https://img.shields.io/badge/🤗_Hugging_Face-FFD21E?style=flat) |
| **Containerization** | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white) |
| **Testing** | ![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat&logo=pytest&logoColor=white) |

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- 🐍 **Python 3.9+**
- 📦 **pip** (Python package installer)
- 🐳 **Docker & Docker Compose**
- ☁️ **Google Cloud Project** with OAuth 2.0 credentials

---

## 🚀 Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/flask-ai-api.git
cd flask-ai-api
```

### 2️⃣ Set Up Google OAuth

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Navigate to **APIs & Services** → **Credentials**
4. Create **OAuth 2.0 Client IDs**:
   - Application type: **Web application**
   - Authorized origins: `http://localhost:8000`
   - Redirect URIs: `http://localhost:8000/auth`

### 3️⃣ Configure Environment

Create a `.env` file in the project root:

```env
# Google OAuth Configuration
GOOGLE_CLIENT_ID="your_google_client_id_here"
GOOGLE_CLIENT_SECRET="your_google_client_secret_here"

# Flask Configuration
SECRET_KEY="your_super_secret_key_here"
FLASK_APP="app.main:create_app"
FLASK_ENV="development"
```

> 💡 **Tip**: Generate a secure secret key using:
> ```bash
> python -c 'import secrets; print(secrets.token_hex(24))'
> ```

### 4️⃣ Run with Docker (Recommended)

```bash
docker-compose up --build
```

### 4️⃣ Alternative: Local Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
flask run --host=0.0.0.0 --port=8000
```

🎉 **Success!** Your application is now running at `http://localhost:8000`

---

## 🏗️ Project Structure

```
flask-ai-api/
│
├── 📁 app/                    # Main application package
│   ├── 📄 __init__.py         # Package initialization
│   ├── 🧠 ai.py               # AI text analysis logic
│   ├── 🔐 auth.py             # OAuth authentication
│   ├── ⚙️ config.py           # Configuration management
│   ├── 🏭 main.py             # Flask app factory
│   └── 🛣️ routes.py           # API routes & endpoints
│
├── 📁 tests/                  # Test suite
│   └── 🧪 test_app.py         # Application tests
│
├── 🐳 Dockerfile              # Docker configuration
├── 🐙 docker-compose.yml      # Multi-container setup
├── 📋 requirements.txt        # Python dependencies
├── 🌍 .env.example            # Environment template
└── 📖 README.md               # This file
```

---

## 🌐 API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/` | Health check & welcome message | ❌ |
| `GET` | `/login` | Initiate Google OAuth flow | ❌ |
| `GET` | `/auth` | OAuth callback handler | ❌ |
| `GET` | `/analyze` | Display analysis form | ✅ |
| `POST` | `/analyze` | Perform text classification | ✅ |

### 📝 Example API Usage

**Text Analysis Request:**
```http
POST /analyze
Content-Type: application/x-www-form-urlencoded

text=I need help with my account login
```

**Response:**
```json
{
  "labels": ["Login"],
  "scores": [0.94],
  "sequence": "I need help with my account login"
}
```

---

## 🤖 AI Model

The application leverages the powerful **Facebook BART-large-MNLI** model for zero-shot text classification:

### 🎯 Classification Categories
- 🔑 **Login** - Authentication related queries
- ✍️ **Sign up** - Registration requests  
- 🆘 **Support** - Help and assistance
- ❓ **Question** - General inquiries
- 🚪 **Logout** - Session termination

### 🧠 How It Works
The model uses Natural Language Inference (NLI) to classify text without specific training on these exact categories, making it highly flexible and accurate.

---

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Local testing
pytest

# Docker testing
docker-compose run --rm app pytest

# With coverage
pytest --cov=app
```

---

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_CLIENT_ID` | Google OAuth Client ID | ✅ |
| `GOOGLE_CLIENT_SECRET` | Google OAuth Client Secret | ✅ |
| `SECRET_KEY` | Flask session encryption key | ✅ |
| `FLASK_APP` | Flask application entry point | ✅ |
| `FLASK_ENV` | Development/Production mode | ❌ |

---

## 🐳 Docker Deployment

### Development
```bash
docker-compose up --build
```

### Production
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Useful Docker Commands
```bash
# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild containers
docker-compose up --build --force-recreate
```

---

## 🔮 Future Enhancements

- [ ] 🎨 Modern React frontend
- [ ] 🗄️ Database integration (PostgreSQL)
- [ ] 🏷️ Custom label management
- [ ] 📊 Analytics dashboard
- [ ] 🔄 Rate limiting
- [ ] 🌐 Multi-language support
- [ ] 📱 Mobile API
- [ ] ☁️ Cloud deployment templates

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. 🍴 **Fork** the repository
2. 🌿 **Create** your feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 **Push** to the branch (`git push origin feature/AmazingFeature`)
5. 🔄 **Open** a Pull Request

### 📋 Development Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation
- Ensure Docker builds successfully

---

## 📞 Contact

**Behrooz Filzadeh**

[![Email](https://img.shields.io/badge/Email-behrooz.filzadeh@gmail.com-red?style=flat&logo=gmail&logoColor=white)](mailto:behrooz.filzadeh@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/behroozfilzadeh)

---



---

<div align="center">

**⭐ Star this repository if you found it helpful!**

[![GitHub stars](https://img.shields.io/github/stars/yourusername/flask-ai-api?style=social)](https://github.com/behroozfili/flask-ai-api/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/flask-ai-api?style=social)](https://github.com/behroozfili/flask-ai-api/network/members)

---

*Built with ❤️ by [Behrooz Filzadeh](mailto:behrooz.filzadeh@gmail.com)*

</div>
