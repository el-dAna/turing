# Define the path where log files will be created
$logPath = "C:\Users\BenjaminAtadana\YandexDisk\MY_FILES\Visual_Studio_Codes\TURING\CI-CD\logs"

# Create the directory if it doesn't exist
if (-not (Test-Path -Path $logPath)) {
    New-Item -ItemType Directory -Path $logPath
}

# Define an array of dates for the log files
$logDates = @(
    "2024-10-01",
    "2024-10-02",
    "2024-10-03",
    "2024-10-04",
    "2024-10-05"
)

# Create log files with different dates
foreach ($date in $logDates) {
    # Create a log file name based on the date
    $logFileName = "log_$($date.Replace('-', '_')).log"
    $logFilePath = Join-Path -Path $logPath -ChildPath $logFileName
    
    # Write sample content to the log file
    @"
127.0.0.1 - - [$date:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024
127.0.0.1 - - [$date:10:05:23 +0000] "POST /api/login HTTP/1.1" 200 512
"@ | Set-Content -Path $logFilePath

    # Set the last write time of the file to the specified date
    $lastWriteTime = Get-Date $date
    Set-ItemProperty -Path $logFilePath -Name LastWriteTime -Value $lastWriteTime
    
    Write-Host "Created file: $logFileName with Last Write Time: $lastWriteTime"
}