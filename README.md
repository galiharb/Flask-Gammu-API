# Flask gammu API

Cara menggunakan:
```
curl --header "Content-Type: application/json" --request POST --data '{"no_hp":"085277172858","pesan":"Hallo Sobat Covid hehe"}' http://localhost/sendsms
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


