# hand-gesture-cooling-fan

Outline: A camera captures hand gestures in real-time, utilizing solutions fine-tuned from Mediapipe, to accurately track and calculate the distance between two fingers (used as a control input). This distance data is transmitted via the Serial Port (UART) to an Arduino microcontroller. The Arduino then translates this data into analog signals, which are used to adjust the fan's speed. Simultaneously, an LCD display provides real-time feedback on the current fan speed, enabling users to monitor changes as they adjust their hand gestures.
