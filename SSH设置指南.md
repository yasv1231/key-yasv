# SSH密钥设置指南

## 🚀 快速开始

### 第一步：生成SSH密钥

1. 打开PowerShell或命令提示符
2. 运行以下命令（替换为您的邮箱）：
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

3. 按提示操作：
   - 按 `Enter` 使用默认文件位置 (`C:\Users\yasv\.ssh\id_ed25519`)
   - 输入密码（可选但推荐）
   - 再次确认密码

### 第二步：启动SSH代理（Windows）

**方法1：使用Git Bash（推荐）**
```bash
# 启动ssh-agent
eval "$(ssh-agent -s)"

# 添加SSH密钥
ssh-add ~/.ssh/id_ed25519
```

**方法2：使用PowerShell**
```powershell
# 设置ssh-agent服务为自动启动
Get-Service ssh-agent | Set-Service -StartupType Automatic

# 启动服务
Start-Service ssh-agent

# 添加SSH密钥
ssh-add C:\Users\yasv\.ssh\id_ed25519
```

### 第三步：复制公钥

```bash
# 显示公钥内容
cat ~/.ssh/id_ed25519.pub
```

或者使用PowerShell：
```powershell
Get-Content C:\Users\yasv\.ssh\id_ed25519.pub
```

### 第四步：添加到GitHub/GitLab

#### GitHub设置：
1. 登录GitHub
2. 点击右上角头像 → Settings
3. 左侧菜单选择 "SSH and GPG keys"
4. 点击 "New SSH key"
5. 粘贴公钥内容
6. 点击 "Add SSH key"

#### GitLab设置：
1. 登录GitLab
2. 点击右上角头像 → Preferences
3. 左侧菜单选择 "SSH Keys"
4. 粘贴公钥内容
5. 点击 "Add key"

### 第五步：测试连接

```bash
# 测试GitHub连接
ssh -T git@github.com

# 测试GitLab连接
ssh -T git@gitlab.com
```

成功会显示类似信息：
```
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

## 🔧 在Cursor中使用SSH

### 克隆仓库
```bash
git clone git@github.com:username/repository.git
```

### 添加远程仓库
```bash
# 查看当前远程仓库
git remote -v

# 添加SSH远程仓库
git remote add origin git@github.com:username/repository.git

# 或者修改现有远程仓库为SSH
git remote set-url origin git@github.com:username/repository.git
```

### 推送代码
```bash
git push -u origin main
```

## 🛠️ 常见问题解决

### 1. SSH代理问题
如果遇到ssh-agent问题，可以：
- 使用Git Bash而不是PowerShell
- 或者每次使用前手动添加密钥：`ssh-add ~/.ssh/id_ed25519`

### 2. 权限问题
确保SSH密钥文件权限正确：
```bash
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
```

### 3. 多个SSH密钥
如果有多个Git账户，可以创建SSH配置文件：
```bash
# 创建配置文件
nano ~/.ssh/config
```

添加内容：
```
# GitHub
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519

# GitLab
Host gitlab.com
    HostName gitlab.com
    User git
    IdentityFile ~/.ssh/id_ed25519
```

## 📝 在Cursor中的快捷操作

1. **打开终端**: `Ctrl + `` (反引号)
2. **源代码管理**: `Ctrl + Shift + G`
3. **命令面板**: `Ctrl + Shift + P`
4. **克隆仓库**: `Ctrl + Shift + P` → "Git: Clone"

## ✅ 验证设置

运行以下命令验证SSH设置：
```bash
ssh -T git@github.com
```

如果看到欢迎消息，说明SSH设置成功！
