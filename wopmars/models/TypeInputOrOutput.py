from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from wopmars.Base import Base


class TypeInputOrOutput(Base):
    """
    This class is the model of the table ``wom_type_input_or_output``. It stores the two kind of entry named "input" and "output" which
    are associated with an ID.

    Fields:

    - id: INTEGER - primary key -arbitrary ID
    - is_input: VARCHAR(255) - the is_input of the type ("input" or "output")
    """

    __tablename__ = "wom_{}".format(__qualname__)

    is_input = Column(Boolean, primary_key=True, autoincrement=False)

    # One type_io is used by many tables
    one_x_to_many_tables = relationship("TableInputOutputInformation", back_populates="one_typeio_to_many_x")
    # One type_io is used by many files
    one_x_to_many_files = relationship("FileInputOutputInformation", back_populates="one_typeio_to_many_x")

    def __repr__(self):
        return "<class TypeInputOrOutput: is_input {}>".format(self.is_input)
