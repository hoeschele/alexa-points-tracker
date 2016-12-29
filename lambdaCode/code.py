""" Alexa Points Tracker Lambda function """ 
from __future__ import print_function 
import logging 
logger = logging.getLogger() 
from pprint import pprint 
import boto3 
from collections import OrderedDict
# --------------- Helpers that build all of the responses ----------------------
def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
def build_response(session_attributes, speechlet_response):
    
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
# --------------- Functions that control the skill's behavior ------------------
def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "OK"
    # If the user either does not reply to the welcome message or says something that is not understood, they will be prompted again with this text.
    reprompt_text = "Im waiting"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session)) def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for using the Points Tracker"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session)) def mapNames(name):
    mapOfNames={};
    mapOfNames['John'] = 'John'
    mapOfNames['johns'] = 'John'
    mapOfNames['Kevin'] = 'Kevin'
    mapOfNames['kevins'] = 'Kevin'
    mapOfNames['Joel'] = 'Joel'
    mapOfNames['joels'] = 'Joel'
    mapOfNames['Elliot'] = 'Elliot'
    mapOfNames['elliots'] = 'Elliot';
    mapOfNames['molly'] = 'molly'
    mapOfNames['mollys'] = 'molly'
    mapOfNames['Greg'] = 'Greg'
    mapOfNames['gregs'] = 'Greg'
    mapOfNames['mike'] = 'mike'
    mapOfNames['mikes'] = 'mike'
    returnName = mapOfNames[name]
    logger.error('returnname ='+ returnName)
    return returnName def saveGameState(playerState):
    dynamodb = boto3.resource('dynamodb')
    table = "game"
    key = 'id'
    item = {}
    item[key] = '3'
    item['players'] = playerState
    db_table = dynamodb.Table(table)
    try:
        db_table.put_item(Item=item)
    except Exception, e:
        print (e) def getGameState():
    dynamodb = boto3.resource('dynamodb')
    table = "game"
    db_table = dynamodb.Table(table)
    Key = '3';
    response = db_table.get_item(Key={'id':Key})
    item = response['Item']
    print(item)
    pprint(item)
    return item
    
def createSessionTwoPlayer(intent, session):
    cardTitle = 'create2p'
    print ("create2p")
    first = intent['slots']['first']['value']
    second = intent['slots']['second']['value']
    points = 0
    table = "game"
    playerState = {
                    "first":{
                        "name": first,
                        "points": points
                    },
                    "second":{
                        "name": second,
                        "points": points
                    }
                }
    
    saveGameState(playerState)
    repromptText = ''
    sessionAttributes = {}
    shouldEndSession = False
    
    speechOutput = 'OK, Creating a new game with ' + first + ' and ' + second + ".  Setting point totals for each to " +str(points);
    # gametype who is playing
    return build_response(sessionAttributes, build_speechlet_response(
        cardTitle, speechOutput, repromptText, shouldEndSession)) def createSessionThreePlayer(intent, session):
    cardTitle = 'create2p'
    first = intent['slots']['first']['value']
    second = intent['slots']['second']['value']
    third = intent['slots']['third']['value']
    points = 0
    table = "game"
    playerState = {
                    "first":{
                        "name": first,
                        "points": points
                    },
                    "second":{
                        "name": second,
                        "points": points
                    },
                    "third":{
                        "name": third,
                        "points": points
                    }
                }
    
    saveGameState(playerState)
    repromptText = ''
    sessionAttributes = {}
    shouldEndSession = False
    
    speechOutput = 'OK, Creating a new game with ' + first + ', '+ second +', and ' + third + ".  Setting point totals for each to " +str(points);
    return build_response(sessionAttributes, build_speechlet_response(
        cardTitle, speechOutput, repromptText, shouldEndSession)) def createSessionFourPlayer(intent, session):
    cardTitle = 'create2p'
    first = intent['slots']['first']['value']
    second = intent['slots']['second']['value']
    third = intent['slots']['third']['value']
    forth = intent['slots']['forth']['value']
    points = 0
    table = "game"
    playerState = {
                    "first":{
                        "name": first,
                        "points": points
                    },
                    "second":{
                        "name": second,
                        "points": points
                    },
                    "third":{
                        "name": third,
                        "points": points
                    },
                    "forth":{
                        "name": forth,
                        "points": points
                    }
                }
    
    saveGameState(playerState)
    repromptText = ''
    sessionAttributes = {}
    shouldEndSession = False
    
    speechOutput = 'OK, Creating a new game with ' + first + ', '+ second + ', '+ third +', and ' + forth + ".  Setting point totals for each to " 
