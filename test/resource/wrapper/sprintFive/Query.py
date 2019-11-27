import threading

from wopmars.models import Rule


class Query(Rule):
    __mapper_args__ = {'polymorphic_identity': "sprintFive.Query"}

    def specify_input_table(self):
        return ["FooBase"]

    def run(self):
        print(threading._active)
        self.session().query(self.input_table("FooBase")).all()
