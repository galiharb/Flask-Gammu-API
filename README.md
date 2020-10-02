# Flask Gammu API

Application Programming Interface (API) yang berguna untuk layanan sms gateway menggunakan framework FLASK

Cara menggunakan API:
```
curl --header "Content-Type: application/json" --request POST --data '{"no_hp":"085277XXXXXX","pesan":"Hallo ini Galih"}' http://localhost/sendsms
```

## Installasi (Ubuntu 18.04)
### Install dependensi menggunakan apt
```
apt-get update && apt-get install -y pkg-config gammu libgammu-dev libffi-dev
```

### Periksa Driver
Dapat Menggunakan Perintah Berikut dan temukan modem anda
```
lsusb
```
atau menggunakan perintah berikut:
```
dmesg | grep ttyUSB
```

### Setting Gammu
Dapat Menggunakan Perintah Berikut:
```
gammu-config
```
Sesuaikan dengan lokasi modem anda. misal /dev/ttyUSB0

### Clone Repository

```
git clone https://github.com/galiharb/Flask-Gammu-API.git
```

### Install requirements
Baru di testing menggunakan Python 2
```
pip install -r requirements.txt
```

### Jalankan Program
```
python init.py
```
