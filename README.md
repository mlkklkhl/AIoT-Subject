# AIoT-Subject
Learning Material for AIoT Subject

Cucumber RIS ESP32-S2 : https://th.cytron.io/p-cucumber-ris-esp32-s2-dev-board-with-sensors
Firmware: https://micropython.org/download/ESP32_GENERIC_S2/

- PIR sensor
  - Ref Doc: https://www.mpja.com/download/31227sc.pdf
  - Description:
    - ปรับการหน่วงเวลา Output ได้ 3 วินาที ถึง 5 วินาที
    - ปรับช่วงระยะตรวจจับได้ 3-7 เมตร
    - องศาการตรวจจับกว้าง 110 องศา
    - เลือก Output ได้ทั้ง Single Trigger และ Repeat Trigger
    - ใช้งานได้ทั้งแสงกลางวันและแสงกลางคืน
    - ไม่สามารถวัด range ได้
  - Setting:
    - Time: 3s
    - Sensitivity: 7m
    - Trigger: Repeat
  - Wire:
      - [+] -> [5V]
      - [OUT] -> [GPIO3]
      - [-] -> [GND]
  - Raw Data: pir_value
  - Convert Data: converted_pir_value
    
- LDR sensor -> [หากต้องการวัดความเข้มแสงไปใช้ BH1750 LUX]
  - Ref Doc: https://www.rajguruelectronics.com/Product/8748/ADIY%20LM393%20Comparator_Datasheet.pdf
  - Description:
    - สามารถวัด range ได้
  - Setting:
    - ?
  - Wire:
      - [VCC] -> [3V3]
      - [GND] -> [GND]
      - [D0] -> []
      - [A0] -> [GPIO4]
  - Raw Data: ldr_value
  - Convert Data: converted_ldr_value

- Mic seeed studio sensor
  - Ref Doc: https://wiki.seeedstudio.com/Grove-Sound_Sensor/
  - Description:
    - สามารถวัด range ได้
  - Setting:
    - ?
  - Wire:
      - [GND] -> [GND]
      - [VCC] -> [5V]
      - [NC] -> []
      - [SIG] -> [GPIO5]
  - Raw Data: mic_value
  - Convert Data: converted_mic_value
