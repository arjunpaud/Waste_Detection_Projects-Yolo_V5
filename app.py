from wasteDetection.logger import logging
from wasteDetection.exception import AppExecption
import sys

try:
    a=3/"s"
except Exception as e:
    raise AppExecption(e,sys)