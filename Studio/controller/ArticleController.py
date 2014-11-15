__author__ = 'victory'
__author__ = 'victory'
from django.http import HttpResponse
from Studio.controller.ResponseProcedure import ResponseProcedure
from Studio.controller.Preconditions import Preconditions
import types


def queryHostArticle(request):
    page = int(request.GET["page"])

    def before(self):
        Preconditions.checkArgument(page > -1)
        return

    def process(self):
        return page

    procedure = ResponseProcedure()
    procedure.before = types.MethodType(before, procedure)
    procedure.process = types.MethodType(process, procedure)

    return HttpResponse(procedure.execute())


def queryOwnerArticle(request): pass


def queryTopicArticle(request): pass


def queryKeysArticle(request): pass


def queryCollectArticle(request): pass


def querySubscribeArticle(request): pass


def praiseArticle(request): pass


def cancelpraiseArticle(request): pass


def collectArticle(request): pass


def cancelCollectArticle(request): pass


def commentArticle(request): pass


def cancelCommentArticle(request): pass

