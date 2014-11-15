__author__ = 'victory'


class Preconditions(object):
    @staticmethod
    def checkNotNull(*args):
        for arg in args:
            if arg == None:
                raise RuntimeError()

    @staticmethod
    def checkArgument(expression):
        if not expression:
            raise RuntimeError()
        else:
            print "Success"
        # if expression:
        # raise RuntimeError()