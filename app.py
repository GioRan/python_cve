from twisted.internet import task
from twisted.internet import reactor

from Entity.PersonEntity import PersonEntity
from Services.PersonService import PersonService


loopTimes = 3
failInTheEnd = False
_loopCounter = 0


def runEverySecond():

    global _loopCounter

    if _loopCounter < loopTimes:
        _loopCounter += 1
        print('A new second has passed.')

        personEntity = PersonEntity("Gio", "Male")
        person = personEntity.getPerson();
        personService = PersonService()
        personService.savePerson(person)

        return

    if failInTheEnd:
        raise Exception('Failure during loop execution.')

    # We looped enough times.
    loop.stop()
    return

loop = task.LoopingCall(runEverySecond)

# Start looping every 1 second.
loopDeferred = loop.start(3.0)

reactor.run()

