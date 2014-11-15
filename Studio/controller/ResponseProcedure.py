__author__ = 'victory'


class ResponseProcedure(object):
    def error(self):
        pass

    def before(self):
        pass

    def process(self):
        pass

    def after(self):
        pass

    def execute(self):
        try:
            self.before()
            result = {"status": 0, "message": "success", "data": self.process()}
            return JsonEncoder().encode(result)
        except:
            self.error()
            result = {"status": 1, "message": "error", "data": None}
            return JsonEncoder().encode(result)
        finally:
            self.after()


from json import JSONEncoder


class JsonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


