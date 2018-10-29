def run_macro(LOCATION, MACRO):
    """
    Executes a macro in an excel file

    Arguments:
        LOCATION {str} -- The full path the excel file
        MACRO {str} -- The name of the macro in the excel file
            (ex: module1.macro_name)
    """
    import win32com.client

    APP = "Excel.Application"
    EXCEL = win32com.client.DispatchEx(APP)

    EXCEL.Workbooks.Open(Filename=LOCATION)
    EXCEL.Application.Run(MACRO)
    EXCEL.Visible = False
    EXCEL.DisplayAlerts = False
    EXCEL.Workbooks.Close()
    EXCEL.Application.Quit()
    del EXCEL
