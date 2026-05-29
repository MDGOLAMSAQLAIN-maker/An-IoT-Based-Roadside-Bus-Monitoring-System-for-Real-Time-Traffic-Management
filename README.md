# 🚌 IoT-Based Roadside Bus Monitoring System

An intelligent IoT and AI-driven roadside monitoring system designed to track bus movement, calculate journey duration, estimate travel distance, and detect delays in real time using simulated GPS data and automated detection logic.

## 🚀 Features

* 📍 Simulated real-time GPS tracking
* 🚌 Automated bus detection system
* ⏱ Journey time calculation
* 📏 Distance measurement using the Haversine Formula
* 🚦 Delay detection based on expected travel time
* ☁️ Cloud/server reporting through API requests
* 📊 Real-time monitoring and analytics support

---

## 🛠 Technologies Used

* Python
* Requests API
* IoT Concepts
* GPS Simulation
* Mathematical Distance Calculation
* Real-Time Monitoring Logic

---

## ⚙️ System Workflow

1. Simulates bus detection using camera logic
2. Generates GPS coordinates for bus movement
3. Records start and end timestamps
4. Calculates:

   * Journey duration
   * Distance traveled
   * Delay status
5. Sends monitoring data to a remote traffic management server

---

## 📐 Distance Calculation

The project uses the Haversine Formula to calculate geographical distance between two GPS coordinates.

d = 2R \arcsin\left(\sqrt{\sin^2\left(\frac{\Delta\phi}{2}\right)+\cos(\phi_1)\cos(\phi_2)\sin^2\left(\frac{\Delta\lambda}{2}\right)}\right)

Where:

* (R) = Radius of Earth
* (\phi) = Latitude
* (\lambda) = Longitude

---

## 📦 Sample Output

```bash
Bus started at: 23.7542, 90.3621
Bus stopped at: 23.7812, 90.3914

Distance traveled: 4.12 km
Journey Time: 18.4 minutes
Status: On Time
```

---

## 🎯 Research Goals

* Improve urban traffic monitoring
* Reduce roadside congestion
* Enable smart transportation analytics
* Support intelligent traffic management systems

---

## 🔮 Future Improvements

* Real camera integration using OpenCV
* Live GPS hardware integration
* Dashboard visualization system
* AI-based traffic prediction
* Cloud database support
* Real-time notification system

---

## 👨‍💻 Author

**MD Golam Saqlain**
CSE Student | AI & IoT Research Enthusiast
