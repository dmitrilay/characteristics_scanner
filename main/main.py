from parser_spec import startParserSpecMVM
from data_requests import sending_data
from html_processing import startHtmlProcessing

data = sending_data()
startParserSpecMVM(data)
startHtmlProcessing()
