# 🏠 A Smart Sim – Home Assistant Custom Integration

A Smart Sim is a custom integration for Home Assistant that simulates various smart home sensors. It is ideal for testing automations, dashboards, and UI behavior without requiring physical devices.

---

## 📁 Folder Structure
components/ └── a_smart_sim/ ├── init.py ├── manifest.json ├── sensor.py └── binary_sensor.py

---

## 📦 Supported Sensors

- Temperature (`sensor`)
- Humidity (`sensor`)
- Light (`sensor`)
- Motion (`binary_sensor`)
- Presence (`binary_sensor`)

---

## ⚙️ Configuration Example (`configuration.yaml`)

```yaml
sensor:
  - platform: a_smart_sim
    sensors:
      - temperature
      - humidity
      - light
      - motion
      - presence
    interval: 5


sensors: List of sensors to simulate
interval: Update interval in seconds (applies to all sensors)


🚀 Setup Instructions
Copy the a_smart_sim folder into config/custom_components/
Add the configuration above to your configuration.yaml
Restart Home Assistant
Go to Developer Tools → States to view the simulated sensors

📝 Notes
Sensors update every interval seconds using async_track_time_interval
Logging is available via _LOGGER.debug() in each sensor’s async_update() method
Each sensor includes device_class and unique_id for better UI integration

📚 License
MIT License

---