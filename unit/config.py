import ujson

# Unit - ID
project = "tlvlp.iot.BazsalikON"
name = "soil"
mqtt_unit_id = "{}-{}".format(project, name)
unit_id_dict = {"unitID": mqtt_unit_id, "project": project, "name": name}

# Unit - Hardware
soil_moisture_sensor_pin = 32
light_sensor_pin = 33
growlight_pin = 25
growlight_relay_active_at = 0
growlight_persistence_path = "growlight_status"

# Unit - Scheduling
gc_collect_interval_sec = 1700
post_status_interval_sec = 600

# WIFI
wifi_ssid = "tllllvllllp"
wifi_password = "Bwnnibsinnwf0"
wifi_connection_check_interval_sec = 1

# MQTT
mqtt_connection_check_interval_sec = 1
mqtt_message_check_interval_ms = 100
mqtt_keepalive_sec = 200
mqtt_qos = 1
mqtt_use_ssl = True
mqtt_queue_size = 10
mqtt_checkout_payload = ujson.dumps(unit_id_dict)

# MQTT - Credentials
mqtt_server = "192.168.0.206"
mqtt_port = "8883"
mqtt_user = "tlvlp-iot-mcu"
mqtt_password = "Vm5c5o67oAWXBxwPIFwPAuL8VytC7F_7"

# MQTT - topics
mqtt_topic_status_request = "/global/status_request"
mqtt_topic_status = "/global/status"
mqtt_topic_inactive = "/global/inactive"
mqtt_topic_error = "/global/error"
mqtt_topic_control = "/units/{}/control".format(mqtt_unit_id)
mqtt_subscribe_topics = [mqtt_topic_status_request, mqtt_topic_control]




