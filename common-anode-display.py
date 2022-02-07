#!/usr/bin/env python3

import time
import spidev

spi = None

def init_display():
    global spi

    spi = spidev.SpiDev()
    spi.open(0,0) # SPI-Schnittstelle aktivieren CS0 , Chanel 0
    spi.max_speed_hz = 50000 # SPI-Clock läuft mit maximal 50kHz, ist unbedingt nötig (MAX7219 laut Datenblatt max. 10MHz)
    spi.writebytes([0x0F,0x01]) # Displaytest ein,
    time.sleep(0.5) # 0,5s warten
    spi.writebytes([0x0F,0x00]) # Displaytest aus
    spi.writebytes([0x0C,0x01]) # Normalmodus
    spi.writebytes([0x0A,0x0F]) # Intensität maximal
    spi.writebytes([0x0B,0x07]) # Scanlimit alle anzeigen
    spi.writebytes([0x09, 0x00]) # Direktmodus aktivieren
    spi.close() # SPI-Schnittstelle in Ruhemodus (Ende Inizialisierung MAX7219)
    # im direkt Ansteuermodus
    # spi.writebytes([0x01,0b00000011]) # A
    # spi.writebytes([0x02,0b00000111]) # B
    # spi.writebytes([0x03,0b00000111]) # C
    # spi.writebytes([0x04,0b00000011]) # D
    # spi.writebytes([0x05,0b00000011]) # E
    # spi.writebytes([0x06,0b00000011]) # F
    # spi.writebytes([0x07,0b00000000]) # G
    # spi.writebytes([0x08,0b00000100]) # DP
    # #             Stelle   12345678

    #time.sleep(0.5)



def char_to_segments(s):
    (a, b, c, d, e, f, g, p) = (0, 0, 0, 0, 0, 0, 0, 0)

    if s == '0': (g, f, e, d, c, b, a, p) = (0, 1, 1, 1, 1, 1, 1, 0)
    if s == '1': (g, f, e, d, c, b, a, p) = (0, 0, 0, 0, 1, 1, 0, 0)
    if s == '2': (g, f, e, d, c, b, a, p) = (1, 0, 1, 1, 0, 1, 1, 0)
    if s == '3': (g, f, e, d, c, b, a, p) = (1, 0, 0, 1, 1, 1, 1, 0)
    if s == '4': (g, f, e, d, c, b, a, p) = (1, 1, 0, 0, 1, 1, 0, 0)
    if s == '5': (g, f, e, d, c, b, a, p) = (1, 1, 0, 1, 1, 0, 1, 0)
    if s == '6': (g, f, e, d, c, b, a, p) = (1, 1, 1, 1, 1, 0, 1, 0)
    if s == '7': (g, f, e, d, c, b, a, p) = (0, 0, 0, 0, 1, 1, 1, 0)
    if s == '8': (g, f, e, d, c, b, a, p) = (1, 1, 1, 1, 1, 1, 1, 0)
    if s == '9': (g, f, e, d, c, b, a, p) = (1, 1, 0, 1, 1, 1, 1, 0)
    if s == ' ': (g, f, e, d, c, b, a, p) = (0, 0, 0, 0, 0, 0, 0, 0)
    if s == 'A': (g, f, e, d, c, b, a, p) = (1, 1, 1, 0, 1, 1, 1, 0)
    if s == 'b': (g, f, e, d, c, b, a, p) = (1, 1, 1, 1, 1, 0, 0, 0)
    if s == 'C': (g, f, e, d, c, b, a, p) = (0, 1, 1, 1, 0, 0, 1, 0)
    if s == 'd': (g, f, e, d, c, b, a, p) = (1, 0, 1, 1, 1, 1, 0, 0)
    if s == 'E': (g, f, e, d, c, b, a, p) = (1, 1, 1, 1, 0, 0, 1, 0)
    if s == 'F': (g, f, e, d, c, b, a, p) = (1, 1, 1, 0, 0, 0, 1, 0)
    if s == 'G': (g, f, e, d, c, b, a, p) = (0, 1, 1, 1, 1, 0, 1, 0)
    if s == 'H': (g, f, e, d, c, b, a, p) = (1, 1, 1, 0, 1, 1, 0, 0)
    if s == 'I': (g, f, e, d, c, b, a, p) = (0, 1, 1, 0, 0, 0, 0, 0)
    if s == 'J': (g, f, e, d, c, b, a, p) = (0, 0, 0, 1, 1, 1, 0, 0)
    if s == 'K': (g, f, e, d, c, b, a, p) = (1, 1, 1, 0, 1, 0, 1, 0)
    if s == 'L': (g, f, e, d, c, b, a, p) = (0, 1, 1, 1, 0, 0, 0, 0)
    if s == 'O': (g, f, e, d, c, b, a, p) = (0, 1, 1, 1, 1, 1, 1, 0)
    if s == 'P': (g, f, e, d, c, b, a, p) = (1, 1, 1, 0, 0, 1, 1, 0)
    if s == 'q': (g, f, e, d, c, b, a, p) = (1, 1, 0, 0, 1, 1, 1, 0)
    if s == 'r': (g, f, e, d, c, b, a, p) = (1, 0, 1, 0, 0, 0, 0, 0)
    if s == 'S': (g, f, e, d, c, b, a, p) = (1, 1, 0, 1, 1, 0, 1, 0)
    if s == 't': (g, f, e, d, c, b, a, p) = (1, 1, 1, 1, 0, 0, 0, 0)
    if s == 'U': (g, f, e, d, c, b, a, p) = (0, 1, 1, 1, 1, 1, 0, 0)
    if s == '-': (g, f, e, d, c, b, a, p) = (1, 0, 0, 0, 0, 0, 0, 0)
    if s == '_': (g, f, e, d, c, b, a, p) = (0, 0, 0, 1, 0, 0, 0, 0)

    return (a, b, c, d, e, f, g, p)

