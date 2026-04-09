# 🎮 GameCenter - Django 游戏中心项目

### [English]
A full-stack game database and review platform built with Django 5.2 and Bootstrap 5. It supports user registration, manual cover art management, and a dynamic community review system.

### [中文]
基于 Django 5.2 和 Bootstrap 5 开发的全栈游戏数据库与评论平台。支持用户注册登录、封面图片管理以及动态社区评论系统。

---

## ✨ Features | 主要功能

* **User System**: Secure Registration, Login, and Password Change functionality.
    * **用户系统**：安全的用户注册、登录及在线修改密码功能。
* **Game Database**: Browse games with high-quality manual cover art and platform tags (e.g., PC, PS5, Switch).
    * **游戏数据库**：浏览带有高质量手动封面图和平台标签（如 PC, PS5, Switch）的游戏列表。
* **Review System**: Authenticated users can post ratings and detailed comments for specific games.
    * **评论系统**：登录用户可以对特定游戏发表评分与详细评论。
* **Responsive UI**: Modern interface featuring purple gradient login pages and responsive card layouts.
    * **响应式 UI**：现代化界面，包含紫色渐变登录页与响应式卡片布局。

---

## 🚀 Quick Start | 快速部署指令

### 1. Clone the repository | 克隆仓库
```bash
git clone [https://github.com/yourusername/Django-GameCenter.git](https://github.com/yourusername/Django-GameCenter.git)
cd Django-GameCenter
```

### 2. Create a virtual environment | 创建虚拟环境
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
 ```

### 3. Install dependencies | 安装依赖
```bash
pip install -r requirements.txt
 ```
### 4. Set up the database | 设置数据库
```bash
python manage.py makemigrations
python manage.py migrate
 ```
### 5. Create a superuser | 创建管理员用户
```bash
python manage.py createsuperuser
 ```
### 6. Run the server | 运行服务器
```bash
python manage.py runserver
 ```
Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) start using your favorite browser to experience the game database and review platform!

## 📚 Tech Stack | 技术栈
* **Backend**: Django 5.2
* **Frontend**: Bootstrap 5, JavaScript
* **Database**: SQLite (Default)
* **Image Processing**: Pillow (Required for Cover Art management)

## 📂 Project Structure | 项目结构
* **/week3**: Contains the Django project files. 包含项目的核心文件。
* **/week3/game_center**: Contains the Django app files. 包含应用的核心文件。
* **/week3/game_center/templates**: Contains the HTML templates. 存放 HTML 模板。

## ❤ Contributing | 贡献指南
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.