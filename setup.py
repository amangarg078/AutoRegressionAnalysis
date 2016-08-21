def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)
        print "Successfully imported: ",package

install_and_import('bs4')
install_and_import('numpy')
install_and_import('openpyxl')
