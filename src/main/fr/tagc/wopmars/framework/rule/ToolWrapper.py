"""
This module contains the ToolWrapper class
"""
from src.main.fr.tagc.wopmars.utils.DictUtils import DictUtils
from src.main.fr.tagc.wopmars.utils.exceptions.WopMarsParsingException import WopMarsParsingException


class ToolWrapper:
    """
    The class ToolWrapper is the superclass of the Wrapper which
    will be designed by the wrapper developers.
    """    
    def __init__(self, input_dict={}, output_dict={}, option_dict={}):
        """
        The constructor
        
        More documentation
        :param input_dict: dict(String: IOPUT)
        :param output_dict: dict(String: IOPUT)
        :param option_dict: dict(String: Option)
        :return: void
        """
        assert(type(input_dict) == dict and type(output_dict) == dict and type(option_dict) == dict)
        self.__input_file_dict = input_dict
        self.__output_file_dict = output_dict
        self.__option_dict = option_dict

    def is_content_respected(self):
        """
        This method checks if the parameters dictionary are properly formed, according to the specifications of the
        wrapper developer.

        :return:
        """

        # the options have to be checked first because they can alter the behavior of the is_input_respected and
        # is_output_respected methods
        # TODO faire et tester cette méthode -> aller voir les méthodes liées des ToolWrappers
        self.is_options_respected()

        self.is_input_respected()
        self.is_output_respected()

    def is_input_respected(self):
        """
        Check if the input dictionary given in the constructor is properly formed for the tool.

        If not, throws a WopMarsParsingException(3)
        :return:void
        """
        if set(self.__input_file_dict.keys()) != set(self.get_input_file()):
            raise WopMarsParsingException(3, "The given input variable's names are not correct, they should be: " +
                                          "\n\t'{0}'".format("'\n\t'".join(self.get_input_file())) +
                                          "\n" + "They are:" +
                                          "\n\t'{0}'".format("'\n\t'".join(self.__input_file_dict.keys()))
                                          )

    def is_output_respected(self):
        """
        Check if the output dictionary given in the constructor is properly formed for the tool.
        :return:
        """
        if set(self.__output_file_dict.keys()) != set(self.get_output_file()):
            raise WopMarsParsingException(3, "The given output variable's names are not correct, they should be: " +
                                          "\n\t'{0}'".format("'\n\t'".join(self.get_output_file())) +
                                          "\n" + "They are:" +
                                          "\n\t'{0}'".format("'\n\t'".join(self.__output_file_dict.keys()))
                                          )

    def is_options_respected(self):
        pass

    def __eq__(self, other):
        """
        Two ToolWrapper objects are equals if their attributes are equals
        :param other: ToolWrapper
        :return:
        """
        return (DictUtils.all_elm_of_one_dict_in_one_other(self.__input_file_dict, other.get_input_file_dict()) and
                DictUtils.all_elm_of_one_dict_in_one_other(self.__output_file_dict, other.get_output_file_dict()) and
                DictUtils.all_elm_of_one_dict_in_one_other(self.__option_dict, other.get_option_dict()))

    def __hash__(self):
        """
        Redefining the hash method allows ToolWrapper objects to be indexed in sets and dict
        :return:
        """
        return id(self)

    def get_input_file_dict(self):
        return self.__input_file_dict

    def get_output_file_dict(self):
        return self.__output_file_dict

    def get_option_dict(self):
        return self.__option_dict

    def create_base_object_from_class_names(self):
        # TODO this method will return (or set self attributes) from class names to base. Il n'y a peut etre pas besoin
        # que cette méthode soit dans self
        # TODO? Faire une espèce de factory de factory -> BaseFactory et WrapperFactory héritantes de Factory
        pass

# TODO vérifier que les méthodes importantes ont bien été réecrites par le développeur et que les autres ne le sont pas
# Ceci pourra être fait avec les décorateurs
    def get_input_file(self):
        return []

    def get_input_db(self):
        return []

    def get_output_file(self):
        return []

    def get_output_db(self):
        return []

    def get_options(self):
        # TODO get_options
        return {}