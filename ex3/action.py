class BaseAction:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __gt__(self, other):
        if self.name == 'Rock':
            if other.name == 'Scissors':
                return True
        if self.name == 'Paper':
            if other.name == 'Rock':
                return True
        if self.name == 'Scissors':
            if other.name == 'Paper':
                return True

    def __lt__(self, other):
        if self.name == 'Rock':
            if other.name == 'Paper':
                return True
        if self.name == 'Paper':
            if other.name == 'Scissors':
                return True
        if self.name == 'Scissors':
            if other.name == 'Rock':
                return True

    def __eq__(self, other):
        return self.name == other.name


class NothingAction(BaseAction):
    def __init__(self):
        super().__init__('Nothing')


class RockAction(BaseAction):
    def __init__(self):
        super().__init__('Rock')


class PaperAction(BaseAction):
    def __init__(self):
        super().__init__('Paper')


class ScissorsAction(BaseAction):
    def __init__(self):
        super().__init__('Scissors')
