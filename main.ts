function dreidel () {
    letter = randint(0, 3)
    if (letter == 0) {
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.happy), SoundExpressionPlayMode.InBackground)
        cuteBot.colorLight(cuteBot.RGBLights.ALL, 0xffff00)
        basic.showLeds(`
            . # # . .
            . . # . .
            . . # . .
            . . # . .
            # # # . .
            `)
    } else if (letter == 1) {
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.giggle), SoundExpressionPlayMode.InBackground)
        cuteBot.colorLight(cuteBot.RGBLights.ALL, 0x00ff00)
        basic.showLeds(`
            . # # . .
            . . # . .
            . . # . .
            . # # . .
            # . # . .
            `)
    } else if (letter == 2) {
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.hello), SoundExpressionPlayMode.InBackground)
        cuteBot.colorLight(cuteBot.RGBLights.ALL, 0x7f00ff)
        basic.showLeds(`
            . # # # #
            . . . . #
            . # . . #
            . # . . #
            . # . . #
            `)
    } else {
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.sad), SoundExpressionPlayMode.InBackground)
        cuteBot.colorLight(cuteBot.RGBLights.ALL, 0xff0000)
        basic.showLeds(`
            # . . . #
            # . # . #
            # . # . #
            # . # . #
            # # # # #
            `)
    }
}
function spin () {
    speed = 60
    music.setTempo(240)
    music.beginMelody(["E5", "G5", "E5", "G5", "E5", "G5", "E5", "-", "E5", "G5", "G5", "F5", "E5", "D5", "D5"], MelodyOptions.OnceInBackground)
cuteBot.colorLight(cuteBot.RGBLights.ALL, 0x0000ff)
    cuteBot.motors(speed, 0 - speed)
    basic.pause(1800)
    for (let index = 0; index < 20; index++) {
        speed = speed - 3
        cuteBot.motors(speed, 0 - speed)
        basic.pause(100)
    }
    cuteBot.stopcar()
}
input.onSound(DetectedSound.Loud, function () {
    basic.clearScreen()
    spin()
    dreidel()
})
let speed = 0
let letter = 0
input.setSoundThreshold(SoundThreshold.Loud, 220)
basic.showLeds(`
    . . # . .
    # # # # #
    # # # # #
    . # # # .
    . . # . .
    `)
