# SnapFlow

![项目预览](https://raw.githubusercontent.com/mmix574/SnapFlow/master/github_readme/1.png)

## 项目介绍

SnapFlow 是一个基于 Django 框架开发的社交媒体分享平台，专注于为用户提供图片分享和社交互动的服务。

### 主要功能
- 用户注册与认证系统
- 图片上传与分享
- 社交互动（关注、点赞、评论）
- 个人主页定制
- 图片标签系统
- 搜索功能
- 用户消息通知

### 技术栈
- 后端：Django 1.10.5
- API：Django REST framework 3.5.4
- 数据库：MySQL
- 分词系统：结巴分词
- 图片处理：Pillow

## 环境要求

- Python 3.x
- MySQL
- pip

## 安装配置

### 1. 系统依赖安装

```bash
sudo apt-get update
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
```

### 2. Python 依赖安装

```bash
pip install django==1.10.5
pip install djangorestframework==3.5.4  # 兼容 Django 1.10.5
pip install mysqlclient==1.4.6  # 稳定版本
pip install jieba==0.39
pip install Pillow==4.0.0
```

### 3. 数据库配置

登录 MySQL:
```bash
mysql -u root -p
```

#### 如遇到权限问题，执行以下 SQL:
```sql
-- 重置 root 用户
DROP USER 'root'@'localhost';
DROP USER 'root'@'%';

-- 创建新的 root 用户
CREATE USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';
CREATE USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '';

-- 授予权限
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;

-- 刷新权限
FLUSH PRIVILEGES;
```

#### 创建项目数据库:
```sql
CREATE DATABASE IF NOT EXISTS fflow CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 4. Django 项目配置

#### 运行数据库迁移
```bash
python manage.py migrate
python manage.py showmigrations
```

#### 创建超级用户
```bash
python manage.py createsuperuser
```

#### 收集静态文件
```bash
python manage.py collectstatic
```

#### 配置允许访问的主机
在 settings.py 中添加:
```python
ALLOWED_HOSTS = [
    'localhost',
    '192.168.1.5',
    'taita.xyz',
    '118.89.60.27',
    'snapflow.top'
]
```

### 5. 启动服务

```bash
python manage.py runserver 0.0.0.0:8000
```

## 访问项目

启动服务后，可通过以下地址访问：
- 本地访问：http://localhost:8000
- 局域网访问：http://[你的IP]:8000
- 后台管理：http://localhost:8000/admin

## 更多项目截图

![用户界面](https://raw.githubusercontent.com/mmix574/SnapFlow/master/github_readme/2.png)
![图片分享](https://raw.githubusercontent.com/mmix574/SnapFlow/master/github_readme/3.png)
![社交功能](https://raw.githubusercontent.com/mmix574/SnapFlow/master/github_readme/4.png)
![个人主页](https://raw.githubusercontent.com/mmix574/SnapFlow/master/github_readme/5.png)
![消息系统](https://raw.githubusercontent.com/mmix574/SnapFlow/master/github_readme/7.png)
![搜索功能](https://raw.githubusercontent.com/mmix574/SnapFlow/master/github_readme/8.png)

## 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进项目。

## 许可证

本项目采用 MIT 许可证，详情请参见 LICENSE 文件。	
