import check50


@check50.check()
def check_file():
    '''tracker.py exists'''
    check50.exists("tracker.py")

@check50.check()
def run_file():
    '''run tracker.py'''
    try:
        check50.run("python3 tracker.py")
    except:
        check50.Failure("cannot run tracker.py")