+str(points);
    return build_response(sessionAttributes, build_speechlet_response(
        cardTitle, speechOutput, repromptText, shouldEndSession)) def createSessionFivePlayer(intent, session):
    cardTitle = 'create2p'
    first = intent['slots']['first']['value']
    second = intent['slots']['second']['value']
    third = intent['slots']['third']['value']
    forth = intent['slots']['forth']['value']
    fith = intent['slots']['fith']['value']
    points = 0
    table = "game"
    playerState = {
                    "first":{
                        "name": first,
                        "points": points
                    },
                    "second":{
                        "name": second,
                        "points": points
                    },
                    "third":{
                        "name": third,
                        "points": points
                    },
                    "forth":{
                        "name": forth,
                        "points": points
                    },
                    "fith":{
                        "name": fith,
                        "points": points
                    }                    
                }
    
    saveGameState(playerState)
    #getGameState()
    repromptText = ''
    sessionAttributes = {}
    shouldEndSession = False
    
    speechOutput = 'OK, Creating a new game with ' + first + ', '+ second + ', '+ third +', '+ forth +', and ' + fith + ".  Setting point totals for each 
to " +str(points);
    return build_response(sessionAttributes, build_speechlet_response(
        cardTitle, speechOutput, repromptText, shouldEndSession)) def createSessionSixPlayer(intent, session):
    cardTitle = 'create2p'
    first = intent['slots']['first']['value']
    second = intent['slots']['second']['value']
    third = intent['slots']['third']['value']
    forth = intent['slots']['forth']['value']
    fith = intent['slots']['fith']['value']
    sixth = intent['slots']['sixth']['value']
    points = 0
    table = "game"
    playerState = {
                    "first":{
                        "name": first,
                        "points": points
                    },
                    "second":{
                        "name": second,
                        "points": points
                    },
                    "third":{
                        "name": third,
                        "points": points
                    },
                    "forth":{
                        "name": forth,
                        "points": points
                    },
                    "fith":{
                        "name": fith,
                        "points": points
                    }  ,
                    "sixth":{
                        "name": sixth,
                        "points": points
                    }                   
                }
    
    saveGameState(playerState)
    repromptText = ''
    sessionAttributes = {}
    shouldEndSession = False
    
    speechOutput = 'OK, Creating a new game with ' + first + ', '+ second + ', '+ third +', '+ forth +', '+ fith +', and ' + sixth + ".  Setting point 
