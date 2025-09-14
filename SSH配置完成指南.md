# 🔐 SSH配置完成指南

## ✅ 已完成的步骤
- [x] 生成SSH密钥对
- [x] 创建SSH目录

## 📋 您的SSH公钥
```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCqwD4xUKTA0fGaSm5xmrTqHdzT5jrDEMpnGJG31J1EEBEaTh7ocZ/5qkRqU6M6hHcH+0AhKY6LSyi06ktkucWAavAbdyfbpU4dGgm9kKxr/DDNGRyrXf0acCykCIaD+Yf8n/4jU7Ig4KqE/9b3P15hc2tMjf+08Z8nTOXPdzMloAP9uDw9XLkxGr6fmPdXP7bqHsNrsMxoQdtz/ohW4LsGmqZsBkUrOzzRBAPVwBPIt7ysCKu494YSmjGcqv8sqS6ez3sJ4WZufOgJEW0L5kJAil7PoInvYqVmB81+mtxPmzFkic/wu+I4SltXYTweS1/kEkiJH24wcUeA3J3t83RDvcGY11+bWfoy20QOUsYxwt0MfriUXcPrqPNHoOitsseEc+LNt/3ZPSnNrvjCm1ttUqXDTQ+vZGMdJRqpstb/NIjwNWlJWOPNXo6VMLCfqU7hTlYoFfJRh2MWr8NHWExuU0Cy/ka73YtfoBRpT26XPFBF/+8ysTrhwpz6VVA1v/UgbNxV/dYRmJDGZcizagJn14rVJGOI5EjlRNuLQ9U1dVvcJHTxoKgT3GhjOAI99pq6JzcmyXUtGF90q8mVkzb/1JMhc35R2TW+5mm0TogB8CBrjEQfDqVN7bpvb5VRF94iRCDwUbcVkGQJgnMxtsKgIUDS2bWeFhsHIOL8nKFvgWw== yasv@example.com
```

## 🚀 下一步操作

### 1. 添加公钥到GitHub
1. 访问：https://github.com/settings/keys
2. 点击 "New SSH key"
3. 标题：`Cursor Git Management`
4. 粘贴上面的公钥
5. 点击 "Add SSH key"

### 2. 测试SSH连接
在PowerShell中运行：
```bash
ssh -T git@github.com
```

### 3. 在Cursor中使用SSH

#### 克隆仓库（SSH方式）
```bash
git clone git@github.com:username/repository.git
```

#### 添加远程仓库（SSH方式）
```bash
# 查看当前远程仓库
git remote -v

# 添加SSH远程仓库
git remote add origin git@github.com:username/repository.git

# 修改现有远程仓库为SSH
git remote set-url origin git@github.com:username/repository.git
```

#### 推送代码
```bash
git push -u origin main
```

## 🛠️ 在Cursor中的快捷操作

### 使用命令面板
1. 按 `Ctrl + Shift + P`
2. 输入 "Git: Clone"
3. 粘贴SSH URL：`git@github.com:username/repo.git`

### 源代码管理面板
1. 按 `Ctrl + Shift + G` 打开源代码管理
2. 点击 "..." 菜单
3. 选择 "Remote" → "Add Remote"
4. 输入SSH URL

### 分支管理
1. 在状态栏左下角点击分支名
2. 选择 "Create new branch"
3. 输入分支名

## 🔧 常见问题解决

### SSH连接问题
如果遇到连接问题，可以：
1. 检查SSH密钥是否正确添加
2. 测试连接：`ssh -T git@github.com`
3. 检查防火墙设置

### 权限问题
确保SSH密钥文件权限正确：
```bash
# 在Git Bash中运行
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
```

### 多个Git账户
如果需要管理多个Git账户，创建SSH配置文件：
```bash
# 创建配置文件
nano ~/.ssh/config
```

添加内容：
```
# GitHub个人账户
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa

# GitHub工作账户
Host github-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_work
```

## 📝 验证设置

运行以下命令验证SSH设置：
```bash
ssh -T git@github.com
```

成功会显示：
```
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

## 🎯 现在您可以：

1. ✅ 使用SSH克隆仓库
2. ✅ 安全地推送和拉取代码
3. ✅ 在Cursor中享受完整的Git集成
4. ✅ 无需每次输入用户名和密码

## 🔗 有用的链接

- [GitHub SSH设置指南](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [GitLab SSH设置指南](https://docs.gitlab.com/ee/ssh/)
- [Cursor Git集成文档](https://cursor.sh/docs)
