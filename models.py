from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import db


class Program(db.Base):
    __tablename__ = 'program'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    sections = relationship("Section", back_populates="program")
    def __str__(self):
        return f"{self.__tablename__ = },\n{self.id = },\n{self.name = },\n{self.start_date = },\n{self.end_date = },\n"

class Section(db.Base):
    __tablename__ = 'section'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    program_id = Column(Integer, ForeignKey('program.id'))
    program = relationship("Program", back_populates="sections")
    classes = relationship("Class", back_populates="section")
    def __str__(self):
        return f"{self.__tablename__ = },\n{self.id = },\n{self.name = },\n{self.start_date = },\n{self.end_date = },\n"

class Class(db.Base):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    section_id = Column(Integer, ForeignKey('section.id'))
    section = relationship("Section", back_populates="classes")
    def __str__(self):
        return f"{self.__tablename__ = },\n{self.id = },\n{self.name = },\n{self.start_date = },\n{self.end_date = },\n"
