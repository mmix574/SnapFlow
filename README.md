# SnapFlow
## 项目截图

![截图1](https://raw.githubusercontent.com/mmix574/SnapFlow/master/github_readme/1.png)
![截图2](https://raw.githubusercontent.com/mmix574/SnapFlow/master/github_readme/2.png)
![截图3](https://raw.githubusercontent.com/mmix574/SnapFlow/master/github_readme/3.png)
![截图4](https://raw.githubusercontent.com/mmix574/SnapFlow/master/github_readme/4.png)
![截图5](https://raw.githubusercontent.com/mmix574/SnapFlow/master/github_readme/5.png)
![截图7](https://raw.githubusercontent.com/mmix574/SnapFlow/master/github_readme/7.png)
![截图8](https://raw.githubusercontent.com/mmix574/SnapFlow/master/github_readme/8.png)

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
