from databases import Database


class BaseCrud:
    def __init__(self, db: Database) -> None:
        self.db = db