totals for each to " +str(points);
    return build_response(sessionAttributes, build_speechlet_response(
        cardTitle, speechOutput, repromptText, shouldEndSession)) def createSession(intent, session):
    cardTitle = 'create'
    repromptText = ''
    sessionAttributes = {}
    shouldEndSession = False
    speechOutput = 'OK, Creating a new game, who is playing?'
    # gametype who is playing
    print ("create end")
    return build_response(sessionAttributes, build_speechlet_response(
        cardTitle, speechOutput, repromptText, shouldEndSession)) def increasePoints(intent, session):
    cardTitle = 'increase'
    name = intent['slots']['name']['value']
    number = intent['slots']['number']['value']
    repromptText = ''
    sessionAttributes = {}
    shouldEndSession = False
    actualName = mapNames(name)
    #parseInt(number)
    
    newPoints =-1
    pointsFromDB = -1
    gameState = getGameState()
    players = gameState['players']
    positionFromDB = ''
    for position,player in players.iteritems():
        pprint(player)
        if actualName == player['name']:
            positionFromDB = position
            pointsFromDB = player['points']
            newPoints= pointsFromDB + int(number)
    
    players[positionFromDB]['points'] = newPoints;
    saveGameState(players)
    
    output=actualName + ' had '+ str(pointsFromDB) +' points, and now has ' +str(newPoints)
  
    speechOutput = output
    return build_response(sessionAttributes, build_speechlet_response(
        cardTitle, speechOutput, repromptText, shouldEndSession)) def decreasePoints(intent, session):
    cardTitle = 'decrease'
    name = intent['slots']['name']['value']
    number = intent['slots']['number']['value']
    repromptText = ''
    sessionAttributes = {}
    shouldEndSession = False
    actualName = mapNames(name)
    newPoints =-1
    pointsFromDB = -1
    positionFromDB = ''
    gameState = getGameState()
    players = gameState['players']
    for position,player in players.iteritems():
        if actualName == player['name']:
            positionFromDB = position
            pointsFromDB = player['points']
            newPoints= pointsFromDB - int(number)
    
    players[positionFromDB]['points'] = newPoints;
    saveGameState(players)
    
    output=actualName + ' had '+ str(pointsFromDB) +' points, and now has ' +str(newPoints)
    speechOutput = output
    return build_response(sessionAttributes, build_speechlet_response(
        cardTitle, speechOutput, repromptText, shouldEndSession)) def setPointsSession(intent, session):
    cardTitle = 'set life'
    name = intent['slots']['name']['value']
    number = intent['slots']['number']['value']
    repromptText = ''
    sessionAttributes = {}
    shouldEndSession = False
    actualName = mapNames(name)
    
    positionFromDB = ''
    newPoints =-1
    pointsFromDB = -1
    gameState = getGameState()
    players = gameState['players']
    for position,player in players.iteritems():
        if actualName == player['name']:
            positionFromDB = position
            pointsFromDB = player['points']
            newPoints= int(number)
    
    players[positionFromDB]['points'] = newPoints;
    saveGameState(players)
    
    output=actualName + ' had '+ str(pointsFromDB) +' points, and now has ' +str(newPoints)
    speechOutput = output
    return build_response(sessionAttributes, build_speechlet_response(
        cardTitle, speechOutput, repromptText, shouldEndSession)) def tellAllPoints(intent, session):
    cardTitle = 'tell all points'
    repromptText = ''
    sessionAttributes = {}
    shouldEndSession = False
    speechOutput = 'Point Totals are, '
    gameState = getGameState()
    players = gameState['players']
    for player in players.values():
        name = player['name']
        points = player['points']
        output=name +" " + str(points) + ", "
        speechOutput += output
        
    logger.error(speechOutput)
    
    return build_response(sessionAttributes, build_speechlet_response(
        cardTitle, speechOutput, repromptText, shouldEndSession)) def tellPlayerPoints(intent, session):
    cardTitle = 'tell points'
    name = intent['slots']['name']['value']
    repromptText = ''
    sessionAttributes = {}
    shouldEndSession = False
    actualName = mapNames(name)
    newPoints =-1
    pointsFromDB = -1
    gameState = getGameState()
    players = gameState['players']
    for position,player in players.iteritems():
        pprint(player)
        nameFromDB = player['name']
        if actualName == nameFromDB:
            pointsFromDB = player['points']
    output=actualName + 'has ' + str(pointsFromDB) + " points"
          
    speechOutput = output
    return build_response(sessionAttributes, build_speechlet_response(
        cardTitle, speechOutput, repromptText, shouldEndSession)) def whoHasTheMostPoints(intent, session):
    cardTitle = 'most points'
    repromptText = ''
    sessionAttributes = {}
    shouldEndSession = False
    logger.error('most life')
    gameState = getGameState()
    players = gameState['players']
    highestPoints = -1000000
    isTied = False
    tiedPlayers =''
    highestPlayer = ''
    for position,player in players.iteritems():
        if player['points'] > highestPoints:
            highestPlayer = player['name']
            highestPoints = player['points']
            isTied = False
        elif player['points'] == highestPoints:
            isTied = True
            tiedPlayers =tiedPlayers + player['name'] +", "
    if isTied:
        output = "The score is tied between the following players at "+str(highestPoints) + " points "+ tiedPlayers
    else:
        output = highestPlayer +" has the most points with " + str(highestPoints)
    speechOutput = output
    return build_response(sessionAttributes, build_speechlet_response(
        cardTitle, speechOutput, repromptText, shouldEndSession)) def whoHasTheLeastPoints(intent, session):
    cardTitle = 'least points'
    repromptText = ''
    sessionAttributes = {}
    shouldEndSession = False
    number = 1
    logger.error('most life')
    gameState = getGameState()
    players = gameState['players']
    lowestPoints = 1000000
    isTied = False
    tiedPlayers =''
    lowestPlayer = ''
    for position,player in players.iteritems():
        if player['points'] < lowestPoints:
            lowestPlayer = player['name']
            lowestPoints = player['points']
            isTied = False
        elif player['points'] == lowestPoints:
            isTied = True
            tiedPlayers =tiedPlayers + player['name'] +", "
    if isTied:
        output = "The score is tied between the following players at "+str(lowestPoints) + " points.  "+ tiedPlayers
    else:
        output = lowestPlayer +" has the least points with " + str(lowestPoints)
    speechOutput = output
    return build_response(sessionAttributes, build_speechlet_response(
        cardTitle, speechOutput, repromptText, shouldEndSession))
