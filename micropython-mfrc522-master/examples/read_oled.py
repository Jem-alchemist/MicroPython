import mfrc522
import machine
import ssd1306
i2c = machine.I2C (-1,machine.Pin(5),machine.Pin(4))
i2c.scan()
oled = ssd1306.SSD1306_I2C(128,64,i2c)
def do_read():
  rdr = mfrc522.MFRC522(14,13,12,2,15)
  oled.fill(0)
  oled.text("Ponga la targeta",0,0)
  oled.text("para leer datos...",0,10)
  oled.show()
  try:
    while True:
      (stat, tag_type) = rdr.request(rdr.REQIDL)
      if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
          targeta = "T.n:" + (str(raw_uid))
          if rdr.select_tag(raw_uid) == rdr.OK:
            key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
            if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
              z=rdr.read(8)(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
              texto=""
              for i in range(16):
                texto+=(chr(z[i]))
              oled.fill(0)
              oled.text("Targeta:",0,0)
              oled.text(str(z),0,10)
              oled.text("Datos:",0,20)
              oled.text(texto,0,30)
              oled.show()
              rdr.stop_crypto1()
            else:
              print("Authentication error")
          else:
            print("Failed to select tag")
  except KeyboardInterrupt:
    print("Bye")
do_read()
