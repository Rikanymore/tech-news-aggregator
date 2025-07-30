# 📰 Tech News Aggregator
LAN-> EN
![Python](https://img.shields.io/badge/python-3.10+-blue)
![GitHub last commit](https://img.shields.io/github/last-commit/Rikanymore/tech-news-aggregator)
![GitHub repo size](https://img.shields.io/github/repo-size/Rikanymore/tech-news-aggregator)

A Python application that automatically collects tech news from multiple sources. Scrapes popular platforms like Hacker News, TechCrunch, and The Verge, stores in SQLite database, and serves via Flask web interface.

## ✨ Key Features
- Automated scraping from **3+ news sources**
- **SQLite** database integration
- Modern **Flask** web interface
- Daily auto-updates via **GitHub Actions**
- **Markdown report** generation

## 🚀 Quick Setup

### Prerequisites
- Python 3.10 or higher
- Git (optional)

```bash
# 1. Clone repo (or download)
git clone https://github.com/Rikanymore/tech-news-aggregator.git
cd tech-news-aggregator

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialize database and fetch news
python scraper/news_scraper.py

# 5. Launch web interface
python run.py
Open http://localhost:5000 in your browser

📂 Project Structure
text
tech-news-aggregator/
├── app/                  # Flask web interface
│   ├── templates/        # HTML templates
│   └── routes.py         # URL routing
├── database/             # Database operations
│   ├── models.py         # Database models
│   └── db.py             # DB operations
├── scraper/              # News scraping module
│   ├── config.py         # Site configurations
│   └── news_scraper.py   # Core scraping logic
├── config.py             # Flask settings
├── requirements.txt      # Python dependencies
└── run.py                # Application entry point
🔧 Configuration
Customize news sources in scraper/config.py:

python
SITES = {
    "Hacker News": {
        "url": "https://news.ycombinator.com",
        "selectors": {
            "container": "tr.athing",
            "title": "a.titlelink",
            "link": "a.titlelink"
        }
    },
    # Add new sources using this format
}
🤖 Auto-Update
Project automatically updates news daily (.github/workflows/scrape.yml):

yaml
on:
  schedule:
    - cron: '0 8 * * *'  # Daily at 08:00 UTC
📸 Screenshots
Web Interface	Terminal Output
https://via.placeholder.com/400x250?text=Flask+Web+Interface	https://via.placeholder.com/400x250?text=Scraper+Output
🙋 FAQ
Q: How to add new news source?
A: Add new site configuration in scraper/config.py

Q: Where is the database located?
A: Created as news.db in project root directory

👥 Contributing
Fork the repository

Create new branch (git checkout -b feature/my-feature)

Commit your changes (git commit -am 'Add some feature')

Push to branch (git push origin feature/my-feature)

Create Pull Request

📜 License
MIT License - See LICENSE file for details

# 📰 Tech News Aggregator

![Python](https://img.shields.io/badge/python-3.10+-blue)
![GitHub last commit](https://img.shields.io/github/last-commit/Rikanymore/tech-news-aggregator)
![GitHub repo size](https://img.shields.io/github/repo-size/Rikanymore/tech-news-aggregator)

A Python application that automatically collects tech news from multiple sources. Scrapes popular platforms like Hacker News, TechCrunch, and The Verge, stores in SQLite database, and serves via Flask web interface.

## ✨ Key Features
- Automated scraping from **3+ news sources**
- **SQLite** database integration
- Modern **Flask** web interface
- Daily auto-updates via **GitHub Actions**
- **Markdown report** generation

## 🚀 Quick Setup

### Prerequisites
- Python 3.10 or higher
- Git (optional)

```bash
# 1. Clone repo (or download)
git clone https://github.com/Rikanymore/tech-news-aggregator.git
cd tech-news-aggregator

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialize database and fetch news
python scraper/news_scraper.py

# 5. Launch web interface
python run.py
Open http://localhost:5000 in your browser

📂 Project Structure
text
tech-news-aggregator/
├── app/                  # Flask web interface
│   ├── templates/        # HTML templates
│   └── routes.py         # URL routing
├── database/             # Database operations
│   ├── models.py         # Database models
│   └── db.py             # DB operations
├── scraper/              # News scraping module
│   ├── config.py         # Site configurations
│   └── news_scraper.py   # Core scraping logic
├── config.py             # Flask settings
├── requirements.txt      # Python dependencies
└── run.py                # Application entry point
🔧 Configuration
Customize news sources in scraper/config.py:

python
SITES = {
    "Hacker News": {
        "url": "https://news.ycombinator.com",
        "selectors": {
            "container": "tr.athing",
            "title": "a.titlelink",
            "link": "a.titlelink"
        }
    },
    # Add new sources using this format
}
🤖 Auto-Update
Project automatically updates news daily (.github/workflows/scrape.yml):

yaml
on:
  schedule:
    - cron: '0 8 * * *'  # Daily at 08:00 UTC
📸 Screenshots
Web Interface	Terminal Output
https://via.placeholder.com/400x250?text=Flask+Web+Interface	https://via.placeholder.com/400x250?text=Scraper+Output
🙋 FAQ
Q: How to add new news source?
A: Add new site configuration in scraper/config.py

Q: Where is the database located?
A: Created as news.db in project root directory

👥 Contributing
Fork the repository

Create new branch (git checkout -b feature/my-feature)

Commit your changes (git commit -am 'Add some feature')

Push to branch (git push origin feature/my-feature)

Create Pull Request


LAN -> TR

# 📰 Tech News Aggregator

![Python](https://img.shields.io/badge/python-3.10+-blue)
![GitHub last commit](https://img.shields.io/github/last-commit/Rikanymore/tech-news-aggregator)
![GitHub repo size](https://img.shields.io/github/repo-size/Rikanymore/tech-news-aggregator)

Çoklu kaynaktan otomatik teknoloji haberleri toplayan Python uygulaması. Hacker News, TechCrunch ve The Verge gibi popüler kaynaklardan haber çeker, SQLite veritabanında saklar ve Flask web arayüzüyle sunar.

## ✨ Öne Çıkan Özellikler
- **3+ haber kaynağı**ndan otomatik çekim
- **SQLite** veritabanı entegrasyonu
- Modern **Flask** web arayüzü
- GitHub Actions ile **günlük otomatik güncelleme**
- Markdown formatında **rapor oluşturma**

## 🚀 Hızlı Kurulum

### Temel Gereksinimler
- Python 3.10 veya üzeri
- Git (opsiyonel)

```bash
# 1. Repoyu klonla (veya indir)
git clone https://github.com/Rikanymore/tech-news-aggregator.git
cd tech-news-aggregator

# 2. Sanal ortam oluştur ve aktif et
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows

# 3. Bağımlılıkları yükle
pip install -r requirements.txt

# 4. Veritabanını başlat ve haberleri çek
python scraper/news_scraper.py

# 5. Web arayüzünü başlat
python run.py
Tarayıcınızda http://localhost:5000 adresini açın

📂 Proje Yapısı
text
tech-news-aggregator/
├── app/                  # Flask web arayüzü
│   ├── templates/        # HTML şablonlar
│   └── routes.py         # URL yönlendirmeleri
├── database/             # Veritabanı işlemleri
│   ├── models.py         # Veritabanı modelleri
│   └── db.py             # DB operasyonları
├── scraper/              # Haber çekme modülü
│   ├── config.py         # Site konfigürasyonları
│   └── news_scraper.py   # Çekirdek scraping kodu
├── config.py             # Flask ayarları
├── requirements.txt      # Python bağımlılıkları
└── run.py                # Uygulama giriş noktası
🔧 Yapılandırma
Haber kaynaklarını özelleştirmek için scraper/config.py dosyasını düzenleyin:

python
SITES = {
    "Hacker News": {
        "url": "https://news.ycombinator.com",
        "selectors": {
            "container": "tr.athing",
            "title": "a.titlelink",
            "link": "a.titlelink"
        }
    },
    # Yeni kaynak eklemek için bu formatta ekleyin
}
🤖 Otomatik Güncelleme
Proje her gün otomatik olarak haberleri günceller (.github/workflows/scrape.yml):

yaml
on:
  schedule:
    - cron: '0 8 * * *'  # Her gün 08:00 UTC
📸 Ekran Görüntüleri
Web Arayüzü	Terminal Çıktısı
https://via.placeholder.com/400x250?text=Flask+Web+Interface	https://via.placeholder.com/400x250?text=Scraper+Output
🙋 SSS
S: Yeni haber kaynağı nasıl eklerim?
C: scraper/config.py dosyasına yeni site konfigürasyonu ekleyin

S: Veritabanını nerede bulabilirim?
C: Proje kök dizininde news.db olarak oluşur

👥 Katkıda Bulunma
Repoyu fork edin

Yeni branch oluşturun (git checkout -b feature/benim-ozelligim)

Değişikliklerinizi commit edin (git commit -am 'Yeni özellik eklendi')

Branch'i pushlayın (git push origin feature/benim-ozelligim)

GitHub üzerinden Pull Request açın

📜 Lisans
MIT Lisansı - Detaylar için LICENSE dosyasına bakın

🌟 Proje aktif olarak geliştirilmektedir. Öneri ve hata bildirimleriniz için issue açabilirsiniz.

text

### GitHub'a Eklerken Dikkat Edilecekler:
1. **Markdown Özellikleri**:
   - Başlıklar için `#`, `##`, `###` kullanın
   - Kod blokları için ``` kullanın
   - Tablo ve liste formatlarını koruyun

2. **Resim Ekleme**:
   - `![Web Preview](https://...)` kısmını kendi ekran görüntülerinizle değiştirin
   - Görselleri [ImgBB](https://imgbb.com/) gibi bir servise yükleyebilirsiniz

3. **Kişiselleştirme**:
   - `Rikanymore` yazan yerleri kendi kullanıcı adınızla değiştirin
   - Özellikleri projenize göre güncelleyin

Bu README, projenizin:
- **Kurulumunu**
- **Kullanımını**
- **Mimarisini**
- **Katkı süreçlerini**

profesyonel şekilde anlatacaktır. GitHub'da render edildiğinde mükemmel görünecektir! 😊
