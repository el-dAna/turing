# ClearLogs.ps1
$logPath = "C:\Users\BenjaminAtadana\YandexDisk\MY_FILES\Visual_Studio_Codes\TURING\CI-CD\logs"  # Change this to your log directory
$daysToKeep = 2  # Number of days to keep logs

# Get the current date and calculate the cutoff date
$cutoffDate = (Get-Date).AddDays(-$daysToKeep)

Write-Host "Current Date: $(Get-Date)"
Write-Host "Cutoff Date: $cutoffDate"

# List files that will be checked for deletion
Get-ChildItem -Path $logPath -File | ForEach-Object {
    Write-Host "Checking file: $($_.Name) Last Write Time: $($_.LastWriteTime)"
}

# Remove log files older than the cutoff date
$removedFiles = Get-ChildItem -Path $logPath -File | Where-Object { $_.LastWriteTime -lt $cutoffDate }

if ($removedFiles) {
    $removedFiles | Remove-Item -Force
    Write-Host "Old log files cleared:"
    $removedFiles | ForEach-Object { Write-Host $_.Name }
} else {
    Write-Host "No old log files to clear."
}