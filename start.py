from os import path

from codelessengine.bootstrap import BootstrapCodeLessEngine
from codelessengine.project_manager import Project


engine = BootstrapCodeLessEngine()
project1 = Project(path.abspath(path.join('.', 'config/config.xml')))
engine.add_project(project1)
