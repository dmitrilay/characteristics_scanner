from parser_spec import startParserSpecMVM
from data_requests import sending_data, sending_spec
from html_processing import startHtmlProcessing
from files_and_folders import WorkFolderFiles

data = sending_data()
# print(data)
startParserSpecMVM(data)
data = startHtmlProcessing()
# print(data)
sending_spec(data)

WorkFolderFiles.file_cleaner()
