import random, time, csv


def generate_BLE_data():
	heart_rate = random.randint(60, 100) #ideal heart rate
	if random.random() < 0.5: #creates a float number between 0.0 - 1.0
		heart_rate += random.randint(10, 40) #adding abnormailty


	temperature = round(random.uniform(36.5, 37.5), 1) #ideal human body temperature in celcius 
	if random.random() < 0.5:
		temperature += round(random.uniform(0.5, 1.5), 1) #adding abnormailty 


	spo2 = random.randint(95, 100) #simulates ideal oxygen level in blood
	if random.random() < 0.5:
		spo2 -= random.randint(5, 10) #adding abnormaility


	
	return heart_rate, temperature, spo2


with open("simulated_physiological_data.csv", 'w', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(['Timestamp', 'HeartRate', 'Temperature', 'SpO2'])	

	for i in range(200):
		hr, temp, spo2 = generate_BLE_data()
		writer.writerow([time.strftime('%Y-%m-%d %H:%M:%S'), hr, temp, spo2])
		time.sleep(0.1) #