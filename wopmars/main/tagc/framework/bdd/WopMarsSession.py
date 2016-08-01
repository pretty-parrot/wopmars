"""
Module containing the WopMarsSession class.
"""
from sqlalchemy.sql.elements import ClauseElement

from wopmars.main.tagc.framework.bdd.WopMarsQuery import WopMarsQuery
from wopmars.main.tagc.utils.Logger import Logger


class WopMarsSession:
    """
    class WopMarsSession
    """

    def __init__(self, session, manager):
        """
        

        :return:
        """
        self.__manager = manager
        self.__session = session

    def commit(self):
        """
        Validate changes on the database.
        :return:
        """
        if self.something():
            Logger.instance().debug(str(self.__session) + " is about to commit.")
            Logger.instance().debug("Operations to be commited in session" + str(self.__session) + ": \n\tUpdates:\n\t\t" +
                                    "\n\t\t".join([str(k) for k in self.__session.dirty]) +
                                    "\n\tInserts:\n\t\t" +
                                    "\n\t\t".join([str(k) for k in self.__session.new]))
            # call on SQLManager commit method to use the lock
            self.__manager.commit(self.__session)

    def rollback(self):
        Logger.instance().debug("Operations to be rollbacked in session" + str(self.__session) + ": \n\tUpdates:\n\t\t" +
                                "\n\t\t".join([str(k) for k in self.__session.dirty]) +
                                "\n\tInserts:\n\t\t" +
                                "\n\t\t".join([str(k) for k in self.__session.new]))
        # call on SQLManager commit method to use the lock
        self.__manager.rollback(self.__session)

    def query(self, table):
        return WopMarsQuery(table, session=self.__session)

    def add(self, item):
        """
        Add.py
        :param item:
        :return:
        """
        self.__session.add(item)

    def add_all(self, collection):
        self.__session.add_all(collection)

    def delete(self, entry):
        self.__session.delete(entry)

    def delete_content(self, table):
        Logger.instance().debug("Deleting content of table " + table.__tablename__ + "...")
        self.__manager.execute(self.__session, table.__table__.delete())
        Logger.instance().debug("Content of table " + table.__tablename__ + " deleted.")

    def close(self):
        self.__session.close()

    def _session(self):
        return self.__session

    def something(self):
        return bool(self.__session.new) or bool(self.__session.dirty)

    def get_or_create(self, model, defaults=None, **kwargs):
        """
        This method allows to check if an entry exist in database and if not, create it. It also return a boolean
        which says if the entry has been created (True) or not (False)

        :param model: A SQLAlchemy model
        :param defaults: Dict containing the default parameter to use in fields if the entry doesn't exist.
        :param kwargs: Specify the values of the fields which are looked for. Create them if not.

        :return: tuple: (instance of the created entry, boolean)
        """
        instance = self.__session.query(model).filter_by(**kwargs).first()
        if instance:
            return instance, False
        else:
            params = dict((k, v) for k, v in kwargs.items() if not isinstance(v, ClauseElement))
            params.update(defaults or {})
            instance = model(**params)
            self.__session.add(instance)
            return instance, True

    def df_to_sql(self, df, *args, **kwargs):
        self.__manager.df_to_sql(df, *args, **kwargs)