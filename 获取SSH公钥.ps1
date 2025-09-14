# 获取SSH公钥的PowerShell脚本
Write-Host "=== 正确的SSH公钥内容 ===" -ForegroundColor Green
Write-Host "请复制以下完整内容到GitHub/GitLab：" -ForegroundColor Yellow
Write-Host ""

# 读取公钥文件
$publicKeyPath = "C:\Users\yasv\.ssh\id_rsa.pub"
if (Test-Path $publicKeyPath) {
    $publicKey = Get-Content $publicKeyPath -Raw
    Write-Host $publicKey.Trim() -ForegroundColor Cyan
    Write-Host ""
    Write-Host "=== 验证公钥格式 ===" -ForegroundColor Green
    if ($publicKey.StartsWith("ssh-rsa ") -or $publicKey.StartsWith("ssh-ed25519 ")) {
        Write-Host "✅ 公钥格式正确" -ForegroundColor Green
    } else {
        Write-Host "❌ 公钥格式可能有问题" -ForegroundColor Red
    }
} else {
    Write-Host "❌ 公钥文件不存在" -ForegroundColor Red
}

Write-Host ""
Write-Host "=== 使用说明 ===" -ForegroundColor Green
Write-Host "1. 复制上面的完整公钥（包括 ssh-rsa 开头和邮箱结尾）" -ForegroundColor White
Write-Host "2. 登录GitHub: https://github.com/settings/keys" -ForegroundColor White
Write-Host "3. 点击 New SSH key" -ForegroundColor White
Write-Host "4. 标题填写: Cursor Git Management" -ForegroundColor White
Write-Host "5. 粘贴公钥内容" -ForegroundColor White
Write-Host "6. 点击 Add SSH key" -ForegroundColor White
