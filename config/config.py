class config:
    # Basic configuration: If you are unsure how to obtain the Bot ID, simply start the bot and it will be logged in the console.
    prefix = '!'
    botID = '66f836f3d30fb7cf5a76b6a2'
    botName = 'ALEX_TIP'
    ownerName = 'X.FEAR'
    roomName = '<#FF0000>ЛОФТ - <#F60000> ЗНАКОМСТВА 💌'
    coordinates = {
        'x': 5.0,
        'y': 16.0,
        'z': 5.0,
        'facing': 'FrontRight'
    }


class loggers:
    # The following settings are related to events. Each event log can be enabled or disabled. Note that turning these off will not affect their usage in the game.
    SessionMetadata = True
    messages = True
    whispers = True
    joins = True
    leave = True
    tips = True
    emotes = True
    reactions = True
    userMovement = True


class messages:
    # The following are optional and serve as a basic usage example for calling messages and replacing variables.
    invalidPosition = "Your position could not be determined."
    invalidPlayer = "{user} is not in the room."
    invalidUser = "User {user} is not found."
    invalidUsage = "Usage: {prefix}{commandName}{args}"
    invalidUserFormat = "Invalid user format. Please use '@username'."


class permissions:
    # You can add as many IDs as you want, for example: ['id1', 'id2'].
    owners = ['62e86343d99a0bb4471669e6']
    moderators = ['62e86343d99a0bb4471669e6']


class authorization:
    # To obtain your token, visit https://highrise.game/ and log in. Then, go to the settings and create a new bot. Accept the terms and generate a token.
    # To obtain your room ID, go to the game and navigate to the top right corner where the player list is displayed. Click on "Share this room" and copy the ID.
    room = '67d3aafa372aa6b9c7abfaf2'
    token = '27bf7252d9342c3e65461804d65267ba033b338b966a81ee818e1ab8a6be4a2c'
