# 显示SSH公钥的PowerShell脚本
Write-Host "=== SSH公钥内容 ===" -ForegroundColor Green
Write-Host "请复制以下内容到GitHub/GitLab的SSH设置中：" -ForegroundColor Yellow
Write-Host ""

$publicKey = Get-Content "C:\Users\yasv\.ssh\id_rsa.pub" -Raw
Write-Host $publicKey -ForegroundColor Cyan

Write-Host ""
Write-Host "=== 下一步操作 ===" -ForegroundColor Green
Write-Host "1. 复制上面的公钥内容" -ForegroundColor White
Write-Host "2. 登录GitHub/GitLab" -ForegroundColor White
Write-Host "3. 进入SSH设置页面" -ForegroundColor White
Write-Host "4. 添加新的SSH密钥" -ForegroundColor White
Write-Host "5. 粘贴公钥内容并保存" -ForegroundColor White
