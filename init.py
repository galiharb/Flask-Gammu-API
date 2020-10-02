from flask import Flask, jsonify, request
import gammu
import time

app = Flask(__name__)

@app.route("/api/covid19",methods=['POST'])
def covid_api():
	if request.method=='POST':
		posted_data = request.get_json()
		no_hp = posted_data['no_hp']
		pesan = posted_data['pesan']
		
		message = {
			'Text': pesan,
			'SMSC': {'Location': 1},
			'Number': no_hp,
		}

		sm = gammu.StateMachine()
		sm.ReadConfig()
		sm.Init()

		i=1
		while True:
			try:
				sm.SendSMS(message)
				break
			except:
				time.sleep(1)
				i=i+1
				if i == 60:
					hasil = {
						"hasil":"Time-Out",
					}
					return jsonify(hasil)
				continue
		
		hasil = {
			"hasil":"Berhasil",
		}
		return jsonify(hasil)

if __name__ == "__main__":
	app.run('0.0.0.0',port=80)
	#app.run()
