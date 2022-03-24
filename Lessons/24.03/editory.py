class BasicTask:

    def __init__(self, desc) -> None:
        self.desc = desc

class PhotoTask(BasicTask): pass

class TextTask(BasicTask): pass

class MarketingTask(BasicTask): pass

class BasicSpecialist:

    def __init__(self, name) -> None:
        self.name = name

    def get_taks(self):
        return [BasicTask]

class Photographer(BasicSpecialist):

    def __init__(self, name, camera) -> None:
        super().__init__(name)
        self.camera = camera

    def get_taks(self):
        return super().get_taks() + [PhotoTask]

class TechnicalWriter(BasicSpecialist):

    def __init__(self, name, experience) -> None:
        super().__init__(name)
        self.experience = experience

    def get_taks(self):
        return super().get_taks() + [TextTask, MarketingTask]

class editory_team:

    def __init__(self, tech_writer, photographer) -> None:
        self.tech_writer = tech_writer
        self.photographer = photographer

    def get_tech_writer(self):
        return self.tech_writer

    def get_photographer(self):
        return self.photographer

class chief_editor:

    def __init__(self, tasks, team) -> None:
        self.tasks = tasks
        self.team = team

    def process(self):
        for task in self.tasks:
            for member in self.team:
                if type(task) in member.get_taks():
                    print(f"{member.name} will take care of {task.desc}")