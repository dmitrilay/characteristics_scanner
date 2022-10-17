from parser_spec import startParserSpecMVM
from data_requests import sending_get_data, sending_spec
from html_processing import startHtmlProcessing
from files_and_folders import WorkFolderFiles


def auto():
    data = sending_get_data()
    startParserSpecMVM(data)
    data = startHtmlProcessing(data)
    sending_spec(data)
    WorkFolderFiles.file_cleaner()
