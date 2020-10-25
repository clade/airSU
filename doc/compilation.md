# Compilation

## Micropython

Normalemement, il n'est pas nécéssaire de recompiler micropython cependant cette étage permet d'avoir sous la main les utilitaires pour créer les fichiers binaires. 

Télécharger Micropython pour le M5 ici :  <a href=https://github.com/m5stack/M5Stack_MicroPython>micropython pour le M5 stack</a> et suivre les instructions.

## Mémoire flash

L'ESP32 contient une mémoire flash qui est partagé en plusieurs espaces : bootloader, micropython et un système de fichier. Cette étape a pour but de 1/ créer une image binaire du système de fichier et 2/ regrouper tous les espaces de la mémoire flash en un seul fichier que l'on pourra distribuer. 

### Système de fichier : 

Mettre tous les fichiers dans un repertoire (ici /tmp/image) et executer:

    ./MicroPython_BUILD/components/mkspiffs/mkspiffs -c /tmp/image -b 4096 -p 256 -s 2621440 ./MicroPython_BUILD/build/spiffs_image.img

### Fusion des fichiers binaires : 

On utilise merge_bin_esp.py disponible <a href="https://github.com/vtunr/esp32_binary_merger">ici</a>. Il faut utiliser python2. 

Ligne de commande deppuis le repertoire MicroPython_BUILD/build: 

    python2 merge_bin_esp.py --output_name app_output.bin --bin_path bootloader/bootloader.bin phy_init_data.bin MicroPython.bin partitions_mpy.bin spiffs_image.img --bin_address 0x1000 0xf000 0x10000 0x8000 0x180000

Le fichier binaire se trouve dans output/app_output.bin



