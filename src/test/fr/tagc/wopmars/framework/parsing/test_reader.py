import unittest
import os
from unittest import TestCase
from fr.tagc.wopmars.framework.parsing.Reader import Reader
from fr.tagc.wopmars.framework.rule.IOFilePut import IOFilePut
from fr.tagc.wopmars.framework.rule.Option import Option
from fr.tagc.wopmars.toolwrappers.FooWrapper1 import FooWrapper1
from fr.tagc.wopmars.toolwrappers.FooWrapper2 import FooWrapper2
from fr.tagc.wopmars.toolwrappers.FooWrapper3 import FooWrapper3
from fr.tagc.wopmars.utils.PathFinder import PathFinder
from fr.tagc.wopmars.utils.SetUtils import SetUtils
from fr.tagc.wopmars.utils.exceptions.WopMarsParsingException import WopMarsParsingException


class TestReader(TestCase):

    def setUp(self):
        s_root_path = PathFinder.find_src(os.path.dirname(os.path.realpath(__file__)))

        s_path_to_example_definition_file = s_root_path + "resources/example_def_file.yml"
        s_path_to_not_existing_example_definition_file = s_root_path + "definition_file_that_doesnt_exists.yml"
        s_path_to_wrong_example_definition_file1 = s_root_path + "resources/example_def_file_wrong_yaml.yml"
        s_path_to_wrong_example_definition_file2 = s_root_path + "resources/example_def_file_wrong_grammar.yml"
        s_path_to_wrong_example_definition_file3 = s_root_path + "resources/example_def_file_wrong_grammar2.yml"

        s_path_to_wrong_example_definition_file4 = s_root_path + "resources/example_def_file_wrong_content.yml"
        s_path_to_wrong_example_definition_file5 = s_root_path + "resources/example_def_file_wrong_content2.yml"
        s_path_to_wrong_example_definition_file6 = s_root_path + "resources/example_def_file_wrong_content3.yml"
        s_path_to_wrong_example_definition_file7 = s_root_path + "resources/example_def_file_wrong_content4.yml"
        s_path_to_wrong_example_definition_file8 = s_root_path + "resources/example_def_file_wrong_content5.yml"

        s_path_to_wrong_example_definition_file9 = s_root_path + "resources/example_def_file_wrong_class_name.yml"
        s_path_to_wrong_example_definition_file10 = s_root_path + "resources/example_def_file_wrong_rule.yml"

        self.assertRaises(WopMarsParsingException, Reader, s_path_to_wrong_example_definition_file1)
        self.assertRaises(WopMarsParsingException, Reader, s_path_to_not_existing_example_definition_file)
        self.assertRaises(WopMarsParsingException, Reader, s_path_to_wrong_example_definition_file2)
        self.assertRaises(WopMarsParsingException, Reader, s_path_to_wrong_example_definition_file3)
        try:
            self.__my_reader = Reader(s_path_to_example_definition_file)
        except:
            raise AssertionError('Should not raise exception')

        self.__reader_wrong_content = Reader(s_path_to_wrong_example_definition_file4)
        self.__reader_wrong_content2 = Reader(s_path_to_wrong_example_definition_file5)
        self.__reader_wrong_content3 = Reader(s_path_to_wrong_example_definition_file6)
        self.__reader_wrong_content4 = Reader(s_path_to_wrong_example_definition_file7)
        self.__reader_wrong_content5 = Reader(s_path_to_wrong_example_definition_file8)
        self.__reader_wrong_content6 = Reader(s_path_to_wrong_example_definition_file9)
        self.__reader_wrong_content7 = Reader(s_path_to_wrong_example_definition_file10)

    def test_read(self):

        result = self.__my_reader.read()
        expected = set()

        expected.add(FooWrapper3(input_file_dict={'input1': IOFilePut('input1', 'the_second_file.txt')},
                                 output_file_dict={'output1': IOFilePut('output1', 'the final_file.txt')},
                                 option_dict={'param1': Option('param1', 10.285)}))

        expected.add(FooWrapper1(input_file_dict={'input1': IOFilePut('input1', 'aFile.txt')},
                                 output_file_dict={},
                                 option_dict={'param1': Option('param1', 5)}))

        expected.add(FooWrapper2(input_file_dict={},
                                 output_file_dict={'output1': IOFilePut('output1', 'the second file.txt')},
                                 option_dict={'param1': Option('param1', 'an_option')}))

        self.assertTrue((SetUtils.all_elm_of_one_set_in_one_other(result, expected) and
                         SetUtils.all_elm_of_one_set_in_one_other(expected, result)))

        self.assertRaises(WopMarsParsingException, self.__reader_wrong_content.read)
        self.assertRaises(WopMarsParsingException, self.__reader_wrong_content2.read)
        self.assertRaises(WopMarsParsingException, self.__reader_wrong_content3.read)
        self.assertRaises(WopMarsParsingException, self.__reader_wrong_content4.read)
        self.assertRaises(WopMarsParsingException, self.__reader_wrong_content5.read)
        self.assertRaises(WopMarsParsingException, self.__reader_wrong_content6.read)
        self.assertRaises(WopMarsParsingException, self.__reader_wrong_content7.read)

if __name__ == "__main__":
    unittest.main()