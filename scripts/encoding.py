def set_system_encoding_utf8():
    import sys, imp
    imp.reload(sys)
    sys.setdefaultencoding("utf-8")
