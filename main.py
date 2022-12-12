def on_button_pressed_a():
    music.play_melody("E G E G E G E E ", 120)
    music.play_melody("E G G F E D - - ", 120)
input.on_button_pressed(Button.A, on_button_pressed_a)

def dreidel():
    global letter
    letter = randint(0, 3)
    if letter == 0:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.happy),
            SoundExpressionPlayMode.IN_BACKGROUND)
        cuteBot.color_light(cuteBot.RGBLights.ALL, 0xffff00)
        basic.show_leds("""
            . # # . .
                        . . # . .
                        . . # . .
                        . . # . .
                        # # # . .
        """)
    elif letter == 1:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.giggle),
            SoundExpressionPlayMode.IN_BACKGROUND)
        cuteBot.color_light(cuteBot.RGBLights.ALL, 0x00ff00)
        basic.show_leds("""
            . # # . .
                        . . # . .
                        . . # . .
                        . # # . .
                        # . # . .
        """)
    elif letter == 2:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.hello),
            SoundExpressionPlayMode.IN_BACKGROUND)
        cuteBot.color_light(cuteBot.RGBLights.ALL, 0x7f00ff)
        basic.show_leds("""
            . # # # #
                        . . . . #
                        . # . . #
                        . # . . #
                        . # . . #
        """)
    else:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.sad),
            SoundExpressionPlayMode.IN_BACKGROUND)
        cuteBot.color_light(cuteBot.RGBLights.ALL, 0xff0000)
        basic.show_leds("""
            # . . . #
                        # . # . #
                        # . # . #
                        # . # . #
                        # # # # #
        """)
def spin():
    global speed
    speed = 60
    basic.clear_screen()
    music.set_tempo(200)
    music.begin_melody(["E5","G5","E5","G5","E5","G5","E5","-","E5","G5","G5","F5","E5","D5","D5"], MelodyOptions.ONCE_IN_BACKGROUND)
    cuteBot.color_light(cuteBot.RGBLights.ALL, 0x0000ff)
    cuteBot.motors(speed, 0 - speed)
    basic.pause(randint(1000, 4000))
    for index in range(20):
        speed = speed - 3
        cuteBot.motors(speed, 0 - speed)
        basic.pause(100)
    cuteBot.stopcar()

def on_sound_loud():
    spin()
    dreidel()
input.on_sound(DetectedSound.LOUD, on_sound_loud)

speed = 0
letter = 0
input.set_sound_threshold(SoundThreshold.LOUD, 200)
basic.show_icon(IconNames.HEART)
basic.pause(1000)
basic.clear_screen()