# --------------- Events ------------------
def on_session_started(session_started_request, session):
    """ Called when the session starts """
    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId']) def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response() def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """
    intent = intent_request['intent']
    intentName = intent_request['intent']['name']
    if intentName == 'SetPointsTotalIntent':
        return setPointsSession(intent, session)
    elif intentName == 'CreateThreePlayerGameIntent':
        return createSessionThreePlayer(intent, session)
    elif intentName == 'CreateFourPlayerGameIntent':
        return createSessionFourPlayer(intent, session)
    elif intentName == 'CreateTwoPlayerGameIntent':
        return createSessionTwoPlayer(intent, session)
    elif intentName == 'CreateThreePlayerGameIntent':
        return createSessionThreePlayer(intent, session)
    elif intentName == 'CreateFourPlayerGameIntent':
        return createSessionFourPlayer(intent, session)
    elif intentName == 'CreateFivePlayerGameIntent':
        return createSessionFivePlayer(intent, session)
    elif intentName == 'CreateSixPlayerGameIntent':
        return createSessionSixPlayer(intent, session)
        
    elif intentName == 'CreateGameIntent':
        return createSession(intent, session)
    elif intentName == 'DecreasePointsIntent':
        return decreasePoints(intent, session)
    elif intentName == 'IncreasePointsIntent':
        return increasePoints(intent, session)
    elif intentName == 'TellAllPointsIntent':
        return tellAllPoints(intent, session)
    elif intentName == 'TellPlayerPointsIntent':
        return tellPlayerPoints(intent, session)
    elif intentName == 'LeastPointsIntent':
        return whoHasTheLeastPoints(intent, session)
    elif intentName == 'MostPointsIntent':
        return whoHasTheMostPoints(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")
    print ("end intent") def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here
# --------------- Main handler ------------------
def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
         event['session']['application']['applicationId'])
    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"): raise ValueError("Invalid Application ID")
    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
