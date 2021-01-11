class Project:
    def __init__(self, data=None):
        self.data = data  if data  else self._get_data()


    @property
    def name(self):
        return self.data['name']

    @property
    def info(self):
        return self.data['info']

    def _get_data(self):
        return {'name':'Kirupa', 'info':'Name'}

    @classmethod
    def get_all(cls):
        output = [{'name':'Kirupa', 'info':'Name'},{'name':'Kirupa1', 'info':'Name1'}]
        return [cls(data) for data in output]


pro = Project().get_all()

