Process I had to do to install on OSX:

* Install homebrew

* `git clone https://github.com/qmk/qmk_firmware.git` - now a submodule at the top level of this repo
* `cd qmk_firmware && git submodule update --init --recursive`
* `brew install dfu-programmer`
* ensure xcode command line tools are installed `xcode-select --install`
* `brew tap osx-cross/avr`
* `brew install avr-libc`  (takes a while)
* set up new keymap in qmk_firmware/keyboards/ergodox/keymaps/<keymap-name>
* (keymap must be named keymap.c)
* Optionally, remove all the other keymaps if you don't want to build them

* Maybe necessary? `brew cask install gcc-arm-embedded`

* `cd qmk_firmware/keyboards/ergodox && make <keymap-name>` or `make infinity-<keymap-name>`
* .hex file should exist in the qmk_firmware root dir as `ergodox_ez_<keymap_name>.hex`


== EZ
* Press reset button on the keyboard
* `teensy_loader_cli -mmcu=atmega32u4 -w <compiled_hex_file>`

== Infinity
Substitute your keymap name for `tnem`
* `make infinity-keymapname`

* `make infinity-tnem-.build/ergodox_infinity_tnem.bin`
* Connect left keyboard, put in flash mode
* `dfu-util --device 1c11:b007 -D ../../.build/ergodox_infinity_tnem.bin`

* `MASTER=right make infinity-tnem-.build/ergodox_infinity_tnem.bin`
* Connect right keyboard, put in flash mode
* `dfu-util --device 1c11:b007 -D ../../.build/ergodox_infinity_tnem.bin`
