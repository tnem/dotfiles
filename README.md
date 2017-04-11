Process I had to do to install on OSX:

* Install homebrew

* `git clone https://github.com/qmk/qmk_firmware.git` - maybe make as submodule later?
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
* `make infinity-keymapname`
* put left keyboard in flash mode
* (sudo?) `make infinity-<keymap-name>-dfu-util`

* put right in flash mode
* `make infinity-<keymap-name> MASTER=right`
* (sudo?) `make infinity-<keymap-name>-dfu-util MASTER=right`

