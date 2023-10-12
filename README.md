# hand-gesture-cooling-fan

Outline: A camera captures hand gestures in real-time, utilizing solutions fine-tuned from Mediapipe, to accurately track and calculate the distance between two fingers (used as a control input). This distance data is transmitted via the Serial Port (UART) to an Arduino microcontroller. The Arduino then translates this data into analog signals, which are used to adjust the fan's speed. Simultaneously, an LCD display provides real-time feedback on the current fan speed, enabling users to monitor changes as they adjust their hand gestures.

![IMG_4305 (1)](https://github.com/g3kooner/hand-gesture-cooling-fan/assets/137963143/e21aee69-d258-4146-a860-d88e2a4093a7)
