def run_macro(location, macro):
    """
    Executes a macro in an excel file

    Arguments:
        location {str} -- The full path the excel file
        macro {str} -- The name of the macro in the excel file
            (ex: module1.macro_name)
    """
    import win32com.client

    EXCEL = win32com.client.DispatchEx("Excel.Application")
    EXCEL.Workbooks.Open(Filename=location)
    EXCEL.Application.Run(macro)

    EXCEL.Visible = False
    EXCEL.DisplayAlerts = False

    EXCEL.Workbooks.Close()
    EXCEL.Application.Quit()
    del EXCEL
