#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame.camera
import pygame.image

camerasoftware_ico = """
   _________    __  _____________  ___            ____   _____
  / ____/   |  /  |/  / ____/ __ \/   |    _   __( __ ) |__  /
 / /   / /| | / /|_/ / __/ / /_/ / /| |   | | / / __  |  /_ <
/ /___/ ___ |/ /  / / /___/ _, _/ ___ |   | |/ / /_/ / ___/ /
\____/_/  |_/_/  /_/_____/_/ |_/_/  |_|   |___/\____(_)____/

 #########################################################
 #       PYTHON CAMERA v8.3 SOFTWARE - GH0ST S0FTWARE    #
 #########################################################
 #                       CONTACT                         #
 #########################################################
 #              DEVELOPER : İSMAİL TAŞDELEN              #
 #           GMAIL : pentestdatabase@gmail.com           #
 # Linkedin : https://www.linkedin.com/in/ismailtasdelen #
 #           Whatsapp : + 90 534 295 94 31               #
 #########################################################
"""

print camerasoftware_ico

pygame.camera.init()
kamera = pygame.camera.Camera(pygame.camera.list_cameras()[0])
kamera.start()
img = kamera.get_image()

star = "***************************************************************"

print star

img_name = raw_input("Fotoğrafınıza bir isim belirleyiniz (example.jpg) : ")
pygame.image.save(img, img_name)

yukleniyor = "Fotoğrafınız kaydedildi... ( Yükleniyor... %100 )"

print yukleniyor

print star

pygame.camera.quit()