def show_string(s):
    global spi

    for_segment_a = 0b00000000
    for_segment_b = 0b00000000
    for_segment_c = 0b00000000
    for_segment_d = 0b00000000
    for_segment_e = 0b00000000
    for_segment_f = 0b00000000
    for_segment_g = 0b00000000
    for_segment_p = 0b00000000

    for c in s:

        if c == '.':
            for_segment_p = for_segment_p | 1
        else:
            (a, b, c, d, e, f, g, p) = char_to_segments(c)
            for_segment_a = for_segment_a * 2 | a
            for_segment_b = for_segment_b * 2 | b
            for_segment_c = for_segment_c * 2 | c
            for_segment_d = for_segment_d * 2 | d
            for_segment_e = for_segment_e * 2 | e
            for_segment_f = for_segment_f * 2 | f
            for_segment_g = for_segment_g * 2 | g
            for_segment_p = for_segment_p * 2 | p

    # print('segment_a: {:0>8b}'.format(for_segment_a))
    # print('segment_b: {:0>8b}'.format(for_segment_b))
    # print('segment_c: {:0>8b}'.format(for_segment_c))
    # print('segment_d: {:0>8b}'.format(for_segment_d))
    # print('segment_e: {:0>8b}'.format(for_segment_e))
    # print('segment_f: {:0>8b}'.format(for_segment_f))
    # print('segment_g: {:0>8b}'.format(for_segment_g))
    # print('segment_p: {:0>8b}'.format(for_segment_p))

    spi.open(0,0) # SPI-Schnittstelle aktivieren CS0 , Channel 0
    spi.max_speed_hz = 50000 # SPI-Clock läuft mit maximal 50kHz, ist unbedingt nötig (MAX7219 laut Datenblatt max. 10MHz)

    spi.writebytes([0x01, for_segment_a]) # A
    spi.writebytes([0x02, for_segment_b]) # B
    spi.writebytes([0x03, for_segment_c]) # C
    spi.writebytes([0x04, for_segment_d]) # D
    spi.writebytes([0x05, for_segment_e]) # E
    spi.writebytes([0x06, for_segment_f]) # F
    spi.writebytes([0x07, for_segment_g]) # G
    spi.writebytes([0x08, for_segment_p]) # DP

    spi.close()


if __name__ == "__main__":
    init_display()
    show_string("--tESt--")
